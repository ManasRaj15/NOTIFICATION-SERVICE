from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.notification import NotificationCreate, Notification
from app.db.database import database
from app.db.models import notifications
from sqlalchemy import select, update
from datetime import datetime
from app.services.notification_service import send_email, send_sms

router = APIRouter()

@router.post("/notifications", response_model=Notification)
async def create_notification(notification: NotificationCreate):
    max_retries = 3
    attempt = 0
    success = False

    query = notifications.insert().values(
        user_id=notification.user_id,
        type=notification.type,
        message=notification.message,
        status="pending",
        created_at=datetime.utcnow()
    ).returning(*notifications.c)
    created = await database.fetch_one(query)

    while attempt < max_retries and not success:
        try:
            if notification.type == "email":
                if not notification.email:
                    raise HTTPException(status_code=400, detail="Email is required for email notifications")
                await send_email(
                    to_email=notification.email,
                    subject="Notification",
                    body=notification.message,
                )
            elif notification.type == "sms":
                if not notification.phone:
                    raise HTTPException(status_code=400, detail="Phone number is required for SMS notifications")
                send_sms(to_phone=notification.phone, body=notification.message)
            elif notification.type == "in_app":
                pass

            update_query = (
                update(notifications)
                .where(notifications.c.id == created.id)
                .values(status="sent")
            )
            await database.execute(update_query)

            created = await database.fetch_one(select(notifications).where(notifications.c.id == created.id))
            success = True

        except Exception as e:
            attempt += 1
            if attempt == max_retries:
                update_query = (
                    update(notifications)
                    .where(notifications.c.id == created.id)
                    .values(status="failed")
                )
                await database.execute(update_query)
                raise HTTPException(status_code=500, detail=f"Failed to send notification after {max_retries} attempts")
            else:
                print(f"Attempt {attempt} failed: {e}. Retrying...")

    return created

@router.get("/users/{user_id}/notifications", response_model=List[Notification])
async def get_user_notifications(user_id: int):
    query = select(notifications).where(notifications.c.user_id == user_id)
    results = await database.fetch_all(query)
    return results