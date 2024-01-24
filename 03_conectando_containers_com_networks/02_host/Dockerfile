
FROM python:3

# atualizar todos os repositorios de pacote e instalar pacotes necessarios
RUN apt-get update -y && \ 
    apt-get install -y python3-pip python3-dev

WORKDIR /app

# framework / lib
RUN pip install Flask requests flask_mysqldb

# copiar tudo do diretorio atual (.) para o diretorio de trabalho (.)
COPY . .

EXPOSE 5000

# executar projeto pelo cmd
CMD ["python", "./app.py"]