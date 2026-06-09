from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "Traffic Monitoring API Running"
    }