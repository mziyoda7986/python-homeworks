from bs4 import BeautifulSoup
import requests
import sqlite3
import csv
from datetime import datetime

with sqlite3.connect('jobs.db') as conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            apply_link TEXT,
            last_update TEXT,
            UNIQUE(title, company, location)
        )
    """)

def fetch_jobs():
    url = 'https://realpython.github.io/fake-jobs/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    jobs = []

    job_elements = soup.find_all('div', class_ = 'card-content')
    for job_elem in job_elements:
        title = job_elem.find('h2', class_ = 'title')
        company = job_elem.find('h3', class_ = 'company')
        location = job_elem.find('p', class_ = 'location')
        link = job_elem.find_all('a')
        apply_link = link[1]['href'] if len(link)>1 else None

        job_url = apply_link
        job_response = requests.get(job_url)
        job_soup = BeautifulSoup(job_response.text, 'html.parser')
        description_elem = job_soup.find('div', class_ = 'content')
        description = description_elem.get_text(strip=True) if description_elem else ""

        job = {
            'title' : title.get_text(strip=True) if title else '',
            'company' : company.get_text(strip=True) if company else '',
            'location' : location.get_text(strip=True) if location else '',
            'description' : description,
            'apply_link' : apply_link
        }
        jobs.append(job)
    return jobs

def update_jobs(jobs):
    for job in jobs:
        cursor.execute("""
            SELECT description, apply_link FROM jobs
            WHERE title = ? AND company = ? AND location = ?
        """, (job['title'], job['company'], job['location']))
        result = cursor.fetchone()

        if result is None:
            cursor.execute("""
                INSERT INTO jobs (title, company, location, description, apply_link, last_update)
                VALUES(?, ?, ?, ?, ?, ?)
            """,
            (job['title'], job['company'], job['location'], job['description'], job['apply_link'], datetime.utcnow().isoformat()))
        else:
            dec, alink = result
            if job['description'] != dec or job['apply_link'] != alink:
                cursor.execute("""
                    UPDATE jobs
                    SET description = ?, apply_link = ?, last_update = ?
                    WHERE title = ? AND company = ? AND location = ?
                """,
                (job['description'], job['apply_link'], datetime.utcnow().isoformat(), job['title'], job['company'], job['location']))
    conn.commit()

def filter_jobs(location=None, company = None):
    query = "SELECT title, company, location, description, apply_link, last_update FROM jobs WHERE 1=1"
    params = []
    if location:
        query += ' AND location = ?'
        params.append(location)
    if company:
        query += ' AND company = ?'
        params.append(company)
    cursor.execute(query, params)
    return cursor.fetchall()

def export_to_csv(jobs, filename = 'filtered_jobs.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Company', 'Location', 'Description', 'Apply link', 'Last update'])
        writer.writerows(jobs)

if __name__ == '__main__':
    jobs = fetch_jobs()
    update_jobs(jobs)

    filtered_jobs = filter_jobs(location='Stewartbury, AA')
    export_to_csv(filtered_jobs, 'jobs_in_stewartbury.csv')

    filtered_jobs = filter_jobs(company='Payne, Roberts and Davis')
    export_to_csv(filtered_jobs, 'jobs_at_payne_roberts_davis.csv')