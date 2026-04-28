let upload_video = document.getElementById("upload-video");
let video_title =  document.getElementById("content-title");
let video_url = document.getElementById("content-body");



upload_video.addEventListener("click" , async(e)=>{
     
    e.preventDefault();

    // Get the email directly from the current URL
    const pathParts = window.location.pathname.split('/');
    const userEmail = pathParts[pathParts.length - 1];


    //create an object with the data 
    const content = {
        title:video_title.value,
        video_url:video_url.value,
        timestamp: new Date().toISOString(),
        email:userEmail
    }
    console.log(content)
    //send the contetnt to flask
    const response= await fetch('/upload-video',{
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body:JSON.stringify(content)
    });

    if (response.ok) {
        alert("Content added!");
        location.reload(); // Refresh to see the new content
    }
    


});

