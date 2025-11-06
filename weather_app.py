import requests

API_KEY = "0dd112be48ebebb856eb2b57af9e2fb5"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input(" ป้อนชื่อเมืองที่ต้องการดูพยากรณ์อากาศ: ")

# พารามิเตอร์ส่งไปยัง API
params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric",
    "lang": "th"
}

# ดึงข้อมูล
response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print("\n ดึงข้อมูลสำเร็จ!\n")

    weather = data["weather"][0]["description"]
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]

    print(f" เมือง: {city}")
    print(f"สภาพอากาศ: {weather}")
    print(f" อุณหภูมิ: {temp}°C (รู้สึกเหมือน {feels_like}°C)")
    print(f"ความชื้น: {humidity}%")

else:
    print(" ดึงข้อมูลไม่สำเร็จ (Status:", response.status_code, ")")
