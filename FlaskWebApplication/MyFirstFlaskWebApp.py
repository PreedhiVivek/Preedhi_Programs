from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route("/")
def say_hello():
   #"My first app"
   #return "This is my first flask application"
   "Returning the template"  
   return render_template('index.html')

if (__name__=='__main__') :
   app.run(host='0.0.0.0', port=5000, debug= True)