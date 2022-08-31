from dataclasses import dataclass


@dataclass
class JobData:
    """
    dataclass representing job information
    """
    title: str
    place: str
    salary: str
    contract_type: str
    contact_email: str
