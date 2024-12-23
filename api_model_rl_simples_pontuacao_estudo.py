"""Criar API com modelo de predição 
"""


from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import joblib

# Criar uma instância do FastAPI
app = FastAPI()


class RequestBody(BaseModel):
    """Criar uma classe que irá agregar todos os request body para a API

    Properties:
        litros_utilizados: float
    """

    litros_utilizados: float


# Carregar o modelo para realizar o modelo de predição
modelo_distancia = joblib.load("./modelo_regressao_combustivel_distancia.plk")

@app.post('/predict')
def predict(data: RequestBody):
    """Preparar dados para realização da predição

    Args:
        data (RequestBody):
    """
    input_feature = [[data.litros_utilizados]]

    # realizar a predição
    y_pred = modelo_distancia.predict(input_feature)[0].astype(int)

    return {"distancia_percorrida_em_km": y_pred.tolist()}