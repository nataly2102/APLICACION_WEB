function getClientes() {

    var request = new XMLHttpRequest();
    //Accede a la session de la pagina
    usernombre = window.prompt('Usernombre:')
    password = window.prompt('Password:')

    request.open('GET', "https://8000-nataly2102-aplicacionwe-s2ngn7hd0f5.ws-us53.gitpod.io/clientes/"); //pasamos el metodo y luego el endpoint que es la url
    request.setRequestHeader("Accept", "application/json");
    request.setRequestHeader("Authorization", "Basic " + btoa(usernombre + ":" + password))
    request.setRequestHeader("content-type", "application/json");
    
    const  tabla   = document.getElementById("tabla_clientes"); //quiere decir que ya existe una tabla le decimos a la api que tome lo que se ya existe y que pueda eliminarlo y todo lo que necesitamos

    var tblBody = document.createElement("tbody"); //quiere decir que ya existe una tabla le decimos a la api que tome lo que se ya existe y que pueda eliminarlo y todo lo que necesitamos
    var tblHead = document.createElement("thead"); //creamos una variable para el encabezado de la tabla

    tblHead.innerHTML = `
        <tr>
            <th>DETALLE</th>
            <th>ACTUALIZAR</th>
            <th>BORRAR</th>
            <th>ID CLIENTE</th>
            <th>NOMBRE</th>
            <th>EMAIL</th>
        </tr>`;

    request.onload = () => {
        // Almacena la respuesta en una variable, si es 202 es que se obtuvo correctamente
        const response = request.responseText;
        const json = JSON.parse(response);
        if (request.status === 401 || request.status === 403) { //si me muestras un 401 o un 403 muestrame el siguiente mensaje
            alert(json.detail);
        }
        
        else if (request.status == 202){
            const response = request.responseText;
            const json = JSON.parse(response);
            for (let i = 0; i < json.length; i++) {
                var tr = document.createElement('tr');
                var detalle = document.createElement('td');
                var actualizar = document.createElement('td');
                var borrar = document.createElement('td');
                var id_cliente = document.createElement('td');
                var nombre = document.createElement('td');
                var email = document.createElement('td');

                detalle.innerHTML = "<a href='cliente.html?"+json[i].id_cliente+"'>Detalle</a";
                actualizar.innerHTML = "<a href='actualizar_cliente.html?"+json[i].id_cliente+"'>Actualizar</a";
                borrar.innerHTML = "<a href='eliminar_clientes.html?"+json[i].id_cliente+"'>Borrar</a";
                id_cliente.innerHTML = json[i].id_cliente;
                nombre.innerHTML = json[i].nombre;
                email.innerHTML = json[i].email;

                tr.appendChild(detalle);
                tr.appendChild(actualizar);
                tr.appendChild(borrar);
                tr.appendChild(id_cliente);
                tr.appendChild(nombre);
                tr.appendChild(email);
                
                tblBody.appendChild(tr);
            }
            tabla.appendChild(tblHead);
            tabla.appendChild(tblBody);
        }
    };
    request.send();
}