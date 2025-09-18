from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from App.routes import voyage

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify ["http://localhost:3000"] for frontend only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(voyage.router)