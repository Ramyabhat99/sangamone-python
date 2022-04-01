
from flask import Flask,render_template,request
area2=Flask(__name__)
@area2.route("/",methods=["POST","GET"])

def area():
    if request.method=="POST":
        r=float(request.form.get("input1"))
        c = 2*3.14*r
        a = 3.14*r*r
        return render_template("area2.html",message1=c, message2=a)
        
if __name__=="__main__":
   area2.run(debug=True)
   
