# handel every thing
import json
from flask import Flask , request ,render_template ,jsonify


#initial static folder
app = Flask(__name__)

#the place where json files that store data 
repo = "../db/talents.json"


#routing the page using render_template library
#routing home page
@app.route("/")
def home():
      return render_template("index.html")

#routing register page
@app.route("/register")
def register():
    return render_template("register-form.html")

#routing talent page
@app.route('/talents')
def talents():
    return render_template("talents.html")

# routing profile page
@app.route("/profile/<path:email>")
def profile(email):
    return render_template("profile.html" , email=email)





@app.route('/submit', methods=['POST'])

def submit():

    #get the data from javascript file 
    user_data = request.get_json()

    #store the data inside talents_form.json file

    with open("talents_form.json", "a") as file:
        json.dump(user_data, file)
        file.write("\n")

    #extract the email to redirect the user to his profile 
    email = user_data.get("email")
    #return a messsage 
    return jsonify(
        {"status": "success",
        "message": "Data stored in JSON file",
        "redirect_url": f"/profile/{email}"}), 200


    
if __name__ == '__main__':
    app.run(debug=True)


