# **Web Page tutorial with Flask**
## Template Inheritence

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




