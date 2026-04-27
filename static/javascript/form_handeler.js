
let inputs= document.querySelectorAll("form input, form select");
let submitForm = document.getElementById("register-button");




inputs.forEach((input)=>{

    input.addEventListener("change" , (event)=>{
      localStorage.setItem(input.name , input.value)
    })
})


submitForm.addEventListener("click" , async(e)=>{

    e.preventDefault();

    let data={}

    inputs.forEach((input)=>{

     data[input.name]= localStorage.getItem(input.name);
     
    
});
  try {
        const response = await fetch('/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data) 
        });

        if (response.ok) {
            const result = await response.json();
            alert("Data saved successfully!");
            localStorage.clear(); 

            // Redirect the user to the URL sent by Flask
             window.location.href = result.redirect_url;
        }
    } catch (error) {
        console.error("Error sending data:", error);
    }


    

});




