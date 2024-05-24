import json

def listaMembros():
    with open('membros(1).json', encoding='utf-8') as arquivo:
        return json.load(arquivo) 
    
def listarMembros():
    todos_membros = listaMembros()

    for membro in todos_membros['membros']:
        if membro['id'] == id:
            return membro

def novoId():
    membros = listaMembros()
    tamanho = len(membros['membros'])
    return tamanho+1

def novoMembro(data_json):
    try:
        dados_membros = listaMembros()
        todos_membros = dados_membros['membros']
        novo_membro = data_json
        id = novoId()
        novo_membro['id'] = id
        todos_membros.append(novo_membro)

        with open('membros(1).json', encoding='utf-8') as arquivo:
            return json.dump(todos_membros, arquivo, indent=4)
        return {"status": True} 

    except Exception as E:
        return {"status": False, "error": E}

