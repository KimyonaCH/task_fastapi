FROM python:3.10-slim
LABEL authors="kimyona"

COPY task_fastapi/ /app
WORKDIR /app

RUN apt-get update -qy && \
    python3 -m pip install poetry && \
    poetry install

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]