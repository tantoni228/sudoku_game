from random import randint, sample, shuffle
from copy import deepcopy

class Generation_sudoku:
    def __init__(self, level):
        self.level = level  # Задаётся уровень сложности
        self.template = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # Шаблон строки
        self.sudoku = []  # Данные судоку (шаблон)
        self.sudoku2 = []  # Судоку с пробелами
        self.sudoku3 = []
        for i in range(3):  # Генерация шаблона судоку
            self.line = self.template.copy()
            for j in range(3):
                self.sudoku.append([])
                if i == 0 and j == 0:
                    self.sudoku[i].append(self.line)
                elif j == 0:
                    self.copy1 = self.line.copy()
                    self.part = self.line[0:i]
                    del self.copy1[0:i]
                    self.copy1 = self.copy1 + self.part
                    self.line = self.copy1
                    self.sudoku[i * 3 + j].append(self.line)
                else:
                    self.copy1 = self.line.copy()
                    self.part = self.line[0:3]
                    del self.copy1[0:3]
                    self.copy1 = self.copy1 + self.part
                    self.line = self.copy1
                    self.sudoku[i * 3 + j].append(self.line)

    def transport_1_rows(self):
        self.y_big = randint(0, 2)  # Место в большой строке где будет происходиться перемешивание
        self.y_small1, self.y_small2 = sample([0, 1, 2], 2)  # Место маленьких строк, которые будут перемешиваться между собой
        self.sudoku[self.y_big * 3 + self.y_small1], self.sudoku[self.y_big * 3 + self.y_small2] = self.sudoku[self.y_big * 3 + self.y_small2], self.sudoku[self.y_big * 3 + self.y_small1]

    def transport_1_columns(self):
        self.x_big = randint(0, 2)  # Место в большом столбце где будет происходиться перемешивание
        self.x_small1, self.x_small2 = sample([0, 1, 2], 2)  # Место в маленьких столбцах которые будут перемешиваться между собой
        for i in range(9):  # Перестановка каждого элемета в столбцы
            self.sudoku[i][0][self.x_big * 3 + self.x_small1], self.sudoku[i][0][self.x_big * 3 + self.x_small2] = self.sudoku[i][0][self.x_big * 3 + self.x_small2], self.sudoku[i][0][self.x_big * 3 + self.x_small1]

    def transport_3_rows(self):
        self.y_big1, self.y_big2 = sample([0, 1, 2], 2)  # Большие строки, которые будут перемешиваться между собой
        for h in range(3):  # Перестановка каждой строки
            self.sudoku[self.y_big1 * 3 + h], self.sudoku[self.y_big2 * 3 + h] = self.sudoku[self.y_big2 * 3 + h], self.sudoku[self.y_big1 * 3 + h]

    def transport_3_columns(self):
        self.x_big1, self.x_big2 = sample([0, 1, 2], 2)  # Большие столбцы, которые будут перемешиваться между собой
        for i in range(3):  # Перестановка каждого столбца
            for j in range(9):  # Перестановка каждого элемета в столбцы
                self.sudoku[j][0][self.x_big1 * 3 + i], self.sudoku[j][0][self.x_big2 * 3 + i] = self.sudoku[j][0][self.x_big2 * 3 + i], self.sudoku[j][0][self.x_big1 * 3 + i]

    def mix(self):  # Перемешивание судоку
        self.n = randint(30, 45)
        for i in range(self.n):  # Примение каждого приёма перемешивания
            self.transport_1_rows()
            self.transport_3_columns()
            self.transport_3_rows()
            self.transport_1_columns()
        for i in self.sudoku:
            self.sudoku2.append(*i)
        self.sudoku3 = deepcopy(self.sudoku2)


    def eating_cells(self):
        if self.level == "лёгкий":
            self.n = randint(31, 35)  # Количестов подсказок на лёгком уровне
        elif self.level == "средний":
            self.n = randint(26, 30)  # Количестов подсказок на среднем уровне
        elif self.level == "сложный":
            self.n = randint(23, 25)  # Количестов подсказок на сложном уровне
        self.long = 81  # Количесто неудаленных клеток
        while self.long != self.n:
            self.x = randint(0, 8)
            self.y = randint(0, 8)
            if self.sudoku2[self.y][self.x] == 0:  # Условие, для того чтобы не повторять одну операцию несколько раз
                continue
            self.sudoku2[self.y][self.x] = 0
            if solve(self.sudoku2) == self.sudoku3:  # Проверка на одно решение при "поедание одной клетки"
                self.long -= 1
            else:
                self.sudoku2[self.y][self.x] = self.sudoku3[self.y][self.x]  # Возращаем значение, если не возможно

    def listing(self):  # Возвращает данные сгенерированного судоку
        return self.sudoku3, self.sudoku2
