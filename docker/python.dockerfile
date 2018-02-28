FROM python:3.6.4
ENV PYTHONUNBUFFERED 1
LABEL Author "Diemesleno Souza Carvalho"
RUN mkdir /var/www
COPY . /var/www
WORKDIR /var/www
EXPOSE 8000
RUN pip install -r requeriments.txt