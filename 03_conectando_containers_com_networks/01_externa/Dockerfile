
FROM python:3

# atualizar todos os repositorios de pacote e instalar pacotes necessarios
RUN apt-get update -y && \ 
    apt-get install -y python3-pip python3-dev

WORKDIR /app

# framework
RUN pip install Flask

# lib
RUN pip install requests

# copiar tudo do diretorio atual (.) para o diretorio de trabalho (.)
COPY . .

EXPOSE 5000

# executar projeto pelo cmd
CMD ["python", "./app.py"]