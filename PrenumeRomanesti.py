file = open("Prenume.txt", "r")


def obtainPrenume():
    lista = []
    for line in file:
        if ("(wikt) @") in line:
            line = line[:-10]
            lista.append(line)
    return lista
