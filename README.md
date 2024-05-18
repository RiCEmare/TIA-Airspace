# TIA Airspace Twitter Bot

## Description
TIA Airspace is a Twitter bot that posts flight information of a random aircraft in the Tribhuvan International Airport (VNKT) airspace every few hours. The bot utilizes Flight Radar API to request real-time flight information, providing followers with updates on aircraft movements in the area.

## Motivation
The motivation behind creating this project was to develop a fun Twitter bot related to aviation. If API pricing and limits weren't a thing, better ideas could've been executed but alas.

## Flight Selection Process
The Twitter bot selects flight details using the Flight Radar API, which allows it to search for aircraft around a specific area using the `flights/list-in-boundary` request. This ensures that the posted flight details are relevant to the Tribhuvan International Airport airspace. The `flights/details` request provides detailed information of the flight.

## Information Included in Each Post
Each post about a flight includes information such as:
- Flight name
- Airline
- Departure airport
- Arrival airport
- Departure time
- Arrival time
- Date
- Stock picture of the aircraft

## Requirements
To run or deploy the Twitter bot, ensure you have the necessary packages installed by running:
```bash
pip install -r requirements.txt
