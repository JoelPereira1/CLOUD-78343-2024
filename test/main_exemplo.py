from utils import Utils
from militar import Militar

obj1 = Militar("Mancebo","Sérgio","Fontes")
obj1.Idade =47
obj2 = Militar("Cabo","Joel","Pereira")
obj2.Idade = 33
lst =[obj1.ToDicionario(),obj2.ToDicionario()]

print(obj2.__dict__)

#Utils.ExportToCSV("militares.csv",Militar.Header(),lst,";",quoting=2)

result,lista,erro = Utils.ImportFromCSV("militares.csv",";")
if result:
    print(lista)




