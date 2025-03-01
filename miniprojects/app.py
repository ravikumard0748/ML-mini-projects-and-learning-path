from flask import Flask,render_template,request
from models import mainmodel as mm

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])

def home():
    val=[[0]]
    if request.method=="POST":
        hrs=request.form['hrs']
        val=mm.predictmark(hrs)
    return render_template("index.html",n=val)
    
app.run(debug=True)