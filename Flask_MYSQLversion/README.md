# Deploying  a Flask Application that intergrate with Mysql returning Mysql version


# Requirements:
- Install Vscode
- Install Docker Desktop on your machine
- Creating a Docker file for a Flask app
- Creating a Docker compose  file for a Flask app
- Building and running the Docker container
- Accessing the Flask Application on the browser to display MYSQL version

# Intro




# Project structure
```
flask-app/
├── Flask_MYSQLversion//  ~ This folder for Flask and Mysql 
│   └── templates/      # HTML templates
│       └── index.html  # Main page template that returns MYSQL version
│   ├── app.py          # Flask application
│   ├── Dockerfile      # Docker build instructions
│   ├── Docker-compose.yml      # Docker compose yaml build instructions
│   ├── requirements.txt # Python dependencies
│   ├── README.md       # README file

   
```


# Build our Docker image and run the container
app.py file:
<img width="685" height="465" alt="image" src="https://github.com/user-attachments/assets/df77f093-236b-410b-8e82-f8ff34b7bf3f" />
Docker file :
<img width="429" height="324" alt="image" src="https://github.com/user-attachments/assets/df374292-cdfb-4cdd-84a1-966db8811506" />

docker build -t sharif-hello-flask .
docker run --name sharif-hello-flask-container -p 5005:5005 sharif-hello-flask


$ docker run --name sharif-hello-flask-container -p 5005:5005 sharif-hello-flask
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5005
 * Running on http://172.17.0.4:5005

 * Accessing  the browser on port 5005
<img width="1883" height="785" alt="image" src="https://github.com/user-attachments/assets/4c0af7c1-472e-4554-abdd-3c233829dfda" />

# Create Docker-compose yaml file
Docker Compose YAML file as a recipe that outlines all the components, or services, required for your application. Rather than starting each container individually, you compile everything into a single file.
<img width="524" height="355" alt="image" src="https://github.com/user-attachments/assets/6fc8572c-f19d-485b-9304-3b490d303924" />


# Open in browser

Go to:

http://localhost:5005

You should see your HTML page.
<img width="1883" height="785" alt="image" src="https://github.com/user-attachments/assets/47b1cb1d-4f65-4338-ade6-fbcd5b740cbe" />
