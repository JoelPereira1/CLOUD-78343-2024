
i="0"

while i!= "99":
    print("0","-","Menu Principal")
    if i == "0":
        print("1","-","Patentes")
        print("2","-","Militares")
    elif i == "1":
        print("11","-","Listar")
        print("12","-","Inserir")
        print("13","-","Editar")
        print("14","-","Eliminar")
        print("15","-","Procurar")
        print("16","-","Exportar")
        print("17","-","Importar")
    elif i == "2":
        print("21","-","Listar")
        print("22","-","Inserir")
        print("23","-","Editar")
        print("24","-","Eliminar")
        print("25","-","Procurar")
        print("26","-","Exportar")
        print("27","-","Importar")

    print("99","-","Sair")
    i = input("Indique a operação\n")

    if i=="99":
        i=input("Tem a certeza que quer sair? (s/n)\n")
        if i=="s":
            i="99"
        else:
            i="0"