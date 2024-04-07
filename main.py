from discord import Intents, Client, Message
from dotenv import load_dotenv
from response import response
import os

# Load env api key
load_dotenv()
DISC_TOKEN = os.getenv('DISCORD_TOKEN')

# Bot setup
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

async def send_msg(msg: Message, usr_msg: str) -> None:
    if not usr_msg:
        print("Msg empty, intents not enabled")
        return
    
    try:
        response_text: str = response(usr_msg)
        await msg.channel.send(response_text)
    except Exception as Err:
        print(f"Error: {Err}")

# Handling startup for bot
@client.event
async def on_ready() -> None:
    print(f'{client.user} has connected to Discord!')

# Handling msgs
@client.event
async def on_message(msg: Message) -> None:
    if msg.author == client.user:
        return

    username: str = str(msg.author)
    user_msg: str = msg.content
    channel: str = str(msg.channel)

    print(f"User: {username} | Channel: {channel} | Msg: {user_msg}")

    await send_msg(msg, user_msg)

# Entry point
def main() -> None:
    client.run(DISC_TOKEN)

# Run
if __name__ == "__main__":
    main()