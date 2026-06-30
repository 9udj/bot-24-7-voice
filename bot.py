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
    await asyncio.sleep(2)
    channel = client.get_channel(VOICE_CHANNEL_ID)
    if channel:
        try:
            await channel.connect(self_deaf=True)
            print(f"✅ اتصل بـ: {channel.name}")
        except Exception as e:
            print(f"⚠️ خطأ: {e}")

@client.event
async def on_voice_state_update(member, before, after):
    if member == client.user and before.channel and not after.channel:
        print("⚡ طُرد البوت! يعود...")
        await asyncio.sleep(5)
        if not client.voice_clients:
            channel = client.get_channel(VOICE_CHANNEL_ID)
            if channel:
                try:
                    await channel.connect(self_deaf=True)
                    print(f"✅ عاد إلى: {channel.name}")
                except Exception as e:
                    print(f"⚠️ خطأ: {e}")

client.run(TOKEN)
 
