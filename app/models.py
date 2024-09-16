from . import db
from datetime import datetime

class AuditLog(db.Model):
    __tablename__ = 'server_audit'
    id = db.Column(db.Integer, primary_key=True)
    server_id = db.Column(db.String(100), nullable=False)
    event_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_host = db.Column(db.String(255), nullable=False)
    query = db.Column(db.Text, nullable=False)
    database = db.Column(db.String(255), nullable=False)
    table_name = db.Column(db.String(255), nullable=True)
    operation = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return f"<AuditLog {self.id}>"
