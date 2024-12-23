# Modelo + API: Prever Distância pelo Consumo de Gasolina

---

## Tecnologias Utilizadas

### Linguagem de Programação

- [Python](https://www.python.org/) (v3.11.0)

### Gerenciadores de Ambiente Virtual

- [Pyenv](https://github.com/pyenv/pyenv)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

### Principais Bibliotecas (Packages)

- [scikit-learn](https://scikit-learn.org/stable/)
- [scipy](https://scipy.org/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [seaborn](https://seaborn.pydata.org/)
- [matplotlib](https://matplotlib.org/)
- [statsmodels](https://www.statsmodels.org/stable/index.html)
- [pingouin](https://pingouin-stats.org/)
- [uvicorn](https://www.uvicorn.org/)
- [joblib](https://joblib.readthedocs.io/en/latest/)
- [fastapi](https://fastapi.tiangolo.com/)
- [pydantic](https://docs.pydantic.dev/)

### APIs

- **FastAPI**: Framework para criação e exposição de APIs.
- **Uvicorn**: Servidor ASGI utilizado para rodar a API.

---

## Visão Geral do Projeto

Este projeto consiste na criação de um modelo de predição para estimar a distância percorrida com base no consumo de gasolina e sua integração com uma API para realizar predições de forma prática e interativa.

No processo, foram explorados os dados com gráficos como dispersão, histogramas, boxplots e correlações (Pearson e Spearman). O modelo foi treinado e testado com uma divisão de 70% para treinamento e 30% para teste, avaliando seu desempenho com métricas como RMSE e análise de resíduos.

Também foram aplicadas validações adicionais, como análise de linearidade, homogeneidade das variâncias, e testes de normalidade (Shapiro-Wilk e Kolmogorov-Smirnov). Por fim, o projeto inclui uma API desenvolvida com FastAPI, permitindo interações dinâmicas para realizar predições.

---

## Como Executar o Projeto

**Pré-requisitos**:
- Certifique-se de que o **Python** esteja instalado em sua máquina. Caso contrário, baixe em [python.org](https://www.python.org/downloads/).

**Instalando o Projeto**:

1. Clone o repositório:
    ```bash
    git clone https://github.com/GianDutra/modelo_regressao_combustivel_distancia.git
    cd ModeloDistanciaGasolina
    ```

2. Configure o ambiente virtual com `pipenv`:
    ```bash
    pipenv install
    pipenv shell
    ```

3. Execute a API:
    ```bash
    uvicorn api_model_rl_simples_regressao_combustivel_distancia:app --reload
    ```

4. Acesse a API pelo navegador ou por ferramentas como Postman em:
    ```
    http://127.0.0.1:8000/docs
    ```

---

## Funcionalidades Implementadas

### Modelo de Machine Learning
- Criação de um modelo para prever a distância percorrida com base no consumo de gasolina.
- Avaliação com métricas como RMSE e análise gráfica dos valores reais e preditos.

### Exploração de Dados
- Gráficos de dispersão, boxplots, histogramas, correlações (Pearson e Spearman).
- Análise de resíduos para validar linearidade, homogeneidade das variâncias e normalidade.
- Testes estatísticos de Shapiro-Wilk e Kolmogorov-Smirnov.

### API com FastAPI
- Permite interagir com o modelo para realizar predições com base nos dados inseridos.
- Interface interativa com documentação gerada automaticamente.

---

## 👨‍💼 Autor

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://github.com/GianDutra.png" width="100px;" alt="Foto do Gian no GitHub"/><br>
        <sub>
          <b>Gian Dutra</b>
        </sub>
      </a>
    </td>
  </tr>
</table>
