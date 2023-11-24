# Instalation guide


### Github (3 steps)
If you prefer to use github, then
- clone git repository
```
git clone https://github.com/KimyonaCH/task_fastapi.git
```
- build docker image (make sure that you have a docker)
```
docker build -t task_fastapi_from_kimyona:latest -f task_fastapi/Dockerfile .
```
- run docker
```
docker run -d -p 8000:8000 task_fastapi_from_kimyona
```
The server successfuly started, to check it open [http://0.0.0.0:8000](http://0.0.0.0:8000).

### DockerHub (2 steps)
To download image from dockerhub, execute:
```
docker pull kimyonavl/task_fastapi:latest
```
and run docker
```
docker run -d -p 8000:8000 kimyonavl/task_fastapi
```
