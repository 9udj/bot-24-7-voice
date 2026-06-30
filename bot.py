import discord
import asyncio
import os

# ===== الإعدادات =====
TOKEN = os.environ.get("DISCORD_TOKEN")  # Token من متغيرات البيئة
VOICE_CHANNEL_ID = int(os.environ.get("VOICE_CHANNEL_ID", 0))  # ID الروم الصوتي
# ====================

intents = discord.Intents.default()
intents.voice_states = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ البوت شغال: {client.user}")
    await join_voice_channel()

async def join_voice_channel():
    """يدخل الروم الصوتي ويفضل فيه"""
    while True:
        try:
            channel = client.get_channel(VOICE_CHANNEL_ID)

            if channel is None:
                print("❌ ما لقيت الروم! تأكد من VOICE_CHANNEL_ID")
                await asyncio.sleep(30)
                continue

            # إذا مو متصل، يتصل
            if not client.voice_clients:
                await channel.connect()
                print(f"✅ اتصل بـ: {channel.name}")
            else:
                vc = client.voice_clients[0]
                # إذا انقطع الاتصال، يعيد الاتصال
                if not vc.is_connected():
                    await vc.disconnect()
                    await channel.connect()
                    print(f"🔄 أعاد الاتصال بـ: {channel.name}")
                # إذا في روم ثاني، ينتقل للروم الصحيح
                elif vc.channel.id != VOICE_CHANNEL_ID:
                    await vc.move_to(channel)
                    print(f"➡️ انتقل إلى: {channel.name}")

        except discord.errors.ClientException as e:
            print(f"⚠️ خطأ في الاتصال: {e}")
        except Exception as e:
            print(f"❌ خطأ غير متوقع: {e}")

        # يتحقق كل 30 ثانية
        await asyncio.sleep(30)

@client.event
async def on_voice_state_update(member, before, after):
    """يتحقق إذا طُرد من الروم ويعود فوراً"""
    if member == client.user and before.channel and not after.channel:
        print("⚡ طُرد البوت! يعود الآن...")
        await asyncio.sleep(3)
        channel = client.get_channel(VOICE_CHANNEL_ID)
        if channel:
            await channel.connect()
            print(f"✅ عاد إلى: {channel.name}")

client.run(TOKEN)
