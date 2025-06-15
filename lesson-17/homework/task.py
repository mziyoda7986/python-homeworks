import sqlite3
import pandas as pd

conn = sqlite3.connect('chinook.db')
customers = pd.read_sql("SELECT * FROM customers", conn)
invoices = pd.read_sql("SELECT * FROM invoices", conn)
merged_df = pd.merge(customers, invoices, on='CustomerId', how='inner')
invoice_count = merged_df.groupby('CustomerId').size().reset_index(name='InvoiceCount')
print(invoice_count.head())

movies = pd.read_csv('movie.csv')
df1 = movies[['director_name', 'color']].dropna()
df2 = movies[['director_name', 'num_critic_for_reviews']].dropna()
left_join = pd.merge(df1, df2, on='director_name', how='left')
print("Left join rows:", len(left_join))
full_join = pd.merge(df1, df2, on='director_name', how='outer')
print("Full outer join rows:", len(full_join))

titanic = pd.read_excel('titanic.xlsx')
grouped = titanic.groupby('Pclass').agg({
    'Age' : 'mean',
    'Fare' : 'sum',
    'PassengerId' : 'count'
}).rename(columns={'PassengerId':'PassengerCount'})
print(grouped)

movie_group = movies.groupby(['color', 'director_name']).agg({
    'num_critic_for_reviews':'sum',
    'duration':'mean'
})
print(movie_group.head())

flight_df = pd.read_parquet('flights')
flight_df['ArrDelay'] = pd.to_numeric(flight_df['ArrDelay'], errors='coerce')
flight_df['DepDelay'] = pd.to_numeric(flight_df['DepDelay'], errors='coerce')
flight_group = flight_df.groupby(['Year', 'Month']).agg({
    'Flight_Number_Reporting_Airline': 'count',
    'ArrDelay': 'mean',
    'DepDelay': 'max'
})
print(flight_group.head())

def classify_age(age):
    return 'Adult' if age >= 18 else 'Child'

titanic['Age_Group'] = titanic['Age'].apply(classify_age)
print(titanic[['Age', 'Age_Group']].head())

employee = pd.read_csv('employee.csv')
employee['NormalizedSalary'] = employee.groupby('DEPARTMENT')['BASE_SALARY'].transform(
    lambda x : (x-x.min())/(x.max()-x.min())
)
print(employee[['DEPARTMENT', 'BASE_SALARY', 'NormalizedSalary']].head())

def duration_label(duration):
    if duration < 60:
        return 'Short'
    elif duration <= 120:
        return 'Medium'
    else:
        return 'Long'

movies['Duration_Class'] = movies['duration'].apply(duration_label)
print(movies[['duration', 'Duration_Class']].head(20))

def filter_survivors(df):
    return df[df['Survived'] == 1]
def fill_age(df):
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    return df
def add_fare_per_age(df):
    df['Fare_Per_Age'] = df['Fare']/df['Age']
    return df
titanic_pip = (
    titanic
    .pipe(filter_survivors)
    .pipe(fill_age)
    .pipe(add_fare_per_age)
)
print(titanic_pip[['Survived', 'Age', 'Fare', 'Fare_Per_Age']].head())

flight_df['DepDelay'] = pd.to_numeric(flight_df['DepDelay'], errors='coerce')
flight_df['AirTime'] = pd.to_numeric(flight_df['AirTime'], errors='coerce')
def filter_delayed_flights(df):
    return df[df['DepDelay'] > 30]
def add_delay_per_hour(df):
    df['Delay_Per_Hour'] = df['DepDelay'] / (df['AirTime'] /  60)
    return df
flight_pip = (
    flight_df
    .pipe(filter_delayed_flights)
    .pipe(add_delay_per_hour)
)
print(flight_pip[['DepDelay', 'AirTime', 'Delay_Per_Hour']].head())