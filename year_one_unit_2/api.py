import requests
import json

def datafinder(url):
    data = requests.get(url).json()
    info = data["currently"]["summary"]
    print(info)

datafinder("https://api.darksky.net/forecast/eb0901072e2680edba98a854d58ebfce/40.7128,74.0060")
