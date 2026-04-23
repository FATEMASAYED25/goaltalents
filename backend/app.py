# handel every thing
import json
from repository import  TalentRepository
from flask import Flask , request ,render_template
from talent import Talent

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
@app.route("/profile")
def profile():
    return render_template("profile.html")





@app.route('/submit', methods=['POST'])

def submit():
    talent = Talent(
        request.form.get('full_name'),
        request.form.get('email'),
        request.form.get('phone'),
        request.form.get('position'),
        request.form.get('birth_year'),
        request.form.get('club'),
        request.form.get('experience')
    ) 



    if talent.is_valid():
       repo.save(talent)
       return "the data Saved!"
    else:
        return "data not valied"
    
if __name__ == '__main__':
    app.run(debug=True)


