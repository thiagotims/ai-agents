from fastapi import FastAPI, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

# Permite que seu frontend (HTML) acesse este backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # pode restringir depois se quiser
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analisar_ameacas/")
async def analisar_ameacas(
    imagem: UploadFile,
    tipo_aplicacao: str = Form(...),
    autenticacao: str = Form(...),
    acesso_internet: str = Form(...),
    dados_sensiveis: str = Form(...),
    descricao_aplicacao: str = Form(...)
):
    """
    Endpoint falso para responder ao formulário.
    No real, aqui você faria análise de segurança.
    """
    resultado = f"""
    📌 Aplicação: {tipo_aplicacao}
    🔑 Autenticação: {autenticacao}
    🌍 Exposição na Internet: {acesso_internet}
    🔒 Dados Sensíveis: {dados_sensiveis}
    📝 Descrição: {descricao_aplicacao}

    ✅ Análise simulada concluída com sucesso.
    """
    return JSONResponse(content={
        "choices": [
            {"message": {"content": resultado.strip()}}
        ]
    })


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)

