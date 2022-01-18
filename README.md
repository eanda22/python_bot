# Python Discord Bot 

This bot is just for me to play around with the discord.py API and practice Python.

# Setup env
Create a .env file: <br>
Replace {your-bot-token} and {your-guild-name} with the correct bot token and guild name
```
# .env
DISCORD_TOKEN={your-bot-token}
DISCORD_GUILD={your-guild-name}
WEATHER_API_KEY={your-api-key}
```

# Commands

Every command starts with an exclamation point: ! <br>
There are currenlty two commands:

## Hello
!hello <br>
This will just have the bot respond "Hello!" in whatever channel you enter the command in

## Weather 
!weather <city_name> <br>
This will take a city name as an argument, and returns:
- the temperature 
- what temperature it feels like
- The pressure
- The humidity

This command uses the OpenWeatherMap API to get the weather data <br>
Link: https://developer.accuweather.com/?gclid=CjwKCAiA55mPBhBOEiwANmzoQkeVVsre809PcMcX4fNyvRLDulM1PNpDlNpF-lER-MjyHS0TdkUvVBoCRS8QAvD_BwE

## Advice
!advice <br>
This will give you a random piece of advice <br>
Uses the advice slip API <br>
Link: https://api.adviceslip.com/