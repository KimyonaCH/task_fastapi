FROM ubuntu:latest
LABEL authors="kimyona"

COPY . /app
WORKDIR /app

RUN apt-get update -qy
RUN apt-get install -qy python3 python3-pip
RUN python3 -m pip install poetry
RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]