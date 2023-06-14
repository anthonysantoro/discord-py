import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
client = commands.Bot(command_prefix="!", intents=intents)

@client.command()
async def commmandName(ctx, otherparameters):
    message = otherparameters # or other ways of getting user input
    response = handle_response(message)
    await ctx.send(response)

def handle_response(message, user_roles) -> str:
    p_message = message.lower()

    if p_message == 'hello':
        return 'Howdy'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == "!twitter":
        return "This is Axel's Twitter - https://twitter.com/axelkoto_"

    if p_message == "!live":
        if "Role Name" in user_roles:
            return "I'm not live on Twitch - https://twitch.tv/axelgg"
        else:
            return "Sorry, you don't have permission to use this command."

    return ""