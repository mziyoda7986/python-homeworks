import pandas as pd
import sqlite3

#part1
con = sqlite3.connect('chinook.db')
customers = pd.read_sql_query("SELECT * FROM customers", con)
print(customers.head(10))

iris_df = pd.read_json('iris.json')
print('Shape:', iris_df.shape)
print('Columns:', iris_df.columns.tolist())

titanic_df = pd.read_excel('titanic.xlsx')
print(titanic_df.head(5))

flights_df = pd.read_parquet('flights')
print(flights_df.info())

movie_df = pd.read_csv('movie.csv')
print(movie_df.sample(10))

#part2
iris_df.columns = iris_df.columns.str.lower()
iris_selected = iris_df[['sepallength', 'sepalwidth']]
print(iris_selected.head())

older_passengers = titanic_df[titanic_df['Age'] > 30]
print(older_passengers)
print(titanic_df['Sex'].value_counts())

flight_info = flights_df[['origin', 'dest', 'carrier']]
print(flight_info.head())
print("Uniques destinations:", flights_df['dest'].nunique())

long_movies = movie_df[movie_df['duration'] > 120]
sorted_long_movies = long_movies.sort_values(by='director_facebook_likes', ascending=False)
print(sorted_long_movies)

#part3
print("Mean:", iris_df.mean(numeric_only=True))
print("Median:", iris_df.median(numeric_only=True))
print("Std:", iris_df.std(numeric_only=True))

print("Min age:", titanic_df['Age'].min())
print("Max age:", titanic_df['Age'].max())
print("Sum of ages:", titanic_df['Age'].sum())

likes = movie_df.groupby('director_name')['director_facebook_likes'].sum()
print("Top director by likes:", likes.sort_values(ascending=False).head(1))
top5 = movie_df[['movie_title', 'duration', 'director_name']].sort_values(by='duration', ascending=False).head(5)
print("Top5:", top5)

print(flights_df.isnull().sum())
if 'arr_delay' in flights_df.columns:
    flights_df['arr_delay'].fillna(flights_df['arr_delay'].mean(), inplace=True)