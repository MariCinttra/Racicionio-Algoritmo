dic = {"Joao": "a", "Maria": "b", "Pedro": "c"}
print(dic)

excluido = dic.pop("Joao")
print("Excluído foi:", excluido)
print(str(dic))

dic.popitem()
print(str(dic))
