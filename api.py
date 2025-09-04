from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok", "message": "API está funcionando!"}

@app.get("/me")
def me():
    return {
        "nome": "Seu Nome",
        "email": "email@exemplo.com",
        "curso": "Curso",
        "github": "https://github.com/seuusuario",
        "cidade": "Cidade",
        "interesses": ["Tecnologia", "Lazer", "Musica" "Programação", "Estudos"]
    }
