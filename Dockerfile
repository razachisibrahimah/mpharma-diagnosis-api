FROM python:3.9.1-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app

COPY requirements.txt start-server.sh /app/
COPY src /app/diagnosis_api/

WORKDIR /app

RUN pip install -r requirements.txt
RUN chmod +x start-server.sh
RUN chown -R www-data:www-data /app

VOLUME ["/app"]

# start server
EXPOSE 8010
CMD ["/app/start-server.sh"]
