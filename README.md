# project-backend

## How to run docker

1. Clone project:
```
git clone https://github.com/exerciseOne/project-backend.git
```

2. Run terminal in main folder of project and create docker image:
```
docker build --tag project-backend .
```

3. Run docker container
```
docker run -d -p 5000:5000 project-backend
```

4. Open localhost:5000 in browser:
[http://localhost:5000/](http://localhost:5000/)
