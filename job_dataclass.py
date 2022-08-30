from dataclasses import dataclass

#dataclass for job information
@dataclass
class JobData:
    title: str
    place: str
    salary: str
    contract_type: str
    contact_email: str
