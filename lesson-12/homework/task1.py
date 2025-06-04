from bs4 import BeautifulSoup

with open("weather.html", 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

forecast = []

rows = soup.find('tbody').find_all('tr')
for row in rows:
    cols = row.find_all('td')
    day = cols[0].text
    temp = int(cols[1].text.replace("°C", ""))
    cond = cols[2].text
    forecast.append({
        'day':day,
        'temperature':temp,
        'condition':cond
    })

for i in forecast:
    print(f"{i['day']}: {i['temperature']}°C, {i['condition']}")

max_temp = max(i['temperature'] for i in forecast)
hot_days = [i['day'] for i in forecast if i['temperature'] == max_temp]
sunny_days = [i['day'] for i in forecast if i['condition'].lower() == 'sunny']

print("\nHottest days:", ', '.join(hot_days), f'{max_temp}°C')
print("Sunny days:", ', '.join(sunny_days))

total = sum(i['temperature'] for i in forecast)
print("\nAverage temperature:", f'{total/5}°C')