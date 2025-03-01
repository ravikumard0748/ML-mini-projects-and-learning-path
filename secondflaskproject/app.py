from os import name
from django.shortcuts import render
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sub",methods=["POST"])

def submit():
    if request.method=="POST":
        name=request.form["username"]
    return render_template("submit.html",n=name)
    
    

if __name__ == "__main__":
    app.run(debug=True)

