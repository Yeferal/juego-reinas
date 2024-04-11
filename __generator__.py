import random


def generate_gene():
    list_gene = []
    for col in range(1, 9):
        row = random.randint(1, 8)
        list_gene.append([col, row])
    return list_gene


def generate_population():
    list_population = []
    for i in range(10):
        chromosome = generate_gene()
        # list_population
        list_population.append([chromosome, 0])
    return list_population


def evaluate_population(population):
    for item in population:
        item[1] = evaluate_chromosome(item[0])

    for item in population:
        print(item)
    return population


def evaluate_chromosome(chromosome):
    val_apt = 0;
    for i_col in range(8):
        col, row = chromosome[i_col]
        # Analizamos las posiciones del cuadrado resultante
        for j_col in range(i_col, 8):
            col_s, row_s = chromosome[j_col]
            # Primero verificamos si estan en la misma fila
            # Segundo verificamos si esta en la diagonal de la reina principal
            if (not (((row - row_s) == 0) or (abs(col - col_s) == abs(row - row_s)))):
                val_apt = val_apt + 1
    # print(F"Numero de parejas: {val_apt}")
    return val_apt


def select_roulette(population):
    s = 0
    for item in population:
        s = s + item[1]
    print("Total S = ", s)
    for i in range(len(population)):
        rand = random.randint(0, s)
        print("busca: ", rand)
        add = 0
        for item in population:
            apt = item[1]
            add = add + apt
            print("A = ",add)
            if (add >= rand):
                return item
            # else:
            #     add = add + apt


def cross_genetic(fth1, fth2):
    print("PADRES:")
    print(fth1)
    print(fth2)
    list_child1 = []
    list_child2 = []
    for i in range(4):
        list_child1.append(fth1[0][i])
        list_child2.append(fth2[0][i])
    for i in range(4):
        list_child1.append(fth2[0][4+i])
        list_child2.append(fth1[0][4+i])

    child1 = [list_child1, evaluate_chromosome(list_child1)]
    child2 = [list_child2, evaluate_chromosome(list_child2)]
    print("HIJOS:")
    print(child1)
    print(child2)
    return [child1, child2]
