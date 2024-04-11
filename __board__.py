def generate_board(chromosome):
    print("   1  2  3  4  5  6  7  8  ")
    print(" +------------------------+")
    for i in range(8):
        # gene = chromosome[i]
        for j in range(8):
            txt_white = "█"
            txt_black = " "

            if (i + j) % 2 == 0:
                for gene in chromosome:
                    if ((j + 1) == gene[0] and (i+1)==gene[1]):
                        txt_white = "x"

                if(j ==0):
                    print(F"{i+1}|█{txt_white}█", end="")  # Casilla blanca
                elif (j == 7):
                    print(F"█{txt_white}█|{i+1}", end="")
                else:
                    print(F"█{txt_white}█", end="")  # Casilla blanca
            else:
                for gene in chromosome:
                    if ((j + 1) == gene[0] and (i+1)==gene[1]):
                        txt_black = "x"

                if (j == 0):
                    print(F"{i+1}| {txt_black} ", end="")  # Casilla blanca
                elif(j==7):
                    print(F" {txt_black} |{i+1}", end="")  # Casilla blanca
                else:
                    print(F" {txt_black} ", end="")  # Casilla blanca
        print()
    print(" +------------------------+")
    print("   1  2  3  4  5  6  7  8  ")
