                                                                                                                                           # Weather Checker

A Python CLI tool that fetches live weather data for any city, by chaining two public APIs together.

## What it does

- Takes a city name as input
- Uses a geocoding API to convert the city name into latitude/longitude coordinates
- Feeds those coordinates into a weather API to get the current temperature
- Runs in a loop so multiple cities can be checked until the user quits
- Handles invalid city names and network/timeout errors gracefully

## Tech used

- Python
- `requests` library for API calls
- Open-Meteo Geocoding API + Open-Meteo Weather API

## How to run

```bash
pip install requests
python weather_checker.py
```

## What I learned building this

- How to chain two separate API calls together, where one call's output becomes the next call's input
- The difference between a missing key in a JSON response versus an empty result — and why you need to test both
- Adding a request timeout and catching network-level exceptions (`ReadTimeout`, `RequestException`), not just bad data
- Avoiding redundant function calls — calling the same function multiple times for one input wastes API requests and slows the program down