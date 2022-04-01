
from flask import Flask,render_template
area1=Flask(__name__)
@area1.route("/",methods=["POST","GET"])

def area():
    r = 5
    c = 2*3.14*r
    a = 3.14*r*r
    print("Circumference of circle", c)
    print("Area of circle",a)
    return render_template("area1.html",message1=c, message2=a)
   
if __name__=="__main__":
   area1.run(debug=True)
   
