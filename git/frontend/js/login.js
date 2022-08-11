function Log(){
    let email = document.getElementById("email").value;
    let password = document.getElementById("contra").value;

    var request = new XMLHttpRequest();
    request.open("GET","https://8000-nataly2102-aplicacionwe-kx8c8dnk4fb.ws-us60.gitpod.io/user/validate/",true);
    request.setRequestHeader("Authorization", "Basic " + btoa(email + ":" + password));
    request.setRequestHeader("Content-Type", "application/json");
    request.setRequestHeader("Accept","application/json");
    request.onload = () =>{
        const response = request.responseText;
        const status = request.status
        const data = JSON.parse(response);

        if (status == 202) {
            alert("Bienvenido");
            sessionStorage.setItem("item",data.token);
            window.location.replace("/clientes_all.html");
            console.log(data.token)
        }
        else{
            alert("Usuario Incorrecto, intenta de nuevo");
        }
    };
   request.send();
};