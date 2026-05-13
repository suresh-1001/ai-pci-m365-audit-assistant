from sqlalchemy import Column, Integer, String, Text
from app.db.session import Base

class Finding(Base):
    __tablename__ = "findings"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    risk_level = Column(String, nullable=False)
    business_impact = Column(Text, nullable=False)
    pci_reference = Column(String, nullable=True)
    status = Column(String, default="open", nullable=False)
