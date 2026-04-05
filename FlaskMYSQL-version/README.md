# Deploying Flask + MySQL Docker Application 
A containerised Flask web application that connects to MySQL and displays the running MySQL version in the browser.
---
## Prerequisites

Before you begin, make sure you have the following installed:
- [VS Code](https://code.visualstudio.com/)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- Creating a Docker file for a Flask app
- Creating a Docker compose  file for a Flask app
- Building and running the Docker container
- Accessing the Flask Application on the browser to display MYSQL version
---

## Project Structure
```
flask-app/
└── Flask_MYSQLversion/
├── templates/
│   └── index.html        # Main page — displays MySQL version
├── app.py                # Flask application entry point
├── Dockerfile            # Docker build instructions
├── docker-compose.yml    # Multi-container setup with MySQL
├── requirements.txt      # Python dependencies
└── README.md

   
```


# Build our Docker image and run container for both Flask and MYSQL

app.py file:\
<img width="1455" height="936" alt="image" src="https://github.com/user-attachments/assets/76d79cb7-da82-48f1-ad22-72c7c54e5bbd" />


Docker file :\
<img width="429" height="324" alt="image" src="https://github.com/user-attachments/assets/df374292-cdfb-4cdd-84a1-966db8811506" />

Make sure you create  network between Flask and MySQL \
<b>docker build -t sharif-hello-flask . </b>
<b>docker run --name sharif-hello-flask-container -p 5005:5005 sharif-hello-flask </b>


$ <b>docker run --name sharif-hello-flask-container -p 5005:5005 sharif-hello-flask </b>
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5005
 * Running on http://172.17.0.4:5005

 * Accessing  the browser on port 5005
<img width="1883" height="785" alt="image" src="https://github.com/user-attachments/assets/4c0af7c1-472e-4554-abdd-3c233829dfda" />

# Create Docker-compose yaml file
Docker Compose YAML file as a recipe that outlines all the components, or services, required for your application. Rather than starting each container individually, you compile everything into a single file.\

<img width="524" height="355" alt="image" src="https://github.com/user-attachments/assets/6fc8572c-f19d-485b-9304-3b490d303924" />

run docker-compose up --build 

# Open in browser

Go to:

http://localhost:5005

You should see your HTML page. From the screenshot below , we can see that MYsql return version <b> 5.7.44</b>
<img width="1790" height="845" alt="image" src="https://github.com/user-attachments/assets/967f2794-4c5e-4fbe-b488-f35a8d5f906a" />

