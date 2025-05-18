import aiosmtplib
from email.message import EmailMessage
from twilio.rest import Client
from app.config import settings

async def send_email(to_email: str, subject: str, body: str):
    message = EmailMessage()
    message["From"] = settings.EMAIL_FROM
    message["To"] = to_email
    message["Subject"] = subject
    message.set_content(body)

    await aiosmtplib.send(
        message,
        hostname=settings.EMAIL_HOST,
        port=settings.EMAIL_PORT,
        start_tls=True,
        username=settings.EMAIL_USERNAME,
        password=settings.EMAIL_PASSWORD,
    )

def send_sms(to_phone: str, body: str):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=settings.TWILIO_PHONE_NUMBER,
        to=to_phone,
    )
    return message.sid