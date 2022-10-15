def read():
    numebers = []
    with open("./Archivos/numeros.txt", "r", encoding="utf-8") as f:
        for line in f:
            numebers.append(int(line))
    print(numebers)

def write():
    name = [ "Daniel", "Alberto", "Paredes", "Peralta"]
    with open("./Archivos/name.txt", "a", encoding="utf-8") as f:
        for name in name:
            f.write(name)
            f.write("\n")







def run():
    #read()
    write()






if __name__ == "__main__":
    run()