# TIA Airspace Twitter Bot

## Description
TIA Airspace is a Twitter bot that posts flight information of a random aircraft in the Tribhuvan International Airport (VNKT) airspace every few hours. The bot utilizes Flight Radar to request real-time flight information, providing followers with updates on aircraft movements in the area.

## Motivation
The motivation behind creating this project was to develop a fun Twitter bot related to aviation. Despite encountering challenges with API pricing constraints, the project aims to bring aviation enthusiasts together by sharing interesting flight details.

## Flight Selection Process
The Twitter bot selects flight details using the Flight Radar API, which allows it to search for aircraft around a specific area using the `flights/list-in-boundary` request. This ensures that the posted flight details are relevant to the Tribhuvan International Airport airspace.

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

## Technology Stack
The project is built using:
- Python with Tweepy for Twitter API integration
- Requests for making API calls
- Urllib3 for web scraping aircraft images

## Requirements
To run or deploy the Twitter bot, ensure you have the necessary packages installed by running:
```bash
pip install -r requirements.txt
