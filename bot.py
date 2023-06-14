import discord
import responses
from discord.ext import commands
from responses import handle_response


# Send messages
async def send_message(message, user_message, is_private, user_roles=None):
    try:
        response = await handle_response(user_message, user_roles)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'YOUR-TOKEN-HERE'
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    @bot.event
    async def on_ready():
        print(f'{bot.user} is now running!')

    @bot.event
    async def on_message(message):
        # Make sure bot doesn't get stuck in an infinite loop
        if message.author == bot.user:
            return

        # Get data about the user
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Debug printing
        print(f"{username} said: '{user_message}' ({channel})")

        # If the user message contains a '?' in front of the text, it becomes a private message
        if user_message[0] == '?':
            user_message = user_message[1:]  # [1:] Removes the '?'
            await send_message(message, user_message, is_private=True,
                               user_roles=message.author.roles)
        else:
            await send_message(message, user_message, is_private=False,
                               user_roles=message.author.roles)

    # Remember to run your bot with your personal TOKEN
    bot.run(TOKEN)
