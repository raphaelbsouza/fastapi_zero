# fastapi_zero/app.py
from http import HTTPStatus
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi_zero.schemas import Message

app = FastAPI(
    title='FastAPI@Zero', 
    version='0.1.0'
    )


@app.get('/api', response_class=HTMLResponse)

def read_root():
    return """
    <html>
    <head>
        <title>FastAPI@Zero</title>
    </head>
    <h1>Olá mundox!</h1>    
    </html>
    """
