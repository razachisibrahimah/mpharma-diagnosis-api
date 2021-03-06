FROM python:3.9.1-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app

COPY requirements.txt /app/
COPY src /app/diagnosis_api/

WORKDIR /app

RUN pip install -r requirements.txt
RUN chown -R www-data:www-data /app

VOLUME ["/app"]

EXPOSE 8010

# start server
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
