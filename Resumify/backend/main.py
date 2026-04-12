from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from schemas import ResumeInput

# Initialize the FastAPI application
app = FastAPI(
    title="AI Resume Builder API",
    description="A beginner friendly FastAPI backend for an AI Resume Builder."
)

# Add CORS so the JS frontend can fetch from this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create an API endpoint for receiving the resume data via HTTP POST
@app.post("/resume")
def submit_resume(resume_data: ResumeInput):
    """
    Endpoint: POST /resume
    
    This function handles the incoming resume data.
    FastAPI takes the JSON payload and uses Pydantic to validate that it 
    matches the 'ResumeInput' schema.
    If the data is invalid, FastAPI automatically returns a helpful 422 Error to the user.
    If valid, the code below executes.
    """
    
    # We return a JSON response confirming successful validation
    return {
        "status": "success",
        "message": "Resume data validated and received successfully!",
        # model_dump() converts our Pydantic Object back into a standard Python dictionary
        "received_data": resume_data.model_dump()
    }
