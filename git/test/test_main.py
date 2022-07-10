from fastapi.testclient import TestClient
from code.main import app
clientes = TestClient(app)

def test_index():
    response = clientes.get("/") # requests
    data = {"message":"Hello World"}
    assert response.status_code == 200
    assert response.json()      == data

def test_clientes():
    response = clientes.get("/clientes/") #requests
    data = [{"id_cliente":1,"nombre":"Dejah","email":"deja@email.com"},
    {"id_cliente":2,"nombre":"John","email":"john@email.com"},
    {"id_cliente":3,"nombre":"Carthoris","email":"carthotis@email.com"},
    {"id_cliente":4,"nombre":"Fer","email":"fer@email.com"}]
    assert response.status_code == 200
    assert response.json()      == data

def test_client1():
    response = clientes.get("/clientes/1") #requests
    data     = [{"id_cliente":1,"nombre":"Dejah","email":"deja@email.com"}]
    assert response.status_code == 200
    assert response.json()      == data

def test_clientpost():
    payload  = {"id_cliente":4,"nombre":"Fer","email":"fer@email.com"}
    response = clientes.post("/clientes/", json=payload)
    data     = {"message":"Insertaste un cliente correctamente :)"}
    assert response.status_code == 200
    assert response.json()      == data

def test_clientdelet():
    payload  = {"id_cliente":1,"nombre":"Dejah","email":"deja@email.com"}
    response = clientes.delete("/clientes/1", json=payload)
    data     = {"message":"Eliminaste un cliente correctamente :("}
    assert response.status_code == 200
    assert response.json()      == data

def test_clientput():
    payload  = {"id_cliente":4,"nombre":"Fer","email":"fer@email.com"}
    response = clientes.put("/clientes/", json=payload)
    data     = {"message":"Actualizaste un cliente correctamente :)"}
    assert response.status_code == 200
    assert response.json()      == data 