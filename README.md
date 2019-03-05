# DockerTest
Challenge to learn Docker

## Project Requirements:

High-level: Using automation we want to spin up an environment which will allow us to connect to a web server on port 80 or 8080 and serve a bit of simple HTML content from a data storage source. You will be required to write a small application in the language/framework of your choice to connect to the database, query it, and return the result to the user.

## Criteria:

·         Developed within a git repository with frequent commits

·         Automated way to spin up/down single machine environment (vagrant, docker compose, minikube etc)

·         OS installation/configuration (Windows or Linux, any versions)

·         Configuration management (Chef/Puppet/Ansible, Dockerfile or kube deployment files) to install and configure applications

·         Installation of a web tier and data tier (your choice, e.g. NGINX/Apache/IIS, MySQL/PostgreSQL/Redis/etc)

·         Running a simple web application to query and return data

## Requirements to run this

### Docker-compose up for non load balanced
1) Please install docker.
https://hub.docker.com/editions/community/docker-ce-desktop-mac
2) Clone the github repo git clone https://github.com/andi23/DockerTest.git
3) Open terminal and cd to DockerTest/test/
4) run command " docker-compose up "
5) open a browser and hit "  http://localhost:8080/  "

### For a load balanced app
1) Please install docker.
https://hub.docker.com/editions/community/docker-ce-desktop-mac
2) Clone the github repo git clone https://github.com/andi23/DockerTest.git
3) Open terminal and cd to DockerTest/test/
4) run command " ./services.sh " 
 -if there is an error of "Permission denied" -> please run the command " chmod +x services.sh  " . This is to basically give permission to run the services.sh file.
5) Open a browser and hit " http://localhost:8080/  "

## Plan of Action
![Image of solution](https://github.com/andi23/DockerTest/blob/master/images/Solution.png)

1) I want to understand the requirements and the technology stack involved
  * Read and implement the Docker tutorial in the official page 
  https://docs.docker.com/get-started/part5/
  * I need to have a web app. I had some experience using Flask. Flask with containers?
  * I need a database. I had some experience using MySQL. MySQL with containers?
  https://developer.ibm.com/tutorials/docker-dev-db/
2) Now that I have done tutorials and have a better understanding, what is the tech stack do I want to use ? 
  * Automated way to spin up/down single machine environment -> Docker
  * Configuration management -> Dockerfile
  * Web tier -> Flask
  * Data tier -> MySQL
3) I want to start with a containerised mySQL data tier and implement it.
4) After having done the containerised data tier, I want to create the web tier using Flask deployed in a container.
5) After having made connected Flask web tier and the data tier, is there anything I can do ? In a separate git branch "services", I made the app load balanced by scaling the services. 

## Journey in developing
1) Begin with making the data tier. 2 ways to do this. Either from an existing SQL file with the database, table, thousands of rows of data like the ibm tut and then simply use docker-compose. Or simply create a new database, define the schema, add some data to the table. 
2) Having created the sql model, I used the docker-compose.yml file with just the sql model and then connected to it using `mysql -P 3306 --protocol=tcp -u root -p`  . SQL queries can then be used to verify the data present.
3) Now that the container for data model is working well, I started to build the web app using Flask. The web app will be able  to simply display the data in the mySQL database and is in a container.
4) The containers are able to connect from the docker-compose.yml in which the Flask app is linked to the databse.
5) Simply test out docker-compose up and then go to the link at http://0.0.0.0:8080/  to check results.

## Problems found
1) No experience in using containers so had to study for that.
2) Following the tutorial and absorbing the knowledge instead of blindly following was a fun challenge. The ibm tut and docker tut were very helpful.

## How to stop and remove the containers 
### Non- load balanced app
1) Stop the containers ->  docker container stop $(docker container ls -a -q) 
2) Remove the containers -> docker container rm $(docker container ls -a -q) 
3) Remove the images ->  docker image rm $(docker image ls -a -q)
4) Verify 
 -- Docker container: docker container ls  
 -- Docker image: docker image ls
### For load-balanced app
1) docker stack rm flaskMolly
2) docker swarm leave --force
3) docker swarm ls -> "This node is not a swarm manager ...."

