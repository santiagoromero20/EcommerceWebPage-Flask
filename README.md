# Flask Market E-commerce

On this project I code a "toy-webpage". The objective of this project was to get more familiar with Flask, HTML, CSS and SQLAlchemy to gain more clarity of the workflow when deploying ML models into production.

![Alt ](images/goat.jpeg "Title")

## **Project Structure**

    ├── Market
    │    ├── static
    │    │    └── img
    │    │         └── logo.png
    │    ├── templates
    │    │    ├── base.html
    │    │    ├── home.html
    │    │    ├── login.html
    │    │    ├── market.html
    │    │    └── register.html
    │    ├── __init__.py
    │    ├── forms.py
    │    ├── models.py
    │    └── routes.py
    │
    ├── requierements.txt
    ├── run.py    
    └── README.md

## **Teachings**

On this project I have deepen my knowledge in all the technologies mentioned. For example on **HTML**, starting from discovering new tags up until the concept of inheritence, and the idea of Boostrap on **CSS**. Then, I learned a lot of built-in classes from Flask such as **FlaskForm** to easily build a proper RegistrationForm class, different security techniques as hashing the passwords (with **bcrypt** library) to store them on the Databases and logically the use of them, in this particular case **sqlite**. And also the use of **SQLAlchemy** to easily write SQL queries and handle tables creation with intuitive python code.
## **Installation and Usage**

I would recommend you to start by creating a virtual or conda environment, whatever you prefer. Once, created install all the dependencies of the project specified on requierements.txt inside this env. Then clone from this repo the code into your local VSCode, PyCharm, etc. It´s important to respect the places of the directories and files if not you may face some problems to start running the program. Finally, write this commands on your terminal:

        #Asssign run.py as the "runner" file for Flask
        export FLASK_RUN=run.py

        #Run the App!
        flask run

Be aware of assigning your own settings to:

        app.config["SQLALCHEMY_DATABASE_URI"] 
        app.config["SECRET_KEY"] 

Hope you like and learn from this project as much as myself!      
