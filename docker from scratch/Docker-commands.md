docker pull [imageName] --> pull an image from the registry
docker run  [imageName] --> Run containers
docker run -d  [imageName] --> Detached mode
docker start [containerName] --> start containers
docker ps --> list all the running containers
docker ps -a --> list running and stopped containers
docker stop [containerName] --> stop containers
docker kill [containerName] --> kill containers
docker image inspect [imageName] --> get image info 
docker info --> display information
docker version --> systems version
docker login --> login to registry 
docker run --memory="256m" ngnix 
docker run --cpus=".5" ngnix 
### Running a container 
* pull and run an ngnix server 
docker run --publish 80:80 --name webserver ngnix 
* list the running containers 
docker ps
* stop the container 
docker stop webserver 
* remove the container 
docker rm webserver 
### Docker attach shell 
* attach shell --->  docker run -it ngnix -- /bin/bash
* docker run -it ----> microsoft/powershell:nanoserver
### Docker Cli cheetsheet - cleaning up
* removes the stopped container --> docker rm [containerName]
* removes all the stopped containers --> docker rm $(docker ps -a -q)
* lists all the images --> docker images
* deletes all the images --> docker rmi [imageName]
* removes all images not in use by any containers --> docker system prune -a
# running a Ngnix container 
* Pulling and running a ngnix container
docker run -d -p 8080:80 --name webserver ngnix 
* list the containers
docker ps
* 


