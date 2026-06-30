# 🤖 بوت ديسكورد - يجلس في الروم 24/7

## كيف تشغله محلياً للتجربة

```bash
pip install -r requirements.txt
python bot.py
```

## متغيرات البيئة المطلوبة

| المتغير | الوصف |
|---------|-------|
| `DISCORD_TOKEN` | توكن البوت من Discord Developer Portal |
| `VOICE_CHANNEL_ID` | ID الروم الصوتي اللي تبيه يجلس فيه |

## كيف تحصل على VOICE_CHANNEL_ID

1. افتح ديسكورد
2. فعّل Developer Mode من الإعدادات → Advanced → Developer Mode
3. كليك يمين على اسم الروم الصوتي → Copy Channel ID

## الاستضافة المجانية على Railway

1. روح على [railway.app](https://railway.app) وسجّل بـ GitHub
2. اضغط **New Project → Deploy from GitHub repo**
3. ارفع الملفات على GitHub أو استخدم Railway CLI
4. من إعدادات المشروع → **Variables** أضف:
   - `DISCORD_TOKEN` = توكنك
   - `VOICE_CHANNEL_ID` = ID الروم
5. اضغط Deploy ✅

## الاستضافة المجانية على Render

1. روح على [render.com](https://render.com) وسجّل
2. اضغط **New → Background Worker**
3. اربطه بـ GitHub repo
4. أضف متغيرات البيئة
5. اضغط Create ✅

## ميزات البوت

- ✅ يدخل الروم تلقائياً عند التشغيل
- ✅ يعود فوراً إذا طُرد
- ✅ يتحقق كل 30 ثانية إنه لا يزال متصل
- ✅ يعيد الاتصال تلقائياً إذا انقطع
