from pydantic import BaseModel
from typing import List

# Pydantic model for validating the incoming resume data.
# When a user submits data to our API, Pydantic automatically checks 
# if the data matches the types specified below.
class ResumeInput(BaseModel):
    name: str               # The applicant's full name
    email: str              # The applicant's email address
    phone: str              # The applicant's phone number
    linkedin: str           # URL to their LinkedIn profile
    skills: str             # A string containing skills (e.g., "Python, FastAPI, React")
    education: List[str]    # A list of educational backgrounds (e.g., ["B.S. Computer Science", "High School"])
    projects: List[str]     # A list of projects built by the applicant
