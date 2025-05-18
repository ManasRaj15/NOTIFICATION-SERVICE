from pydantic import BaseModel
from enum import Enum
from datetime import datetime
from typing import Optional

class NotificationType(str, Enum):
    email = "email"
    sms = "sms"
    in_app = "in_app"

class NotificationStatus(str, Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"

class NotificationBase(BaseModel):
    user_id: int
    type: NotificationType
    message: str

class NotificationCreate(NotificationBase):
    email: Optional[str] = None    
    phone: Optional[str] = None    

class Notification(NotificationBase):
    id: int
    status: NotificationStatus
    created_at: datetime

    class Config:
        orm_mode = True