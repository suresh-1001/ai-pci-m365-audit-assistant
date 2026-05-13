from fastapi import APIRouter

router = APIRouter()

@router.get('')
def list_findings():
    return [
        {"id": 1, "title": "MFA not enforced for privileged users", "risk_level": "High", "business_impact": "Account takeover risk", "pci_reference": "8.4.2", "status": "open"}
    ]
