from datetime import datetime
import uuid

from sqlalchemy.ext.hybrid import hybrid_property
from app.extensions.db import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(
        db.String(40),
        primary_key=True,
        default=lambda: str(uuid.uuid4()),
    )
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = db.Column(db.Boolean, default=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def destroy(self):
        db.session.delete(self)
        db.session.commit()

    def discard(self):
        self.deleted = True
        self.save()

    def undiscard(self):
        self.deleted = False
        self.save()

    @hybrid_property
    def is_not_deleted(self):
        return not self.deleted