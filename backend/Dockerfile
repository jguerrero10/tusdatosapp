FROM python:3.12-slim

WORKDIR /app
COPY pyproject.toml poetry.lock ./

RUN apt-get update && apt-get install -y postgresql-client && apt-get clean

RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root --without dev

COPY . .

EXPOSE 8000


COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
CMD ["uvicorn", "main:app", "--host", "0.0.0", "--port", "8000", "--reload"]
