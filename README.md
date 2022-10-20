# **Web Page tutorial with Flask**

## **P1. Introduction**


## Create a Enviroment

In my case I am using Anaconda, hence a conda enviroment. Follow this steps:


- Go to the folder you are going to work
- conda create -n “name” python=3.10.4
- conde activate “name”
-conda install jupyter ipykernel
- ipython kernel install --user --name=“name·
- conde install packages/libraries

---

## Flask env variables declaration

- export FLASK_APP=app.py (1)
- export FLASK_ENV=development (2)
- export FLASK_DEBUG=1 (3)

(1) The "app.py" make reference of the python file you are using as a reference.

(2) This will set Flask as a Development env, instead of a Deploymnent.

(3) To enable us to debug easily, instead we should be turning down and up our application every time we make a chango in the code and want to see the results.

---

## Important Concepts

- Decorators: It’s something that modifies the behavior of a function. In using Flask, probably you have some familiarity with a couple decorators already such as @app.route(), @classmethod, @staticmethod etc.

- App Routing: First of all, as I mentioned before, this is a type of decorator. It means mapping the URLs to a specific function that will handle the logic for that URL. 
  
   - Static Routes: This are the ones were we hardcode the url. 

            Home Page
            @app.route('/') 
            def hello():
                return 'Hello, World!'

            Welcome Page
            @app.route('/welcome') 
            def welcome():
                return 'Welcome!'
    
    - Dynamic Routes: Now, imagine you want to say hi to the person who has just log in into your page, you can not make millions of functions to say hi to everybody....

            @app.route('/welcome/<username>') 
            def welcome(username):
                return f'Welcome {username}'

  ---

## **P2. Styling & Templates**

## Front-end

We are starting with a starter code template from getboostrap.com. 
Each HTML file has two main "components", the head and body blocks.

## Important Concepts and tricks

- render_template(): This is a method from flask object, which will render out the html specify when you call the specified url
  
            @app.route('/')
            @app.route('/home') 
            def home_page():
                return render_template("home.html")

OBS: The second decorator indicates that not only when the url is empty but also when is called by /home, we should render the home.html file.

---

## **P3. Sending Data to Template**

Let´s start by a "Naive" approaach, which is hardcoding it. We should pass the parameter in the render_template() method (on the function that is returning the method, which is in charge of this job...), and on the html file call the variable like this: <p>{{ variable }}</p>.

            markey.py file

            @app.route('/market') 
            def market_page():
                items = [
                        {'id': 1,'name':"Phone", 'barcode':"123345", 'price':500},
                        {'id': 2,'name':"Laptop", 'barcode':"123346", 'price':900},
                        {'id': 3,'name':"Keyboard", 'barcode':"123347", 'price':150},
                        ]
                        return render_template("market.html", items=items)

            HTML file

            <h1>Market Page</h1>
            <p>{{ items }}</p> 

If we do this, the problem will be that all the info of the items will be displayed in a line, we want to generate a table, for example, to improve our page. 

With this, we have finished our first part of the tutorial. Let´s see how we could improve the logic of it by adding a Template inheritence, so far we have copied all the home.html code into a new market.html file and there add the necessary things, such as the table. Clearly, this is not a good practice.

## **P4.Template Inheritence**

On this second part we are going to improve our code by implementing this new concept of Templated Inheritence. The main idea is to not repeate html code on different files but rather "inheritade" from a base file.

We will create a new html file call "base.html", there will be hold the core code, and then our home and market giles will inherited from it.

## Important Concepts, Tricks and Improvements

- We will face problems with the code we had, for example, we hardcoded the title of the URL page for each URL, if we inheritence that we would always have the same title (on the head block) for every URL. To fight this:

    Previously
        <title>
        HomePage/MarketPage
        </title>

We harcoded for every file, home, market, etc...

    Now We code this on the base.html file

        <title>
        {% block title %}
            
        {% endblock %}
        </title>
    
    And on every html file that is going to inheritate the base

        {% extends "base.html" %} 
        {% block title%}
        Home page
        {% endblock %}
    
- The same logic is apply to add content to new files:
    
        Now We code this on the base.html file

        <body>
        {% block content %}
            
        {% endblock %}
        </body>
    
    And on every html file that is going to inheritate the base

        {% extends "base.html" %} 
        {% block content%}
        All the table code for market.html...
        {% endblock %}

- One last thing, on the navigation bar when we click the home, market, etc buttom we are not being redirected to those routes. There is a method to do so, **url_for()**, which basically redirects you to the URL of the page you indicate them between brackets (you have to put the name of the function which is being decorated by the URL you want to redirect). That has to be indicated on the base file.
    
        market.py file

        @app.route('/')
        @app.route('/home') 
        def home_page():
            return render_template("home.html")

        @app.route('/market') 
        def market_page():
            ...
            return render_template("market.html", items=items)


        Base.html file

        <li class="nav-item active"> 
        <a class="nav-link" href= "{{ url_for('home_page') }}" >Home <span class="sr-only">(current)</span></a> 
        </li>
        <li class="nav-item">
            <a class="nav-link" href="{{ url_for('market_page') }}">Market</a> 
        </li>

---

## **P5. Models and Databases**

We are going to use a database already "link" with Flask, which underhood is just a python class. We are using SQLAlchemy.

- Installation: "pip install flask-sqlalchemy" on conda env

- Instatiate the db object and create a class (or various) for the things you wan to store info, in our case Items.

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
        db = SQLAlchemy(app)

        class Item(db.Model):
            id = db.Column(db.Integer(), primary_key=True)
            name = db.Column(db.String(length=30), nullable=False, unique=True)
            price = db.Column(db.Integer(), nullable=False)
            barcode = db.Column(db.String(length=12), unique=True)
            description = db.Column(db.String(length=1024), nullable=False, unique=True)

- Go to MacBook-Pro-de-Carolina:FlaskFCC python3, import the db from the script were you declare it (from market import db). Then, create it, "db.create_all()". By now you should see it on your project.

How can we add the items to the db ?

On the python3 script as before:

- from market imort Item
- item1 = Item(name="IPhone10", price=500, barcode="187345987832", descrition="descr")
- db.session.add(item1)
- db.session.commit()
  
To verify if it was correctly uploaded to the db,

- Item.query.all()