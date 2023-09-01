from random import randint, sample, shuffle
from copy import deepcopy

class Generation_sudoku:
    def __init__(self, level):
        self.level = level  # The difficulty level is set
        self.template = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # String Template
        self.sudoku = []  # Sudoku data (template)
        self.sudoku2 = []  # Судоку с пробелами
        self.sudoku3 = []
        for i in range(3):  # Sudoku with spaces
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
        self.y_big = randint(0, 2)  # The place in the big row where the mixing will take place
        self.y_small1, self.y_small2 = sample([0, 1, 2], 2)  # Place small strings that will be shuffled together
        self.sudoku[self.y_big * 3 + self.y_small1], self.sudoku[self.y_big * 3 + self.y_small2] = self.sudoku[self.y_big * 3 + self.y_small2], self.sudoku[self.y_big * 3 + self.y_small1]

    def transport_1_columns(self):
        self.x_big = randint(0, 2)  # The place in the large column where the mixing will take place
        self.x_small1, self.x_small2 = sample([0, 1, 2], 2)  # Place in small columns that will mix with each other
        for i in range(9):  # Rearranging each element into columns
            self.sudoku[i][0][self.x_big * 3 + self.x_small1], self.sudoku[i][0][self.x_big * 3 + self.x_small2] = self.sudoku[i][0][self.x_big * 3 + self.x_small2], self.sudoku[i][0][self.x_big * 3 + self.x_small1]

    def transport_3_rows(self):
        self.y_big1, self.y_big2 = sample([0, 1, 2], 2)  # Large strings that will be shuffled together
        for h in range(3):  # Rearranging each row
            self.sudoku[self.y_big1 * 3 + h], self.sudoku[self.y_big2 * 3 + h] = self.sudoku[self.y_big2 * 3 + h], self.sudoku[self.y_big1 * 3 + h]

    def transport_3_columns(self):
        self.x_big1, self.x_big2 = sample([0, 1, 2], 2)  # Large columns that will be shuffled together
        for i in range(3):  # Rearranging each column
            for j in range(9):  # Rearranging each element into columns
                self.sudoku[j][0][self.x_big1 * 3 + i], self.sudoku[j][0][self.x_big2 * 3 + i] = self.sudoku[j][0][self.x_big2 * 3 + i], self.sudoku[j][0][self.x_big1 * 3 + i]

    def mix(self):  # Shuffling Sudoku
        self.n = randint(30, 45)
        for i in range(self.n):  # Application of each mixing technique
            self.transport_1_rows()
            self.transport_3_columns()
            self.transport_3_rows()
            self.transport_1_columns()
        for i in self.sudoku:
            self.sudoku2.append(*i)
        self.sudoku3 = deepcopy(self.sudoku2)


    def eating_cells(self):
        if self.level == "лёгкий":
            self.n = randint(31, 35)  # Number of hints at an easy level
        elif self.level == "средний":
            self.n = randint(26, 30)  # The number of hints at the average level
        elif self.level == "сложный":
            self.n = randint(23, 25)  # Number of hints at a difficult level
        self.long = 81  # The number of undeleted cells
        while self.long != self.n:
            self.x = randint(0, 8)
            self.y = randint(0, 8)
            if self.sudoku2[self.y][self.x] == 0:  # Condition, in order not to repeat the same operation several times
                continue
            self.sudoku2[self.y][self.x] = 0
            if solve(self.sudoku2) == self.sudoku3:  # Checking for one solution when "eating one cell"
                self.long -= 1
            else:
                self.sudoku2[self.y][self.x] = self.sudoku3[self.y][self.x]  # Return the value if not possible
    def listing(self):  # Returns the data of the generated Sudoku
        return self.sudoku3, self.sudoku2
