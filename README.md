# prima-app-api

Python-based API server for managing user data

# Installation

1. Install the dependencies via PIP. (If you use virtualenv you'll want to
   create a virtual environment and activate it first.)

   Open a terminal and cd <project_directory>

   Run `python -m venv your_venv_name` # To Create a new virtual environment

   Run `source your_venv_name/bin/activate` # To Activate the virtual environment on (macOS/Linux)

   Run `your_venv_name\Scripts\activate` # To activate the virtual environment (Windows)

   Run `pip install -r requirements.txt` # Install project dependencies

   Optionally, RUN `pip install -r requirements-dev.txt` # Install project dev dependencies

# Start Server

Run `python manage.py runserver` # To start the development server.

The browser API Endpoint documentation is on `http://127.0.0.1:8000/api/docs/`

# API Endpoints

| #   | Request Method | Endpoint                                | Description                  | Param        | Example Request Body                                                                            | Response Format                 | Example Result                                                                         |
| --- | -------------- | --------------------------------------- | ---------------------------- | ------------ | ----------------------------------------------------------------------------------------------- | ------------------------------- | -------------------------------------------------------------------------------------- |
| 1   | GET            | `http://127.0.0.1:8000/api/users/`      | Retrieve all users           | None         | None                                                                                            | - HTTP status code: 200 OK      | `[ { "id": 0, "email": "user@example.com", "username": "string", "name": "string" } ]` |
| 2   | POST           | `http://127.0.0.1:8000/api/users/`      | Create a new user            | None         | `{ "email": "user@example.com", "username": "string", "password": "string", "name": "string" }` | - HTTP status code: 201 CREATED | `{ "id": 0, "email": "user@example.com", "username": "string", "name": "string" }`     |
| 3   | GET            | `http://127.0.0.1:8000/api/users/{id}/` | Retrieve a single user by ID | id (integer) | None                                                                                            | - HTTP status code: 200 OK      | `{ "id": 0, "email": "user@example.com", "username": "string", "name": "string" }`     |
| 4   | PATCH          | `http://127.0.0.1:8000/api/users/{id}/` | Update a user by ID          | id (integer) | `{ "email": "user@example.com", "username": "string", "password": "string", "name": "string" }` | - HTTP status code: 200 OK      | `{ "id": 0, "email": "user@example.com", "username": "string", "name": "string" }`     |
| 5   | DELETE         | `http://127.0.0.1:8000/api/users/{id}/` | Delete a user by ID          | id (integer) | None                                                                                            | - HTTP status code: 204         | No response body                                                                       |

# Dockerising The Application

1. The purpose and benefits of dockerising The application.

The three reasons I feel containers are so popular today and why containers themselves had to exist are:

- Isolation: Containers give our application a layout of isolation inside a single operating system, applications are isolated in their own containers, they get their own IP address, file system, process space. This allows many benefits, including running multiple versions of the same app on the same system without any conflit, saving us time, helps with dependency management, gives us the isolation we need to protect our applications.

- Environment: Containers minimize environmental variations, much like physical containers in the real world that allow us to ship goods all around the world, the people that deliver the physical containers didn't have to know what was inside it, and the people that put their stuff inside the container didn't have to know or care how the container physically got to its destination.The same thing is true of images and Docker containers now. Similar to the way physical containers abstract the contents they carry, Docker containers offer a standardized format known as OCI standards. These standards ensure consistency in running containers across different environments, guaranteeing that they operate with the same dependencies they were built with

- Speed: Containers and Docker give us an ability to develop faster, build apps faster, to test them faster and to deploy them faster, all because the container images and the containers themselves are so easy to build, redeploy and rerun. Containers give us the speed of change, not just for the software but also for the business that want to implement that software.

2. Docker Docker Compose Installation:

Ensure that you have Docker and Docker Compose installed on your development machine.

Follow the instructions based on your operating system to install Docker: [Install Docker](https://docs.docker.com/get-docker/)

Docker Compose is included with Docker Desktop. For separate installation : [Install Docker Compose](https://docs.docker.com/compose/install/)

3. Build the Docker Image and Start the Docker Containers:

   Open a terminal and cd <project_directory>

   Run `docker-compose build` # To build the docker image for the main app and the database service defined in the docker-compose file

   Run `docker-compose up` # To start the containers

4. Access API endpoints

   When the containers are up and running, you can access the API endpoints documentation on:

` http://127.0.0.1:8080/api/docs/`

5. Stopping the containers

   Run `docker-compose down` # To stop the containers

# Deployment Using Kubernetes (Minikube)

1. Benefits of Kubernetes for deployment.

The usage of Kubernetes for deployment offers multiple benefits across scaling and management of our application. Some of these benefits are:

- Kubernetes automates deployments, reducing errors that may arise from manual management.
- Containerization limits the impact of application failures on the entire system.
- Labels, annotations, health checks, and features like Horizontal Pod Autoscaling enhance application performance, manageability, and responsiveness to varying demands.
- Automation via Kubernetes reduces time and labour costs linked with manual deployment tasks.
- It supports the use of cloud-based services and container-based applications, which are more efficient and scalable.
  Kubernetes facilitates increased efficiency and productivity

2. Install Minikube
   Ensure that you have Docker and Docker Compose installed on your development machine.

Follow the instructions on the minikube official website to install Minikube. [Install Minikube](https://minikube.sigs.k8s.io/docs/start/)

Open a terminal and run the command `minikube start ` # to start minikube.

3. Build and load the Image locally

From the terminal, run the command `docker buildx build --no-cache  -t django-app:latest .` # This will build the docker image locally. Ensure the docker daemon is running

To load the image to minikube run this command `minikube image load django-app:latest `

4. Deploy Ap to Minikube

cd to the infra/k8s/ directory

Run these commands to deploy the manefests
`kubectl apply -f deployment.yaml
`
`kubectl apply -f services.yaml`
`kubectl apply -f storage.yaml`

To confirm the pod is running, run this commands `kubectl get pods` and `kubectl get services`.

5. Access the API Server

Ways you can access the API server:

- Run the command `minikube service <SERVICE_NAME>  --url` which will give you direct url to access application and access the url in web browser.

- If you are using a driver to run minikube, accessing the provided url from step one might not work. A way to get it working is to use port-forwarding.

  Run the command `kubectl port-forward <SERVICE_NAME> 8000:8000` and access the API server application on localhost:8000

Note: <SERVICE_NAME> is the name of the service. In this case it will be django-api-srvc

6. Clean up:

To delete the Kubernetes resources to free up resources and avoid conflicts:

- Run the command kubectl delete -f deployment.yaml # To delete the deployment

- Run the command kubectl delete -f services.yaml # To delete the services

- Run the command kubectl delete -f storage.yaml # To delete the storage
