from flask import Flask

app = Flask(__name__)  # Initialize Flask

@app.route("/")  # This sets up the root route
def home():
    return "Flask is working!"  # Response to display on the page

if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask app
