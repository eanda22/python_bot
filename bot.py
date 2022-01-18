# bot.py
import os
import time
from unicodedata import name
from urllib import response
import requests, json

import discord
# from discord_slash import SlashCommand, SlashContext
# from discord_slash.utils import manage_components
# from discord_slash.model import ButtonStyle
from discord.ext import commands, tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

# client = discord.Client()

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)
# slash = SlashCommand(client, sync_commands=True)
# client = discord.Client(intents=intents)

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f"{client.user} is connected to the following server: {GUILD}")


@client.command(name="hello")
async def hello(ctx):
    await ctx.channel.send("Hello!")

@client.command(name="advice")
async def advice(ctx):
    url = "https://api.adviceslip.com/advice"
    response = requests.get(url)
    final_advice = response.json()["slip"]["advice"]
    if response.status_code == 200:
        await ctx.channel.send(
            f"Here is a short and random piece of advice: \n"
            + final_advice
            )

@client.command(name="weather")
async def weather(ctx, arg):
    try:
        city_name = arg
        weather_data = _get_weather(city_name)
        temperature = weather_data["Temperature"]
        feels_like_temp = weather_data["Feels Like"]
        pressure = weather_data["Pressure"]
        humidity = weather_data["Humidity"]
        await ctx.channel.send(
            f"Weather for: {city_name} \n"
            + f"The temperature is {temperature} degrees Fahrenheit \n"
            + f"The temperature feels like {feels_like_temp} degrees Fahrenheit \n"
            + f"The pressure is {pressure} \n"
            + f"The humidity is {humidity}"
        )
    except Exception:
        await ctx.channel.send(
            "There was an error getting the weather information... \n"
            + f"Perhaps there is a typo in the city name: {city_name} ?"
        )


def _get_weather(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    api_key = "61014df7b199691919ecc0d5a097ebc8"
    full_url = base_url + "appid=" + api_key + "&q=" + city + "&units=imperial"
    response = requests.get(full_url)
    if response.status_code == 200:
        raw_data = response.json()
        main_data = raw_data["main"]
        final_data = {
            "Temperature": main_data["temp"],
            "Feels Like": main_data["feels_like"],
            "Pressure": main_data["pressure"],
            "Humidity": main_data["humidity"],
        }
        return final_data
    else:
        return Exception


client.run(TOKEN)
