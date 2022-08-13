function PutCliente(){
    var token = sessionStorage.getItem('item');
    console.log(token)
    var request = new XMLHttpRequest();
    var id_cliente = window.location.search.substring(1);
    console.log("id_cliente: " + id_cliente);
    request.open('PUT', "https://8000-nataly2102-aplicacionwe-kx8c8dnk4fb.ws-us60.gitpod.io/clientes/" + id_cliente,true);
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("Authorization", "Bearer " + token)
    request.setRequestHeader("content-type", "application/json");
    
    request.onload = () => {
        
        const response = request.responseText;
        const json = JSON.parse(response);     
        const status = request.status;

        if (request.status === 401 || request.status === 403) {
            alert(json.detail);
        }

        else if (request.status == 202){

            console.log("Response: " + response);
            console.log("JSON: " + json);
            console.log("Status: " + status);

            alert(json.message);
            window.location.replace("clientes_all.html")
        }
    };
    request.send;
}