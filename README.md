# API-HEALTH-E-ME-

# API em FastAPI

# Endpoints

- `/health` → Verifica se a API está funcionando.  
- `/me` → Retorna informações pessoais.

# Como rodar localmente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/meu_projeto_api.git
   cd meu_projeto_api
2. Crie um ambiente virtual e instale as dependências:

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt

3. Rode a aplicação:

uvicorn main:app --reload

4. Acesse no navegador:

http://127.0.0.1:8000/health

http://127.0.0.1:8000/me

Documentação: http://127.0.0.1:8000/docs

5. # API online no Render

6. 1. Crie uma conta no [Render](https://render.com/).
2. Clique em **New + → Web Service**.
3. Conecte seu repositório público do GitHub.
4. Configure:
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port 10000`
5. Deploy e pegue a URL pública para colocar no README.
