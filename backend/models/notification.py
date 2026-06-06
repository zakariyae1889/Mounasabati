from __future__ import annotations
import uuid
from uuid import UUID
from datetime import datetime,timezone
from typing import Optional,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship

if TYPE_CHECKING:
    from .user import User


class Notification(SQLModel, table=True):
    __tablename__ = "notifications"
    
    # المعرف الأساسي UUID إجباري
    id: UUID = Field(
        default_factory=uuid.uuid4, 
        primary_key=True, 
        index=True, 
        nullable=False
    )
    
    # ربط الإشعار بمستخدم معين (إجباري)
    user_id: UUID = Field(foreign_key="users.id", nullable=False)
    
    # تفاصيل الإشعار
    title: str = Field(nullable=False)
    body: str = Field(nullable=False)
    
    # حالة الإشعار (هل قرأه المستخدم أم لا؟)
    is_read: bool = Field(default=False, nullable=False)
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updateed_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


    # العلاقة مع جدول المستخدمين
    user: Optional["User"] = Relationship(back_populates="notifications")