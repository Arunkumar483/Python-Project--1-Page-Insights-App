from flask import Flask, json,render_template
import requests
#Standard :WSGI -> STANDARD THAT IS USED TO COMMUNICATE MY APP TO SERVER
app=Flask(__name__)
#Decorator binded with function
@app.route('/',methods=['Get'])
def index():
    
    api_key = 'AIzaSyAhSbk4l49jwrWO9iBaD_hJeLg3elYjSEw'
    search_api_url = 'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://www.google.com&key='+api_key
    #getting the information response from the specified url
    response = requests.get(search_api_url)
    data=json.loads(response.content)
    captcha=data["captchaResult"]
    timestamp=data["analysisUTCTimestamp"]
    performance=data["loadingExperience"]
    
    return render_template('index.html',data=captcha,data2=timestamp,data3=performance)



@app.route('/results')
def result():
    #return json.jsonify({"hello":"gk"})
    return "<h1 align=center>Page Speed Analyser</h1>"


if __name__=='__main__':
    app.run(debug=True)