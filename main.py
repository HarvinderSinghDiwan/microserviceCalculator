from flask import Flask,request,jsonify,session,flash
import requests
import http.client
from flask_session import Session
app = Flask(__name__)
app.config.from_pyfile('config.py')
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = """eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImt
pZCI6Ik84MXk3YjZhZDdkdldIeU15WDVTVCJ9.eyJpc3MiOiJodHRwczovL2Rldi00
c2U4bG13bC5qcC5hdXRoMC5jb20vIiwic3ViIjoiUEpkWVBrbFhjTmFMd3NScjhVRUVSeUU5VXBZcHV2RHNAY2xpZW50cyIsImF1ZCI6Imh0dHA6Ly9sb2Nh
bGhvc3QuY29tIiwiaWF0IjoxNjQ2MzIyOTY4LCJleHAiOjE2NDY0MDkzNjgsImF6cCI6IlBKZFlQa2xYY05hTHdzUnI4VUVFUnlFOVVwWXB1dkRzIiwiZ3R5Ijo
iY2xpZW50LWNyZWRlbnRpYWxzIn0.P0_1FeWc00DcGfLnA888yd1aNJR8u5WDw-nibUgQyKtneRhqfWkFnNRjYaphczToF8ZRzj8FuKazvtCcRCReY437oKwZEJOk
bHqgIho2qMbMk5X1WF9OuN2dsMiP_pc6nK9po8ohSHef8KC4Ph0QJnAYqNLdCQ4tOcIqLexxfON-6q4o-W2Z1sUbcoWGj0Rck_MCatiPLgY1Qq8HYBORghbGZ-_d8Zr0
HFR4bWKhxaQR_VNLEyP3gSFFY8IrTfLUIikRJb3cHBJ0Op5SKYtzEFGS4AQQK627SYZCf7xHdlEY-cLUJZqC3AvEFcDaSXaRE5l9Yt3RxboCjFktXEGDeA"""
Session(app)
@app.route("/")
def genAuth():
    conn = http.client.HTTPSConnection("dev-4se8lmwl.jp.auth0.com")
    payload = "{\"client_id\":\"PJdYPklXcNaLwsRr8UEERyE9UpYpuvDs\",\"client_secret\":\"YcihHRcDU1KiYq0lcaSn6zHrd0q_mw_HF0fJDHXGBDPuLI755a7nPxWXp9z96Azz\",\"audience\":\"http://localhost.com\",\"grant_type\":\"client_credentials\"}"
    headers = { 'content-type': "application/json" }
    conn.request("POST", "/oauth/token", payload, headers)
    res = conn.getresponse()
    data = res.read()
    bearer_token=data.decode("utf-8").split(",")
    session['name']=bearer_token
    return str(open("index_style.css","r").read())+str(open("index.html","r").read()).format(str(bearer_token[0].split(":")[1]),app.config["FRONTEND"])

@app.route("/services")
def services():
    #getr=requests.get("http://localhost:5000/gif")
     #send_file(getr.text,mimetype='image/gif')
    if session:
        return str(open("main_style.css","r").read())+str(open("main.html","r").read()).format(app.config['FRONTEND'],app.config['FRONTEND'],app.config['FRONTEND'])
    return genAuth()
@app.route("/addition")
def add():
    args=request.args
    x=int(args.get('fnum'))
    y=int(args.get('lnum'))
    if session:
        result=requests.get("http://{}/addition?x={}&y={}".format(app.config['ADDITION'],x,y))
        
        return str(open("style.css","r").read())+str(open("result.html","r").read()).format("""Your request has been processed 
                                                                                            successfully and the SUM is given below""",result.text)
    return genAuth()
@app.route("/subtraction")
def subtract():
    args=request.args
    x=int(args.get('fnum'))
    y=int(args.get('lnum'))
    if session:
        result=requests.get("http://{}/subtraction?x={}&y={}".format(app.config['SUBTRACTION'],x,y))
        return str(open("style.css","r").read())+str(open("result.html","r").read()).format("""Your request has been processed 
                                                                                            successfully and the DIFFERENCE is given below""",result.text)
    return genAuth()
@app.route("/multiplication")
def multiply():
    args=request.args
    x=int(args.get('fnum'))
    y=int(args.get('lnum'))
    if session:
        result=requests.get("http://{}/multiplication?x={}&y={}".format(app.config['MULTIPLICATION'],x,y))
        return str(open("style.css","r").read())+str(open("result.html","r").read()).format("""Your request has been processed 
                                                                                            successfully and the PRODUCT is given below""",result.text)
    return genAuth()
#app.run(debug=False,port=80,host="0.0.0.0")
