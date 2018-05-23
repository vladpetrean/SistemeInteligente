file = open("NumeFamilie.txt", "r")


def obtainNume():
    lista = []
    for line in file:
        if ("(wikt)") in line:
            line = line[:-8]
            lista.append(line)
    return lista
