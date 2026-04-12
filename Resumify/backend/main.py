from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from schemas import ResumeInput
from model import analyze_project

# Initialize the FastAPI application
app = FastAPI(
    title="AI Resume Builder API",
    description="A beginner friendly FastAPI backend for an AI Resume Builder."
)

# Add CORS so the JS frontend can fetch from this API without browser blocks
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom exception handler to return very clear error messages when Pydantic validation fails
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    If the frontend sends an empty name or empty project list, Pydantic throws an error.
    This handler catches those errors and formats them cleanly for the user.
    """
    errors = exc.errors()
    
    # Extract readable error messages
    error_messages = []
    for err in errors:
        # err["loc"] looks like ('body', 'email')
        field_name = err["loc"][-1]
        error_messages.append(f"Validation failed for '{field_name}': {err['msg']}")
        
    return JSONResponse(
        status_code=422,
        content={
            "message": "Validation Error",
            "details": error_messages
        }
    )

# Create an API endpoint for receiving the resume data via HTTP POST
@app.post("/resume")
def submit_resume(resume_data: ResumeInput):
    """
    Endpoint: POST /resume
    
    FastAPI takes the JSON payload and uses our strict 'ResumeInput' schema.
    If any field is missing or empty, the custom exception handler above takes over!
    If valid, the code perfectly reaches this success block.
    """
    
    # We return a JSON response confirming successful validation exactly as requested
    return {
        "message": "Resume data validated and received successfully!",
        "received_data": resume_data.model_dump()
    }

# Create an API endpoint for analyzing project descriptions using AI
@app.post("/analyze")
def analyze_resume(resume_data: ResumeInput):
    """
    Endpoint: POST /analyze
    
    Accepts the validated resume JSON and runs each project description
    through our HuggingFace NLP Machine Learning model!
    """
    analysis_results = []
    score = 100
    
    # Loop through all the provided projects
    for project in resume_data.projects:
        # Get ML strength rating and suggestions for each project
        result = analyze_project(project)
        analysis_results.append(result)
        
        # Deduct 15 points if the NLP model flags it as weak
        if result["strength"] == "weak":
            score -= 15
            
    # Ensure score doesn't drop below 40
    score = max(40, score)
        
    return {
        "score": score,
        "analysis": analysis_results
    }
