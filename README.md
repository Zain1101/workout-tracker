# Workout Tracker

This is a Python-based Workout Tracker that uses the [Nutritionix Exercise API](https://www.nutritionix.com/business/api) to interpret natural language workout descriptions and log them to a Google Sheet using the [Sheety API](https://sheety.co/).

## Features

- Accepts natural language input like "ran 3km and did 20 pushups"
- Converts it into structured data using Nutritionix
- Automatically logs the workout to a Google Sheet via Sheety
- Tracks:
  - Exercise name
  - Duration
  - Calories burned
  - Date and time

## Example

```bash
Tell about your workout:
ran 3km and did 20 pushups
