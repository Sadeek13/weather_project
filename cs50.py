import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import datetime


def get_city_from_ip():
    try:
        response = requests.get("http://ip-api.com/json/")
        data = response.json()
        return data["city"]
    except:
        return "Vijayawada" 


def get_weather(city):
    api_key = "9a8cc69ae773d64bee3aa3c59e16fb21"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res.json()
    except:
        return None


def send_email(subject, body):
    sender_email = "13syedsadeek@gmail.com"
    receiver_email = "13syedsadeek@gmail.com"
    app_password = "ljxc bwvu ioak elru"

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)


def send_weather_update():
    choice = input("Use current location automatically? (yes/no): ").strip().lower()
    
    if choice == "yes":
        city = get_city_from_ip()
    else:
        city = input("Enter your city name: ").strip()

    weather = get_weather(city)
    
    if not weather or "main" not in weather:
        print("❌ Could not get weather data. Check your city name or connection.")
        return

    temp = weather["main"]["temp"]
    humidity = weather["main"]["humidity"]
    condition = weather["weather"][0]["description"].capitalize()

    now = datetime.datetime.now().strftime("%A, %d %B %Y %I:%M %p")
    
    message = f"""📍 City: {city}
🌡 Temperature: {temp}°C
💧 Humidity: {humidity}%
☁ Condition: {condition}
🕒 Time: {now}
"""

    print(message)
    send_email(f"🌦 Weather Update for {city}", message)
    print("✅ Mail sent successfully.")

if __name__ == "__main__":
    send_weather_update()
