# Deploying  a Flask Application


# Requirements:
- Install Vscode
- Install Docker Desktop on your machine
- Creating a Docker file for a Flask app.
- Building and running the Docker container.
- Accessing the Flask Application

# Intro
In this exploration of containers, I will be using Docker, the most widely adopted containerisation platform. Before proceeding, it is useful to understand what containers are. According to Docker, “A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application, including the code, runtime, system tools, libraries, and settings.”

Unlike traditional approaches that rely on separate virtual machines for each application, containers allow multiple applications to run on a single operating system. This approach significantly reduces resource usage and improves efficiency, as less processing power is spent maintaining multiple virtual machines and more can be dedicated to running applications.
![Docker](https://github.com/user-attachments/assets/5ca69e17-f03f-4b2e-b1c2-2a23faba59ff)




# Project structure
```
flask-app/
├── FlaskApplication//  # Build artifacts
│   └── templates/      # HTML templates
│       └── index.html  # Main page template
│   ├── app.py          # Flask application
│   ├── Dockerfile      # Docker build instructions
│   ├── requirements.txt # Python dependencies
│   ├── README.md       # README file

   
```


# Build our Docker image
From the command line and type the command docker build -t hello-flask-app.
This command "Docker build "starts the build process. Next, we have "-t hello-flask-app", where the -t option assigns a name to the image. In this instance, we are calling it hello-flask-app. Following this, we use a dot, which signifies the current directory and instructs Docker to search for the Dockerfile there. If we happened to be in another directory, we would replace the . with ./hello-flask, depending on our current location.

<b> docker build -t Hello-flask-app . </b>

# Run the container

<br><b>docker run -d -p 5003:5003 hello-flask-app</b></br>
<br>a3aaa766645785a29ea01a0f670841c06d3d8a6e316808d9bb503d4ec5f6b32a </br>
<br>The below commad shows  all containers running. In our case hello-flask-app is running </br>
<br><b>docker ps</b><br>
<br>CONTAINER ID   IMAGE             COMMAND           CREATED         STATUS         PORTS                                         NAMES</br>
a3aaa7666457   <b>hello-flask-app</b>   "python app.py"   6 seconds ago   Up 5 seconds   0.0.0.0:5003->5003/tcp, [::]:5003->5003/tcp   blissful_mendeleev

# Open in browser

Go to:

http://localhost:5003

You should see your HTML page.
<img width="1680" height="908" alt="image" src="https://github.com/user-attachments/assets/ba902505-9e07-4c03-b51f-c2917cf64d70" />


