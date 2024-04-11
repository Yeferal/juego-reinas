

import __generator__
import __board__


def main():
    population = __generator__.generate_population()
    population = __generator__.evaluate_population(population)
    fth1 = __generator__.select_roulette(population)
    fth2 = __generator__.select_roulette(population)
    childs = __generator__.cross_genetic(fth1, fth2)
    __board__.generate_board(childs[0][0])
    __board__.generate_board(childs[1][0])

main()