# handel every thing
import json
from flask import Flask , request ,render_template ,jsonify


#initial static folder
app = Flask(__name__)

#the place where json files that store data 
filename = "db/talents_form.json"


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

# routing profile page depending on the user's email 
@app.route("/player-profile/<path:email>")
def profile(email):

    # 1. Open the "database" file
 
     with open(filename, "r") as file:
    #convert json arry into python array
        all_users = json.load(file)
  
    
    # search the user using his email
     for user in all_users:
        if user.get('email') == email:

         return render_template("player-profile.html" , user=user)
        
# 3. If the loop finishes and find nothing
     return "User profile not found", 404




#adding logic to submittion form 
@app.route('/submit', methods=['POST'])

def submit():

    #get the data from javascript file 
    user_data = request.get_json()
  


    # 1. Try to get the existing list of users
    try:
        with open(filename, "r") as file:
            all_users = json.load(file) 
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist yet, start an empty list
        all_users = []

 
   # 2. Add the new user to the Python list
    all_users.append(user_data)

    # 3. store the data inside talents_form.json file
    with open(filename, "w") as file:
        json.dump(all_users, file, indent=4)

    #extract the email to redirect the user to his profile 
    email = user_data.get("email")
    #return a messsage 
    return jsonify(
        {"status": "success",
        "message": "Data stored in JSON file",
        "redirect_url": f"/player-profile/{email}"}), 200


    
if __name__ == '__main__':
    app.run(debug=True)


