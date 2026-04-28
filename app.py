# handel every thing
import json
from flask import Flask , request ,render_template ,jsonify


#initial static folder
app = Flask(__name__)

#the place where json files that store data 
filename = "db/talents_form.json"
contentfile = "db/player_videos.json"


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

  # 2. Get User Videos from the content halders file
    # Find ALL Videos for this user


    with open(contentfile, "r") as file:
        all_videos = json.load(file)


    # 1. get all users from  "database" file
  
    with open(filename, "r") as file:
    #convert json arry into python array
        all_users = json.load(file)

    for video in all_videos:
        raw_url = video.get('video_url', '')
    
    # Convert youtu.be links
    if "youtu.be/" in raw_url:
        video['video_url'] = raw_url.replace("youtu.be/", "www.youtube.com/embed/").split('?')[0]
    
    # Convert standard watch?v= links
    elif "watch?v=" in raw_url:
        video['video_url'] = raw_url.replace("watch?v=", "embed/").split('&')[0]
    #get the user videos and user data

    metadata=[]
    # search the user using his email
    for targetuser in all_users :
        usermail= targetuser['email']
        for video in all_videos:
            videomail=video['email']
            if videomail == usermail:

                compined_data={
                    "user_info": targetuser,
                    "video_info": video
                }
                metadata.append(compined_data)



    

    return render_template("talents.html" , metadata=metadata)


# routing profile page depending on the user's email 
@app.route("/player-profile/<path:email>")
def profile(email):
    # Get the 'mode' from the URL (it will be 'view' if clicked from talents page)
     mode = request.args.get('mode')
    # 1. get all users from  "database" file
     user = None
     with open(filename, "r") as file:
    #convert json arry into python array
        all_users = json.load(file)
  
     
    # search the user using his email
     for targetuser in all_users:
        if targetuser.get('email') == email:
            user=targetuser
       
    # 2. Get User Videos from the content halders file
        # Find ALL Videos for this user
     user_videos = []
     try:
        with open(contentfile, "r") as file:
            all_videos = json.load(file)
            # Filter the videos to only show ones belonging to this email
            for video in all_videos:
                if video.get('email') == email:
                    user_videos.append(video)
     except (FileNotFoundError, json.JSONDecodeError):
        # If file doesn't exist, just keep the list empty
        user_videos = []
        # addapt youtube url videos
     for video in user_videos:
        raw_url = video.get('video_url', '')
        
        # Convert youtu.be links
        if "youtu.be/" in raw_url:
            video['video_url'] = raw_url.replace("youtu.be/", "www.youtube.com/embed/").split('?')[0]
        
        # Convert standard watch?v= links
        elif "watch?v=" in raw_url:
            video['video_url'] = raw_url.replace("watch?v=", "embed/").split('&')[0]
     return render_template("player-profile.html" , user=user , videos=user_videos , mode=mode )
      
    
        





#adding logic to submittion form 
@app.route('/submit', methods=['POST'])

def submit():

    #get the data from json file 
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


#addin a logic for upload videos by the players

@app.route('/upload-video' , methods=['POST'])

def upload():
        #get the data from json file 
    newcontent= request.get_json()
  


    # 1. Try to get the existing list of the content
    try:
        with open(contentfile, "r") as file:
            all_videos = json.load(file) 
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist yet, start an empty list
        all_videos = []

        #add the user content to the all contents aaray

    all_videos.append(newcontent)

         # 3. store the data inside player_videos.json file
    with open(contentfile, "w") as file:
        json.dump(all_videos, file, indent=4)

         #return a messsage 
    return jsonify(
        {"status": "success",
        "message": "Data stored in JSON file",
        }), 200


  
if __name__ == '__main__':
    app.run(debug=True)


