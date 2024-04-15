# Python-flask-rest-api-project-using-helm

## 1. Build Docker image 
```commandline
docker build -t python-project .
```

## 2. Run Docker image
```commandline
docker run -p 9001:9001 python-project
```

## 3. Build & tag according to dockerhub
'''
docker tag python-project tagoregelli/python-flask-rest-api-project-using-helm:python-project
'''

## 4. Docker push
'''
docker push tagoregelli/python-flask-rest-api-project-using-helm:python-project
'''

## 5. Docker pull

