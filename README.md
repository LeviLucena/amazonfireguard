<p align="center">

  <!-- Linguagem principal -->
  <a href="https://www.python.org/">
    <img src="https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  </a>

  <!-- Frameworks Web -->
  <a href="https://flask.palletsprojects.com/">
    <img src="https://img.shields.io/badge/-Flask-000000?style=flat-square&logo=flask&logoColor=white" alt="Flask" />
  </a>
  <a href="https://dash.plotly.com/">
    <img src="https://img.shields.io/badge/-Dash-1E1E1E?style=flat-square&logo=plotly&logoColor=white" alt="Dash" />
  </a>

  <!-- APIs Meteorológicas e de Incêndios -->
  <a href="https://earthdata.nasa.gov/firms">
    <img src="https://img.shields.io/badge/-NASA%20FIRMS-E74C3C?style=flat-square&logo=nasa&logoColor=white" alt="NASA FIRMS" />
  </a>
  <a href="http://queimadas.dgi.inpe.br/queimadas/">
    <img src="https://img.shields.io/badge/-INPE%20Queimadas-00A859?style=flat-square&logo=google-earth&logoColor=white" alt="INPE" />
  </a>
  <a href="https://content.meteoblue.com/en/access/weather-apis">
    <img src="https://img.shields.io/badge/-Meteoblue-0082C8?style=flat-square&logo=cloud&logoColor=white" alt="Meteoblue API" />
  </a>
  <a href="https://openweathermap.org/api">
    <img src="https://img.shields.io/badge/-OpenWeatherMap-EA7600?style=flat-square&logo=openweathermap&logoColor=white" alt="OpenWeatherMap" />
  </a>

  <!-- Visualização Geoespacial -->
  <a href="https://leafletjs.com/">
    <img src="https://img.shields.io/badge/-Leaflet-199900?style=flat-square&logo=leaflet&logoColor=white" alt="Leaflet.js" />
  </a>
  <a href="https://www.openstreetmap.org/">
    <img src="https://img.shields.io/badge/-OpenStreetMap-7EBC6F?style=flat-square&logo=openstreetmap&logoColor=white" alt="OpenStreetMap" />
  </a>
  <a href="https://postgis.net/">
    <img src="https://img.shields.io/badge/-PostGIS-4183C4?style=flat-square&logo=postgresql&logoColor=white" alt="PostGIS" />
  </a>

  <!-- Machine Learning e Processamento -->
  <a href="https://scikit-learn.org/">
    <img src="https://img.shields.io/badge/-Scikit--Learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white" alt="Scikit-learn" />
  </a>
  <a href="https://pandas.pydata.org/">
    <img src="https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white" alt="Pandas" />
  </a>
  <a href="https://numpy.org/">
    <img src="https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white" alt="NumPy" />
  </a>
  <a href="https://matplotlib.org/">
    <img src="https://img.shields.io/badge/-Matplotlib-0080CD?style=flat-square&logo=python&logoColor=white" alt="Matplotlib" />
  </a>
  <a href="https://seaborn.pydata.org/">
    <img src="https://img.shields.io/badge/-Seaborn-2E77BC?style=flat-square&logo=python&logoColor=white" alt="Seaborn" />
  </a>

  <!-- Banco de Dados -->
  <a href="https://www.postgresql.org/">
    <img src="https://img.shields.io/badge/-PostgreSQL-336791?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  </a>
  <a href="https://www.sqlalchemy.org/">
    <img src="https://img.shields.io/badge/-SQLAlchemy-D71F00?style=flat-square&logo=python&logoColor=white" alt="SQLAlchemy" />
  </a>

  <!-- Manipulação de Dados / HTTP -->
  <a href="https://requests.readthedocs.io/">
    <img src="https://img.shields.io/badge/-Requests-20232A?style=flat-square&logo=python&logoColor=white" alt="Requests" />
  </a>

  <!-- Containerização -->
  <a href="https://www.docker.com/">
    <img src="https://img.shields.io/badge/-Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  </a>
  <a href="https://docs.docker.com/compose/">
    <img src="https://img.shields.io/badge/-Docker%20Compose-3855D6?style=flat-square&logo=docker&logoColor=white" alt="Docker Compose" />
  </a>

  <!-- Variáveis de Ambiente -->
  <a href="https://pypi.org/project/python-dotenv/">
    <img src="https://img.shields.io/badge/-Dotenv-ECD53F?style=flat-square&logo=python&logoColor=black" alt="Dotenv" />
  </a>

  <!-- Licença e Status -->
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square" alt="Status" />
  <img src="https://img.shields.io/badge/license-MIT-blue?style=flat-square" alt="MIT License" />

</p>


