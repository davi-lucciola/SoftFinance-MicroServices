FROM python:3.11

COPY . ./

WORKDIR /app

RUN pip install --upgrade pip && \
    pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "uvicorn", "main:api_auth", "--host", "0.0.0.0", "--port", "9000"]