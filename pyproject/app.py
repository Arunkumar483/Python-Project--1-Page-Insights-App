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
    captcha=data["captchaResult"]
    timestamp=data["analysisUTCTimestamp"]
    lighthouseResult=data["lighthouseResult"]

    #viewport parameters
    viewportdetails=data["lighthouseResult"]["audits"]["viewport"]
    viewportid=viewportdetails["id"]
    viewporttitle=viewportdetails["title"]

    #viewport score checker
    viewportscore=viewportdetails["score"]
    if(int(viewportscore)==1):
        viewportscore="GOOD"
    else:
        viewportscore="BAD"
    viewportdescription=viewportdetails["description"]
    analyzedurl=data["id"]


    #unusedjs parameters
    unusedjsdetails=data["lighthouseResult"]["audits"]["unused-javascript"]
    unusedjsid=unusedjsdetails["id"]
    unusedjstitle=unusedjsdetails["title"]

    #unusedjs score checker
    unusedjsscore=unusedjsdetails["score"]
    if(int(unusedjsscore)==1):
        unusedjsscore="GOOD"
    else:
        unusedjsscore="BAD"
    unusedjsdescription=unusedjsdetails["description"]
    analyzedurl=data["id"]

    return render_template('results.html',urltobechecked=urltobechecked,data=data,captcha=captcha,timestamp=timestamp,lighthouseResult=lighthouseResult,analyzedurl=analyzedurl,viewportid=viewportid,viewportdetails=viewportdetails,viewportscore=viewportscore,viewportdescription=viewportdescription,viewporttitle=viewporttitle,unusedjsid=unusedjsid,unusedjsdetails=unusedjsdetails,unusedjsscore=unusedjsscore,unusedjsdescription=unusedjsdescription,unusedjstitle=unusedjstitle)




    


if __name__=='__main__':
    app.run()