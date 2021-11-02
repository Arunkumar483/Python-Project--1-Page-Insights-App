from flask import Flask, json,render_template
import requests
#Standard :WSGI -> Standard that is used for communication between appliication and server.
app=Flask(__name__)
#Decorator binded with function
@app.route('/',methods=['Get'])
def index():
    
    api_key = 'AIzaSyAhSbk4l49jwrWO9iBaD_hJeLg3elYjSEw'
    search_api_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://www.google.com&key='+api_key
    
    #getting the information response from the specified url
    response = requests.get(search_api_url)
    
    #convert json string into python dictionary
    data=json.loads(response.content)
    
    #getting necessary parameters from the response's dictionary (data) 
    captcha=data["captchaResult"]
    timestamp=data["analysisUTCTimestamp"]
    performance=data["loadingExperience"]
    
    return render_template('index.html',data=captcha,data2=timestamp,data3=performance)



@app.route('/results')
def result():
    return "<h1 align=center>Page Speed Analyser</h1>"


if __name__=='__main__':
    app.run(debug=True)