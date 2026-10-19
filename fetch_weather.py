import pandas as pd
import requests
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

cities = ["Lucknow", "Delhi", "Mumbai", "Chennai", "Shimla"]
all_data = []

def fetch (city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
    data = requests.get(url).json()
    all_data.append(data)
    data["queried_city"] = city
    return data

all_data = [fetch(city) for city in cities]

df = pd.json_normalize(all_data)
df["weather_main"] = df["weather"].str[0].str["main"]

cols = ["queried_city", "dt", "main.temp", "main.humidity", "main.pressure",
        "wind.speed", "rain.1h", "weather_main", "coord.lat", "coord.lon"]

df = df.reindex(columns=cols).rename(columns={
    "queried_city": "city",
    "main.temp": "temp_c",
    "main.humidity": "humidity",
    "main.pressure": "pressure",
    "wind.speed": "wind_speed",
    "rain.1h": "rain_1h",
    "coord.lat": "lat",
    "coord.lon": "lon",
})

df["rain_1h"] = df["rain_1h"].fillna(0)
df["timestamp_utc"] = pd.to_datetime(df["dt"], unit="s")
df = df.drop(columns="dt")

conn = sqlite3.connect("climate.db")
df.to_sql("weather", conn, if_exists="append", index=False)
weather_data = pd.read_sql("SELECT * FROM weather ORDER BY timestamp_utc",conn)
weather_data.to_csv("weather_data.csv",index = False)
conn.close()

print("Saved", len(df), "rows")