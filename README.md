# Weather Email Notifier 🌤📧

#### GitHub Username: Sadeek13
#### edX Username: syedsadeek
#### #### Video Demo: [Watch it here](https://youtu.be/huqliwvqB2A?si=zpGDc7FltHyKutio)


---

 
## Description:

This project is a command-line Python tool that fetches real-time weather data and sends it to the user via email. It combines location detection, API usage, and email automation into a single project.

---

## Features:

- Detects your city automatically based on your IP, or lets you enter it manually.
- Fetches live weather data using the OpenWeatherMap API.
- Sends temperature, humidity, and weather condition to your email.
- Includes proper exception handling.
- Tested with `pytest`.

---

## Technologies Used:

- Python 3
- Requests (for HTTP API calls)
- smtplib + email.mime (to send emails)
- OpenWeatherMap API
- Pytest (for testing)

---

## Sample Output:

📍 City: tokyo
🌡 Temperature: 12.54°C
💧 Humidity: 30%
☁ Condition: Scattered clouds
🕒 Time: Tuesday, 15 April 2025 11:06 PM

---

## Testing:

Basic unit tests were written to:

- Verify city is correctly fetched from IP.
- Check weather data fetch works for valid and invalid cities.

---

## What I Learned:

This project helped me learn how to:

- Work with APIs and JSON responses.
- Automate tasks using Python.
- Write test cases using pytest.
- Send emails programmatically.
