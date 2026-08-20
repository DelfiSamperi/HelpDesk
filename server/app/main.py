from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.tickets import router as tickets_router
from app.routes.comments import router as comments_router
from app.routes.auth import router as users_auth_router
from app.routes.users import router as users_router

app = FastAPI(
    title="HelpDesk API",
    description="""
    Ticket management system with:

    - JWT Authentication
    - Role based access control
    - Ticket History
    - Comments
    - Pagination
    """,
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tickets_router)
app.include_router(comments_router)
app.include_router(users_auth_router)
app.include_router(users_router)

@app.get('/')
def root():
    return {'message': 'API funcionando'}

