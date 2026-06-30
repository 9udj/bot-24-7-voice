import discord
import asyncio
import os

TOKEN = os.environ.get("DISCORD_TOKEN")
VOICE_CHANNEL_ID = int(os.environ.get("VOICE_CHANNEL_ID", 0))

intents = discord.Intents.default()
intents.voice_states = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ البوت شغال: {client.user}")
    channel = client.get_channel(VOICE_CHANNEL_ID)
    if channel:
        try:
            await channel.connect()
            print(f"✅ اتصل بـ: {channel.name}")
        except Exception as e:
            print(f"⚠️ خطأ: {e}")

@client.event
async def on_voice_state_update(member, before, after):
    if member == client.user and before.channel and not after.channel:
        print("⚡ طُرد البوت! يعود...")
        await asyncio.sleep(3)
        channel = client.get_channel(VOICE_CHANNEL_ID)
        if channel and not client.voice_clients:
            try:
                await channel.connect()
                print(f"✅ عاد إلى: {channel.name}")
            except Exception as e:
                print(f"⚠️ خطأ: {e}")

client.run(TOKEN)
