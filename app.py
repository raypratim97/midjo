from flask import Flask,request,render_template
import google.generativeai as palm
import json,time,requests
app = Flask(__name__)

headers = {
    "Authorization": "Token r8_28AhTuxBsmLq0kv2aV7Mh5rSFhMTadP4DLdlr",
    "Contnt-Type": "application/json"
}
    
palm.configure(api_key="AIzaSyCCT1K99BJ1JbLwhCE7qOcQ5KOZcPJ9ZZ4")
model = {"model" : "models/chat-bison-001"}
@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        q = request.form.get("q")

        body = json.dumps(
         {
     'version' : 'db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf',
     "input": {"prompt":q}
         }
        )

        output=requests.post("https://api.replicate.com/v1/predictions",data=body,headers=headers)
        time.sleep(10)
        get_url = output.json()["urls"]["get"]
        #print(get_url)
        get_result = requests.post(get_url,headers=headers).json()['output']


        #print image
#         from PIL import Image
#         image = Image.open(requests.get(get_result[0], stream=True).raw)


        return(render_template("index.html",r=get_result[0]))
    else:
        return(render_template("index.html",r="waiting for description....."))
if __name__ == "__main__":
    app.run()
