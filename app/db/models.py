from sqlalchemy import Table, Column, Integer, String, DateTime, Enum, MetaData
import enum
from datetime import datetime

metadata = MetaData()

class NotificationType(str, enum.Enum):
    email = "email"
    sms = "sms"
    in_app = "in_app"

class NotificationStatus(str, enum.Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"

notifications = Table(
    "notifications",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False),
    Column("type", Enum(NotificationType), nullable=False),
    Column("message", String, nullable=False),
    Column("status", Enum(NotificationStatus), default=NotificationStatus.pending),
    Column("created_at", DateTime, default=datetime.utcnow),
)