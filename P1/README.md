# **Web Page tutorial with Flask**

## **Introduction**


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

## **Styling & Templates**

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

## **Sending Data to Template**

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

