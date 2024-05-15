# CloudFreme Project

This project includes a Solara user interface that allows users to input their birth date details and a FastAPI backend server to process the data. 

## Requirements

- Python 3.9+
- FastAPI
- Uvicorn
- Requests
- Solara

## Installation

1. Clone the project:
    ```bash
    git clone https://github.com/ersinaksar/cloud-frame
    cd CloudFreme
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: .\venv\Scripts\activate
    pip install fastapi uvicorn requests solara
    ```

## Usage

### Start the FastAPI Server

Start the FastAPI server with the following command:

```bash
uvicorn main:app --reload --port 8000

docker-compose up --build