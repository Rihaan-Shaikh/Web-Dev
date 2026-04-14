# Resumify
[![Ask DeepWiki](https://devin.ai/assets/askdeepwiki.png)](https://deepwiki.com/Rihaan-Shaikh/Web-Dev/tree/main/Resumify)

Resumify is a full-stack AI-powered resume builder designed to help users craft professional, impactful resumes. It features a sleek, real-time editor that generates LaTeX source code and provides intelligent feedback on project descriptions using a powerful NLP model.

## Features

*   **Real-Time LaTeX Generation**: As you type your information, Resumify dynamically generates a professionally formatted LaTeX resume source code.
*   **AI-Powered Feedback**: Leverages a Hugging Face NLP model to analyze the sentiment of your project descriptions, providing a strength rating (strong/weak), confidence score, and actionable suggestions for improvement.
*   **Overall Resume Score**: Calculates a score from 40-100 based on the AI analysis of your projects, giving you a quick measure of your resume's impact.
*   **Live Preview & Export**: Preview a simple HTML version of your resume, download the `.tex` file, or print directly to PDF.
*   **Robust Backend Validation**: Utilizes FastAPI and Pydantic to ensure all required fields are filled, providing clear error messages for invalid submissions.
*   **Modern UI**: A clean, dark-mode interface built with vanilla HTML, CSS, and JavaScript.
*   **Auto-Save Drafts**: Automatically saves your progress to the browser's local storage so you never lose your work.

## Tech Stack

*   **Frontend**: HTML, CSS, Vanilla JavaScript
*   **Backend**: Python, FastAPI
*   **AI/ML**: Hugging Face Transformers (`distilbert-base-uncased-finetuned-sst-2-english`)
*   **Data Validation**: Pydantic
*   **Server**: Uvicorn

## Project Structure

```
Resumify/
├── backend/
│   ├── main.py           # FastAPI app, defines API endpoints
│   ├── model.py          # Handles NLP analysis with Hugging Face
│   ├── requirements.txt  # Python dependencies
│   └── schemas.py        # Pydantic models for data validation
└── frontend/
    └── index.html        # Single-page application UI and logic
```

## Setup and Installation

Follow these steps to run Resumify locally.

### 1. Clone the Repository

```bash
git clone https://github.com/rihaan-shaikh/web-dev.git
cd web-dev/Resumify
```

### 2. Set Up the Backend

The backend server powers the validation and AI analysis features.

```bash
# Navigate to the backend directory
cd backend

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Install the required Python packages
pip install -r requirements.txt

# Run the FastAPI server
# The first time you run this, it will download the NLP model (~250MB)
uvicorn main:app --reload
```

The server will be running at `http://127.0.0.1:8000`.

### 3. Launch the Frontend

Navigate to the `frontend` directory and open the `index.html` file in your web browser.

```bash
# From the project root (Resumify/)
cd frontend
# Open index.html in your browser
```

## How It Works

1.  **Fill in Details**: Use the input fields on the left panel to add your personal information, education, experience, projects, and more.
2.  **Live LaTeX Output**: The "LaTeX Source" card on the right updates in real-time as you type.
3.  **Validate Data**: Click **Validate Resume** to send your data to the backend. The API checks that no fields are empty and returns a success or failure message.
4.  **Get AI Feedback**: Click **✨ AI Feedback** to analyze your resume. The backend processes each project description and returns an overall score and a card for each project detailing its linguistic strength and providing suggestions for improvement.
5.  **Export Your Resume**:
    *   **Preview**: View an HTML-based preview in a modal.
    *   **Copy LaTeX**: Copy the generated code to your clipboard.
    *   **Download TEX**: Save the `resume.tex` file.
    *   **Download PDF**: Open a print dialog to save the resume as a PDF in a classic "Harvard-style" format.

## API Endpoints

The FastAPI backend exposes two main endpoints:

### `POST /resume`

Accepts a JSON payload with the user's resume data. It validates the data against the `ResumeInput` Pydantic schema, ensuring no lists or strings are empty.

-   **Success Response (200)**:
    ```json
    {
      "message": "Resume data validated and received successfully!",
      "received_data": { ... }
    }
    ```
-   **Error Response (422)**:
    ```json
    {
      "message": "Validation Error",
      "details": [
        "Validation failed for 'name': Field required"
      ]
    }
    ```

### `POST /analyze`

Accepts the same JSON payload. It uses the `distilbert-base-uncased-finetuned-sst-2-english` model to analyze each project description.

-   **Success Response (200)**:
    ```json
    {
        "score": 85,
        "analysis": [
            {
                "project": "Developed full-stack inventory management resolving 50% delay",
                "strength": "strong",
                "confidence": 0.99,
                "suggestion": "Great project description! It highlights positive impact effectively."
            },
            {
                "project": "I made a website",
                "strength": "weak",
                "confidence": 0.98,
                "suggestion": "Consider starting your description with stronger action verbs like: Developed, Engineered, Implemented, Optimized, or Designed."
            }
        ]
    }