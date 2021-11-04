from flask import Flask, json,render_template,request

import requests
#Standard :WSGI -> Standard that is used for communication between appliication and server.
app=Flask(__name__)

#Decorator binded with function

@app.route('/',methods=['Get'])
def index():
    return render_template("index.html")

@app.route('/results',methods=['GET','POST'])
def result():
    if request.method == 'POST':
        urltobechecked=request.form['url']
    #req=request.form['url']

    api_key = 'AIzaSyAhSbk4l49jwrWO9iBaD_hJeLg3elYjSEw'
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
    app.run()