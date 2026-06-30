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
    await join_voice_channel()

async def join_voice_channel():
    while True:
        try:
            channel = client.get_channel(VOICE_CHANNEL_ID)
            if channel is None:
                print("❌ ما لقيت الروم!")
                await asyncio.sleep(30)
                continue

            for vc in client.voice_clients:
                await vc.disconnect(force=True)

            await asyncio.sleep(1)
            await channel.connect()
            print(f"✅ اتصل بـ: {channel.name}")

        except Exception as e:
            print(f"⚠️ خطأ: {e}")

        await asyncio.sleep(30)

@client.event
async def on_voice_state_update(member, before, after):
    if member == client.user and before.channel and not after.channel:
        print("⚡ طُرد البوت! يعود الآن...")
        await asyncio.sleep(2)
        try:
            for vc in client.voice_clients:
                await vc.disconnect(force=True)
            await asyncio.sleep(1)
            channel = client.get_channel(VOICE_CHANNEL_ID)
            if channel:
                await channel.connect()
                print(f"✅ عاد إلى: {channel.name}")
        except Exception as e:
            print(f"⚠️ خطأ عند العودة: {e}")

client.run(TOKEN)
