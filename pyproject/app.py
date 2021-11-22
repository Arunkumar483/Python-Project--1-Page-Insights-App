from flask import Flask, json,render_template,request
import os
from dotenv import load_dotenv
import requests
#Standard :WSGI -> Standard that is used for communication between appliication and server.

load_dotenv()

api_key = os.getenv('API_KEY')
app=Flask(__name__)

#Decorator binded with function

@app.route('/',methods=['Get'])
def index():
    return render_template("index.html")

@app.route('/results',methods=['GET'])
def result():
    
    urltobechecked=request.args.get('url')
    api_key = 'AIzaSyAhSbk4l49jwrWO9iBaD_hJeLg3elYjSEw'
    #binding api key with the url to be assessed
    search_api_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url='+urltobechecked+'/&key='+api_key
    
    #getting the information response from the specified url
    response = requests.get(search_api_url)
    
    #convert json string into python dictionary
    data=json.loads(response.content)

    #getting necessary parameters from the response's dictionary (data) 
    analyzedurl=data["id"]
    captcha=data["captchaResult"]
    timestamp=data["analysisUTCTimestamp"]
    lighthouseResult=data["lighthouseResult"]
    auditsdata=data["lighthouseResult"]["audits"]
    
    #iterating through audits
    auditsdata=data["lighthouseResult"]["audits"]

    return render_template('results.html',urltobechecked=urltobechecked,data=data,captcha=captcha,timestamp=timestamp,lighthouseResult=lighthouseResult,analyzedurl=analyzedurl,auditsdata=auditsdata)

if __name__=='__main__':
    app.run(debug=True)