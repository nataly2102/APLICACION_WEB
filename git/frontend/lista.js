function getClientes(){
    var token = sessionStorage.getItem('item');
    console.log(token);
    //Conectar Backend con Frontend
    var request = new XMLHttpRequest();
    request.open("GET","https://8000-nataly2102-aplicacionwe-kx8c8dnk4fb.ws-us60.gitpod.io/clientes/",true);
    request.setRequestHeader("Authorization", "Bearer " + token);
    request.setRequestHeader("Accept","application/json")
    request.onload = () =>{
        const response = request.responseText;
        const json = JSON.parse(response);

        var tbody = document.getElementById("tbody");
        for(let row=0; row<json.length; row++){
            var tr = document.createElement("tr");

            var td_id_cliente = document.createElement("td");
            var td_nombre = document.createElement("td");
            var td_email = document.createElement("td");
            var td_detalle = document.createElement("td");
            var td_update = document.createElement("td");
            var td_delete = document.createElement("td");

            td_id_cliente.innerHTML = json[row].id_cliente;
            td_nombre.innerHTML = json[row].nombre;
            td_email.innerHTML = json[row].email;
            td_detalle.innerHTML = "<a href='/cliente.html?"+json[row].id_cliente+"'>Detalles</a>";
            td_update.innerHTML =  "<a href='/actualizar_cliente.html?"+json[row].id_cliente+"'>Actualizar</a>";
            td_delete.innerHTML =  "<a href='/eliminar_clientes.html?"+json[row].id_cliente+"'>Eliminar</a>";

            tr.appendChild(td_id_cliente);
            tr.appendChild(td_nombre);
            tr.appendChild(td_email);
            tr.appendChild(td_detalle);
            tr.appendChild(td_update);
            tr.appendChild(td_delete);

            tbody.appendChild(tr);

        }
    };
    request.send();
};