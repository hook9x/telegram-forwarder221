from telethon import TelegramClient, events

# معلومات الدخول
api_id = 25760508
api_hash = "abd523c1a98e6441ad8b5866acdb2988"
phone_number = "+9647505705346"

# الرسالة الثابتة التي تريد إرسالها
auto_reply = "مرحبًا، شكرًا لتواصلك معنا. سيتم الرد عليك قريبًا."

client = TelegramClient("session_auto_reply", api_id, api_hash)

@client.on(events.NewMessage(incoming=True))
async def auto_responder(event):
    if event.is_private and not event.out:  # تأكد أنه من شخص في الخاص وليس من البوت نفسه
        sender = await event.get_sender()
        await client.send_message(sender.id, auto_reply)

async def main():
    await client.start(phone=phone_number)
    print("Auto-reply bot is running...")
    await client.run_until_disconnected()

client.loop.run_until_complete(main())
