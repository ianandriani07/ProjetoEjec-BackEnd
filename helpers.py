import json

def listaClientes():
    with open('Clientes.json', encoding='utf-8') as arquivo:
        return json.load(arquivo)  

def Projeto(id):
    todos_Clientes = listaClientes()

    for info_projeto in todos_Clientes['clientes']:
        if info_projeto['id'] == id:
            return info_projeto

def Descricao(id):
    todos_Clientes = listaClientes()

    for info_projeto in todos_Clientes['clientes']:
        if info_projeto['id'] == id:
            return info_projeto['Descricao']

def NomeCliente(id):
    todos_Clientes = listaClientes()

    for info_projeto in todos_Clientes['clientes']:
        if info_projeto['id'] == id:
            return info_projeto['Cliente']

def Envolvidos(id):
    todos_Clientes = listaClientes()

    for info_projeto in todos_Clientes['clientes']:
        if info_projeto['id'] == id:
            return info_projeto['Envolvidos']
        
def Prazo(id):
    todos_Clientes = listaClientes()

    for info_projeto in todos_Clientes['clientes']:
        if info_projeto['id'] == id:
            return info_projeto['Prazo']
        
def REP(id):
    todos_Clientes = listaClientes()

    for info_projeto in todos_Clientes['clientes']:
        if info_projeto['id'] == id:
            return info_projeto['link rep']
        
def Proj(id):
    todos_Clientes = listaClientes()

    for info_projeto in todos_Clientes['clientes']:
        if info_projeto['id'] == id:
            return info_projeto['link proj']



def proximoId():
    clientes = listaClientes()
    tamanho_lista = len(clientes['clientes'])
    return tamanho_lista+1

def addclient(data_json):
    
    try:
        listcustomer = listCustomer()
        todos_membros = listcustomer['custumer_name']
        new_custumer = data_json
        id = nextId()
        new_custumer['id'] = id
        todos_membros.append(new_custumer)
        
        with open('membros.json', 'w', encoding='utf-8') as arquivo:
            json.dump(todos_membros, arquivo, indent=4)
        return {"status": True}
    except Exception as E:
        return {"status": False, "erro": E}


