from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from src.core.config import init_db
from src.core.auth import verificar_password, crear_token, USERS
from src.api.routes import router

app = FastAPI(title="HRD - Home Router Daemon", version="0.1.0")

@app.on_event("startup")
def startup():
    init_db()

@app.post("/token")
def login(form: OAuth2PasswordRequestForm = Depends()):
    user = USERS.get(form.username)
    if not user or not verificar_password(form.password, user["password"]):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    token = crear_token({"sub": form.username})
    return {"access_token": token, "token_type": "bearer"}

app.include_router(router)

@app.get("/")
def root():
    return {"message": "HRD funcionando", "version": "0.1.0"}

@app.get("/health")
def health():
    return {"status": "ok"}