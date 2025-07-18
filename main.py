from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    query = data.get("query", "")
    result = run_agent(query)
    return {"response": result}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
