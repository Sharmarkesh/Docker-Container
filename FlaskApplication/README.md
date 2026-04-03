# Deploying  a Flask Application


# Requirements:
- Install Vscode
- Install Docker Desktop on your machine
-Creating a Docker file for a Flask app.
-Building and running the Docker container.
-Best practices for deploying Flask applications using Docker.

#Intro
In this exploration of containers, I will be using Docker, the most widely adopted containerisation platform. Before proceeding, it is useful to understand what containers are. According to Docker, “A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application, including the code, runtime, system tools, libraries, and settings.”

Unlike traditional approaches that rely on separate virtual machines for each application, containers allow multiple applications to run on a single operating system. This approach significantly reduces resource usage and improves efficiency, as less processing power is spent maintaining multiple virtual machines and more can be dedicated to running applications.

1. Project structure
flask-app/
│
├──FlaskApplication
   ├── app.py
   ├── requirements.txt
   ├── templates/
   │   └── index.html
   └── Dockerfile


# Build our Docker image
From the command line and type the command docker build -t hello-flask-app
This command "Docker build "starts the build process. Next, we have "-t hello-flask-app", where the -t option assigns a name to the image. In this instance, we are calling it hello-flask-app. Following this, we use a dot, which signifies the current directory and instructs Docker to search for the Dockerfile there. If we happened to be in another directory, we would replace the . with ./hello-flask, depending on our current location.

docker build -t Hello-flask-app .

# Run the container
docker run -p 5000:5000 flask-html-app
docker run -d -p 5003:5003 hello-flask-app
a3aaa766645785a29ea01a0f670841c06d3d8a6e316808d9bb503d4ec5f6b32a

docker ps
CONTAINER ID   IMAGE             COMMAND           CREATED         STATUS         PORTS                                         NAMES
a3aaa7666457   hello-flask-app   "python app.py"   6 seconds ago   Up 5 seconds   0.0.0.0:5003->5003/tcp, [::]:5003->5003/tcp   blissful_mendeleev

# Open in browser

Go to:

http://localhost:5003

You should see your HTML page.
