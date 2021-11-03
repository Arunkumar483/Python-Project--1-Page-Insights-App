from flask import Flask, json,render_template
import requests
#Standard :WSGI -> Standard that is used for communication between appliication and server.
app=Flask(__name__)
#Decorator binded with function
@app.route('/',methods=['Get'])
def index():
    
    api_key = 'AIzaSyAhSbk4l49jwrWO9iBaD_hJeLg3elYjSEw'
    search_api_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=http://www.biomotionlog.in/&key='+api_key
    
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

    #viewport score
    viewportscore=viewportdetails["score"]
    if(int(viewportscore)==1):
        viewportscore="GOOD"
    else:
        viewportscore="BAD"
    #firstmeaningfulpaint=data['first-meaningful-paint']
    viewportdescription=viewportdetails["description"]
    analyzedurl=data["id"]


    return render_template('index.html',data=data,viewportdetails=viewportdetails,viewportscore=viewportscore,viewportdescription=viewportdescription,captcha=captcha,timestamp=timestamp,lighthouseResult=lighthouseResult,analyzedurl=analyzedurl,viewportid=viewportid,viewporttitle=viewporttitle)




@app.route('/results')
def result():
    return "<h1 align=center>Page Speed Analyser</h1>"


if __name__=='__main__':
    app.run(debug=True)