from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "GitHub FastAPI Pod Test OK"}

@app.get("/health")
def health():
    return {"status": "healthy"}
