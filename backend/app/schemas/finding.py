from pydantic import BaseModel

class FindingOut(BaseModel):
    id: int
    title: str
    risk_level: str
    business_impact: str
    pci_reference: str | None = None
    status: str

    class Config:
        from_attributes = True
