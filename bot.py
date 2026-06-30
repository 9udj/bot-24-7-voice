import discord
import asyncio
import os

TOKEN = os.environ.get("DISCORD_TOKEN")
VOICE_CHANNEL_ID = int(os.environ.get("VOICE_CHANNEL_ID", 0))

intents = discord.Intents.default()
intents.voice_states = True

client = discord.Client(intents=intents)

class SilentAudio(discord.AudioSource):
    def read(self):
        return b'\xf8\xff\xfe'
    
    def is_opus(self):
        return True

@client.event
async def on_ready():
    print(f"✅ البوت شغال: {client.user}")
    await connect_and_play()

async def connect_and_play():
    channel = client.get_channel(VOICE_CHANNEL_ID)
    if channel:
        try:
            vc = await channel.connect()
            vc.play(SilentAudio(), after=lambda e: print(f"Audio stopped: {e}"))
            print(f"✅ متصل في: {channel.name}")
        except Exception as e:
            print(f"⚠️ خطأ: {e}")

@client.event
async def on_voice_state_update(member, before, after):
    if member == client.user and before.channel and not after.channel:
        print("⚡ طُرد البوت! يعود...")
        await asyncio.sleep(3)
        if not client.voice_clients:
            await connect_and_play()

client.run(TOKEN)
