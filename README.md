# Python + Docker Swarm Color Translation App

## Build the App

- git pull https://github.com/rlcosta177/docker-swarm-translate.git
- docker build -t rlcosta121/translation-app .
- docker service create --name translation-app --replicas 3 --publish published=80,target=5000 rlcosta121/translation-app 

## Create/Update Docker Service & Push to Docker Hub

- docker build -t rlcosta121/translation-app .
- docker push rlcosta121/translation-app
- docker service create --name translation-app --replicas 3 --publish published=80,target=5000 rlcosta121/translation-app 
OR
- docker service update --image rlcosta121/translation-app translation-app 

## Using the App

Using the terminal:
- curl "http://localhost/translate?color=red&from=english&to=portuguese"

On a browser:
- http://localhost/translate?color=red&from=english&to=portuguese
