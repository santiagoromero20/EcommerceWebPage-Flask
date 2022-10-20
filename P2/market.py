from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home') 
def home_page():
    return render_template("home.html")

@app.route('/market') 
def market_page():
    items = [
        {'id': 1,'name':"Phone", 'barcode':"187345", 'price':500},
        {'id': 2,'name':"Laptop", 'barcode':"543349", 'price':900},
        {'id': 3,'name':"Keyboard", 'barcode':"293342", 'price':150},
    ]
    return render_template("market.html", items=items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)