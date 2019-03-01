# DockerTest
Challenge to learn Docker

## Requirements:

High-level: Using automation we want to spin up an environment which will allow us to connect to a web server on port 80 or 8080 and serve a bit of simple HTML content from a data storage source. You will be required to write a small application in the language/framework of your choice to connect to the database, query it, and return the result to the user.

## Criteria:

·         Developed within a git repository with frequent commits

·         Automated way to spin up/down single machine environment (vagrant, docker compose, minikube etc)

·         OS installation/configuration (Windows or Linux, any versions)

·         Configuration management (Chef/Puppet/Ansible, Dockerfile or kube deployment files) to install and configure applications

·         Installation of a web tier and data tier (your choice, e.g. NGINX/Apache/IIS, MySQL/PostgreSQL/Redis/etc)

·         Running a simple web application to query and return data

## Plan of Action
1) I want to understand the requirements and the technology stack involved
  * Read and implement the Docker tutorial in the official page 
  https://docs.docker.com/get-started/part5/
  * I need to have a web app. I had some experience using Flask so is there any Flask with containers tutorial ?
  * I need a database. I had some experience using MySQL. Is there any mysql with containers tutorial?
  https://developer.ibm.com/tutorials/docker-dev-db/
2) Now that I have done tutorials and have a better understanding, what is the tech stack do I want to use ? 
  * Automated way to spin up/down single machine environment -> Docker
  * Configuration management -> Dockerfile
  * Web tier -> Flask
  * Data tier -> MySQL
  * Orchestration 
3) I want to start with a containerised mySQL data tier and implement it.
3) After having done the containersised data tier, I want to create the web tier using Flask deployed in a container.
