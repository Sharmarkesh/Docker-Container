# Deploying  a Flask Application + Redis Visit Counter


# Requirements:
- Install Vscode
- Install Docker Desktop on your machine
- Creating a Docker file for a Flask app
- Creating a Docker compose  file for a Flask app
- Building and running the Docker container
- Accessing the Flask Application on the browser to display MYSQL version

# Intro

This project uses two HTML templates that work together to create a simple visit tracking app.

home.html — the landing page
This is the first page the user sees when they visit the app at http://localhost:5001. It has no dynamic content — it is pure static HTML. Its only job is to welcome the user and provide a "View visit count" button that links to /count.
When the button is clicked, the browser sends a GET request to the /count route in Flask.

visits.html — the counter page
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


# Build our Docker image and run the container
count.py file:
<img width="451" height="466" alt="image" src="https://github.com/user-attachments/assets/ce804c9b-f087-4ceb-b779-24dbd8e6a08b" />


Docker file :
<img width="273" height="156" alt="image" src="https://github.com/user-attachments/assets/c8ebd1bf-9d66-4268-af88-c3ebf71b789e" />







# Create Docker-compose yaml file
<img width="618" height="665" alt="image" src="https://github.com/user-attachments/assets/ac6bbf67-24f2-4654-b214-0c17ba486549" />



# Open in browser

Go to:

http://localhost:5001



http://localhost:5005

You should see your HTML page.
<img width="1883" height="785" alt="image" src="https://github.com/user-attachments/assets/47b1cb1d-4f65-4338-ade6-fbcd5b740cbe" />
