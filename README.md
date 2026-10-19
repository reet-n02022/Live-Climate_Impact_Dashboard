# Live Climate Impact Dashboard

An automated pipeline that collects weather data for five Indian cities, cleans and stores it in a database, and shows it in an interactive Power BI dashboard.

![Dashboard](images/dashboard.png)

## What it does

- Fetches live weather data from the Open Weather API for Lucknow, Delhi, Mumbai, Chennai and Shimla.
- Cleans the data with pandas (renames columns, converts timestamps, fills missing rainfall).
- Stores every run in a SQLite database, so the history keeps growing.
- Runs automatically every day using Windows Task Scheduler.
- Exports a CSV that feeds a Power BI dashboard (city and date-range filters, temperature, humidity, rainfall).

## Tech stack

Python, pandas, requests, SQLite, Power BI, Windows Task Scheduler

## Data notes

- Timestamps are in UTC (IST is UTC + 5:30).
- OpenWeather omits the rain field when it is not raining, so missing rainfall is treated as 0 (an assumption).
- Data collection started on 9 Oct 2026, and daily automation started on 11 Oct 2026, so 10 Oct has no data.

## Limitations and future work

- Power BI Desktop is refreshed manually from the latest CSV
- Air quality (AQI), forecasting and more cities are planned
- NASA POWER data could be added for historical data