![Gemini_Generated_Image_vbzw2uvbzw2uvbzw111](https://github.com/user-attachments/assets/682ad99c-a522-48be-ac5c-90e2eef3162d)

---
# 🔥 Monitoramento de Queimadas na Amazônia
Este projeto AmazonFireGuard é uma plataforma inteligente para monitoramento de queimadas na Amazônia (e globalmente), integrando dados em tempo real de satélites, fontes meteorológicas e modelos de inteligência artificial para visualização, análise e resposta rápida com pontos de calor detectados por sensores térmicos.

## 🌟 Destaques

🛰️ **Dados direto da NASA/INPE** - Atualização automática a cada 5 minutos  
🌎 **Cobertura global** com foco especial na Amazônia brasileira  
📊 **Visualização interativa** com múltiplas camadas de informação  
🔮 **Previsão de risco** usando modelos de machine learning (em desenvolvimento)  
🐳 **Pronto para produção** com infraestrutura containerizada (Docker)

## 🚀 Funcionalidades Principais

### 🗺️ Visualização Geoespacial
- Mapa interativo com biblioteca Leaflet.js
- Camadas base: 
  - 🛰️ Satélite (Esri World Imagery)
  - 🗺️ OpenStreetMap
  - ⚫ Stamen Toner (preto e branco)
- 📌 Marcadores coloridos por intensidade térmica
- 🔍 Zoom para região amazônica ou visão global

### 📡 Dados em Tempo Real
- Atualização automática a cada minuto
- Exibição de:
  - 📅 Data/hora do registro
  - 🌡️ Temperatura (banda TI4)
  - ✔️ Nível de confiança (0-100%)

### 📊 Ferramentas de Análise
- 🎚️ Filtros por data e região (em desenvolvimento)
- 📈 Gráficos temporais (em desenvolvimento)
- � Overlay com dados meteorológicos
---

## 🧪 Exemplo de Uso
https://github.com/user-attachments/assets/9628404a-a96b-4052-b95c-38743de3b45e


## 🔧 Tecnologias e Bibliotecas

### Frontend
- **HTML5 + CSS3 + JavaScript**
- **[Leaflet.js](https://leafletjs.com/)** - biblioteca de mapas interativos.
- Camadas de mapa:
  - [Esri World Imagery](https://server.arcgisonline.com)
  - [OpenStreetMap](https://www.openstreetmap.org/)
  - [Stamen Toner](https://stamen.com/)

### Backend
- Python + Flask — API RESTful
- SQLAlchemy + SQLite/PostGIS — Banco de dados relacional e geoespacial
- YOLO (Ultralytics) — Detecção de assinaturas ou queimadas por imagens (visão computacional) (Em Desenvolvimento)
- Dash / Streamlit — Frontend interativo 

---

## 📡 APIs de Fontes de Dados

| Fonte | Descrição | Frequência |
|-------|-----------|------------|
| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/) | Dados de focos de calor via satélite | 5 minutos |
| [INPE Queimadas](http://queimadas.dgi.inpe.br/) | Dados regionais do Brasil | Diária |
| [Meteoblue](https://www.meteoblue.com/) | Dados meteorológicos | Horária |

---  

## 🗂 Estrutura do Projeto
```bash
amazonfireguard/
├── app/
│   ├── api/                # Rotas e endpoints da API Flask
│   ├── services/           # Integrações com APIs externas (NASA FIRMS, INPE, etc.)
│   ├── ml/                 # Modelos de IA/ML para previsão e análise
│   ├── maps/               # Utilitários de mapa
│   ├── database/           # Modelos e conexão com banco (SQLite + SQLAlchemy + PostGIS)
│   ├── templates/          # Templates HTML (ex: index.html)
│   └── utils/              # Funções auxiliares geoespaciais e diversas
├── frontend/               # Interface interativa (Dash ou Streamlit)
│   ├── dashboard.py        # Mapa, gráficos, interação
│   └── assets/             # Estilos, imagens, fontes
├── etl/                    # Scripts para extração e pré-processamento
├── notebooks/              # Análises exploratórias e experimentos com ML
├── tests/                  # Testes automatizados da API e serviços
├── data/                   # Dados temporários e arquivos CSV
├── .env                    # Variáveis de ambiente (chaves API, DB)
├── Dockerfile              # Docker para backend e frontend
├── docker-compose.yml      # Orquestração de contêineres
├── requirements.txt        # Dependências Python
└── run.py                  # Inicialização principal da aplicação

```
---  

## 🚀 Como executar localmente

### 1. Clonar o repositório
```bash
git clone https://github.com/LeviLucena/amazonfireguard.git
cd monitoramento-queimadas
```

### 2. Criar ambiente Python (opcional)
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instalar dependências
```bash
cd amazonfireguard
pip install -r requirements.txt
```

### 4. Executar o servidor backend
```bash
python run.py
```
Acesse o frontend em: http://localhost:5000

## 🛠️ Melhorias Futuras
Upload de shapefiles para sobrepor limites territoriais (ex: terras indígenas, unidades de conservação).

- Filtros por data, estado ou intensidade.
- Exportar visualizações como imagem ou PDF.
- Histórico temporal (animação de queimadas por dia).
- Notificações via e-mail ou Telegram sobre novos focos críticos.

## 📚 Referências
- NASA FIRMS API: https://earthdata.nasa.gov/firms
- INPE Queimadas: http://queimadas.dgi.inpe.br/queimadas/
- Meteoblue Weather API: https://content.meteoblue.com/en/access/weather-apis
- OpenWeatherMap API: https://openweathermap.org/api
- Leaflet.js: https://leafletjs.com/
- Esri World Imagery: https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/
- OpenStreetMap: https://www.openstreetmap.org/
- Stamen Map Tiles: https://stamen.com/

- ## 🤝 Como Contribuir
Sinta-se à vontade para contribuir, sugerir melhorias ou relatar problemas para ajudar a desenvolver este projeto.

## 📄 Licença
Este projeto está licenciado sob a licença MIT — veja [LICENSE](https://github.com/github/gitignore/blob/main/LICENSE) para detalhes.
