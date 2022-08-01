from flask import Flask, jsonify
import requests
from requests.structures import CaseInsensitiveDict

app = Flask(__name__)

#Dad jokes URL
dadjokeapi = "https://icanhazdadjoke.com/"

#Get a random dad joke
@app.route("/jokeme")
def get_joke():
        headers = CaseInsensitiveDict()
        #As per api documentation, request for json results with a header
        headers["Accept"] = "application/json"
        response = requests.get(dadjokeapi,headers=headers)

        if response.status_code == 200:

            #return json response
            return response.json()
        else:
            #There is an error in the request
            print(f"Hello geek, there's a {response.status_code} error with your request")

# ##add host as 0.0.0.0 to be accessible from outside when running as a container
if __name__ == '__main__':
    app.run(host='0.0.0.0')