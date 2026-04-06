# Deploying  a Flask Application + Redis Visit Counter and Scalability with Docker


# Requirements:
- Install Vscode
- Install Docker Desktop on your machine
- Creating a Docker file for a Flask app and Redis
- Creating a Docker compose  file for a Flask app and Redis
- Building and running the Docker container
- Accessing the Flask Application on the browser to display MYSQL version

  <img width="506" height="502" alt="image" src="https://github.com/user-attachments/assets/37396f4e-a092-4d43-b9d3-ad5b3c1cdbef" />


# Introduction

This project uses two HTML templates that work together to create a simple visit tracking app.

<b>home.html — The landing page</b>
This is the first page the user sees when they visit the app at http://localhost:5001. It has no dynamic content — it is pure static HTML. Its only job is to welcome the user and provide a "View visit count" button that links to /count.
When the button is clicked, the browser sends a GET request to the /count route in Flask.

<b>visits.html — The counter page</b>
This is where the magic happens. When Flask receives a request on /count, it calls r.incr('visits') which tells Redis to increment the visits key by 1 and return the new value. Flask then passes that number to visits.html like this:

Splitting the welcome page and the counter page keeps responsibilities clean. home.html is static and loads instantly with no Redis dependency. visits.html is dynamic and only hits Redis when actually needed. If Redis is down, only the /count route breaks — the home page still loads fine.Every time the user refreshes the page or clicks the button again, the counter goes up by 1.



# Project structure
```
flask-app/
├── Flask_MYSQLversion//  ~ This folder for Flask and Mysql 
│   └── templates/      # HTML templates
│       └── home.html  # Main page template that returns MYSQL version
│       └── about.html  # Main page template that returns MYSQL version
│       └── visits.html  # Main page template that returns MYSQL version
│   ├── app.py          # Flask application
│   ├── Dockerfile      # Docker build instructions
│   ├── Docker-compose.yml      # Docker compose yaml build instructions
│   ├── requirements.txt # Python dependencies
│   ├── README.md       # README file

   
```

# Flow of Diagram:

<img width="1453" height="464" alt="image" src="https://github.com/user-attachments/assets/aa560f4e-071b-475d-97f9-5a2d78071325" />

 # Full request flow:
<img width="925" height="685" alt="image" src="https://github.com/user-attachments/assets/fad1df12-6a06-403b-a98f-05e807b4e2da" />




# Build our Docker image and run the container
<b>count.py file:</b>\

<img width="451" height="466" alt="image" src="https://github.com/user-attachments/assets/ce804c9b-f087-4ceb-b779-24dbd8e6a08b" />


<b>Docker file :</b>\

<img width="543" height="331" alt="image" src="https://github.com/user-attachments/assets/776b7005-b353-4708-988a-479b7ee8f030" />








# Create Docker-compose yaml file
<b>Docker-compose.yml:</b>\

<img width="618" height="665" alt="image" src="https://github.com/user-attachments/assets/ac6bbf67-24f2-4654-b214-0c17ba486549" />



# Open in browser

Go to:

http://localhost:5001

<b>This is the first page the user sees when they visit the app at http://localhost:5001</b>


<img width="1201" height="708" alt="image" src="https://github.com/user-attachments/assets/1ff58184-988a-4817-b447-0cc162620906" />


<b>This is the about page if user clicks about button</b>

<img width="1200" height="733" alt="image" src="https://github.com/user-attachments/assets/595214e2-796d-4fad-a0e2-e201dab241ca" />


<b>This is  count visists page  where user can see the number of times the home page was visisted</b>

<img width="1542" height="777" alt="image" src="https://github.com/user-attachments/assets/808f1478-4a58-4fe9-924b-7a2c1a9ba92a" />

<img width="1651" height="755" alt="image" src="https://github.com/user-attachments/assets/fceb3a73-9b65-4746-ac77-6f38f5784516" />

<img width="1550" height="784" alt="image" src="https://github.com/user-attachments/assets/9fca4de9-4a85-4d6c-8beb-3f4aa58ecb53" />






<img width="922" height="348" alt="image" src="https://github.com/user-attachments/assets/ddf097c2-ab1b-414c-a032-bd70078fd652" />


# Scaling the Flask service

Previously, the Flask web application was configured to run on a single instance. In a production environment, however, it is often necessary to scale services horizontally to handle increased traffic and ensure high availability.
In this implementation, the application has been scaled to three instances. The port configuration has been updated from a fixed port mapping to expose: 5001, allowing all three instances to communicate internally on port 5001 without conflicts. Since exposed ports are not directly accessible externally, a load balancer is required to sit in front of the instances and distribute incoming traffic evenly across all three Flask replicas.

<b> Web-1 flask instance</b>

<img width="947" height="510" alt="image" src="https://github.com/user-attachments/assets/b5190fa6-a600-4706-a23b-ea5f64763dac" />

<b> Nginx Load Balancer </b>

<img width="577" height="340" alt="image" src="https://github.com/user-attachments/assets/be73251c-96d0-4a3c-ba02-b5f9796d45d3" />

With this command <b> docker-compose up --scale web=3 --build </b> . We can scale up our flask app to 3 instances as shown from the screenshot below.

<img width="950" height="667" alt="image" src="https://github.com/user-attachments/assets/0ce43fd4-9490-4a5f-90a5-1940b3dce6d6" />








