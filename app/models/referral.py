from app.extensions.db import db

from .base import BaseModel


class ReferralCodeSequence(BaseModel):
    __tablename__ = "referral_code_sequences"

    # id from BaseModel used as UUID, but we need integer sequence; override
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    def __repr__(self):
        return f"<ReferralCodeSequence {self.id}>"
