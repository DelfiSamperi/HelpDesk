from fastapi import FastAPI

from app.routes.tickets import router as tickets_router
from app.routes.comments import router as comments_router
from app.routes.auth import router as users_auth_router
app = FastAPI()

app.include_router(tickets_router)
app.include_router(comments_router)
app.include_router(users_auth_router)

@app.get('/')
def root():
    return {'message': 'API funcionando'}

