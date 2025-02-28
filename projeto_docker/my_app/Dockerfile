FROM python:3.9

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar e instalar as dependências do projeto
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Definir as variáveis de ambiente para Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Comando para iniciar a aplicação Flask
CMD ["flask", "run"]
