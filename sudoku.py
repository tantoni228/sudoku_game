from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QLabel, QComboBox, QInputDialog, QLineEdit
from PyQt5 import QtCore
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt
from generation import Generation_sudoku
import os.path
import sys


if not os.path.exists("files.txt"):  # проверка сущетвование файла
    sudoku = Generation_sudoku('лёгкий')  # начало генерации судоку
    sudoku.mix()
    sudoku.eating_cells()
    full_sudoku, incomplete_sudoku = sudoku.listing()  # получаем значение полного и неполного судоку
    f = open("files.txt", 'w')  # создание файла
    for i in range(9):  # запись данных о судоку
        for g in range(9):
            f.write(str(i * 9 + g))  # номер клетки начиная с 0
            f.write(" ")
            f.write(str(full_sudoku[i][g]))  # значение в полном судоку
            f.write(" ")
            f.write(str(incomplete_sudoku[i][g]))  # значение в неполном судоку
            f.write('\n')
    else:
        f.write('лёгкий')
    f.close()  # закрытие файла


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 630, 590)

        # Создание кнопок
        self.btns = []
        for i in range(9):
            self.btns.append([])
            for j in range(9):
                self.btn = QPushButton(self)
                self.btn.resize(30, 30)
                self.btns[i].append(self.btn)
                self.btn.move(30 + 31 * j, 140 + 31 * i)
                self.btn.clicked.connect(self.active)

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(360, 470, 241, 51))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setText("Отчистить")
        self.pushButton.clicked.connect(self.clean)

        # Создание надписи "Судоку"
        self.label = QLabel(self)
        self.label.setGeometry(QtCore.QRect(200, 0, 200, 55))
        self.label.setMouseTracking(True)
        self.label.setLineWidth(50)
        self.label.setTextFormat(QtCore.Qt.MarkdownText)
        self.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; font-weight:600; font-style:italic; color:#203eff;\">Судоку</span></p></body></html>")

        # Создание надписи "Уровень:"
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 90, 30))
        self.label_2.setText("<html><head/><body><p><span style=\" font-size:16pt;\">Уровень:</span></p></body></html>")

        self.label_3 = QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(120, 100, 90, 30))
        with open('files.txt', 'rt') as f:
            value = f.readlines()[-1]
        if value == "лёгкий":
            self.label_3.setText("<html><head/><body><p><span style=\" font-size:16pt;\">лёгкий</span></p></body></html>")
        elif value == "средний":
            self.label_3.setText("<html><head/><body><p><span style=\" font-size:16pt;\">средний</span></p></body></html>")
        else:
            self.label_3.setText("<html><head/><body><p><span style=\" font-size:16pt;\">сложный</span></p></body></html>")

        self.label_4 = QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 70, 170, 30))
        self.label_4.setText("<html><head/><body><p><span style=\" font-size:14pt;\">Имя пользователя:</span></p></body></html>")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(200, 75, 160, 20))

        self.pushButton_num = QPushButton(self)
        self.pushButton_num.setGeometry(QtCore.QRect(360, 220, 81, 81))
        self.pushButton_num.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_num.setText("1")
        self.pushButton_num.clicked.connect(self.assignment)

        self.pushButton_num = QPushButton(self)
        self.pushButton_num.setGeometry(QtCore.QRect(440, 220, 81, 81))
        self.pushButton_num.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_num.setText("2")
        self.pushButton_num.clicked.connect(self.assignment)

        self.pushButton_num = QPushButton(self)
        self.pushButton_num.setGeometry(QtCore.QRect(520, 220, 81, 81))
        self.pushButton_num.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_num.setText("3")
        self.pushButton_num.clicked.connect(self.assignment)

        self.pushButton_num = QPushButton(self)
        self.pushButton_num.setGeometry(QtCore.QRect(360, 300, 81, 81))
        self.pushButton_num.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_num.setText("4")
        self.pushButton_num.clicked.connect(self.assignment)

        self.pushButton_num = QPushButton(self)
        self.pushButton_num.setGeometry(QtCore.QRect(440, 300, 81, 81))
        self.pushButton_num.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_num.setText("5")
        self.pushButton_num.clicked.connect(self.assignment)

        self.pushButton_num = QPushButton(self)
        self.pushButton_num.setGeometry(QtCore.QRect(520, 300, 81, 81))
        self.pushButton_num.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_num.setText("6")
        self.pushButton_num.clicked.connect(self.assignment)

        self.pushButton_num = QPushButton(self)
        self.pushButton_num.setGeometry(QtCore.QRect(360, 380, 81, 81))
        self.pushButton_num.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_num.setText("7")
        self.pushButton_num.clicked.connect(self.assignment)

        self.pushButton_num = QPushButton(self)
        self.pushButton_num.setGeometry(QtCore.QRect(440, 380, 81, 81))
        self.pushButton_num.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_num.setText("8")
        self.pushButton_num.clicked.connect(self.assignment)

        self.pushButton_num = QPushButton(self)
        self.pushButton_num.setGeometry(QtCore.QRect(520, 380, 81, 81))
        self.pushButton_num.setStyleSheet("font: 11pt \"MS Shell Dlg 2\";")
        self.pushButton_num.setText("9")
        self.pushButton_num.clicked.connect(self.assignment)

        self.pushButton_check = QPushButton(self)
        self.pushButton_check.setGeometry(QtCore.QRect(360, 160, 241, 51))
        self.pushButton_check.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_check.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_check.setToolTip("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Проверить</span></p></body></html>")
        self.pushButton_check.setWhatsThis("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Проверить</span></p></body></html>")
        self.pushButton_check.setText("Проверить")
        self.pushButton_check.clicked.connect(self.check)

        self.pushButton_start_newgame = QPushButton(self)
        self.pushButton_start_newgame.setGeometry(QtCore.QRect(360, 100, 241, 51))
        self.pushButton_start_newgame.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_start_newgame.setIconSize(QtCore.QSize(16, 16))
        self.pushButton_start_newgame.setToolTip("<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Новая игра</span></p></body></html>")
        self.pushButton_start_newgame.setWhatsThis("<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Новая игра</span></p></body></html>")
        self.pushButton_start_newgame.setText("Новая игра")
        self.pushButton_start_newgame.clicked.connect(self.new_game)

        h = open("files.txt", "rt")  # открытие файла файла
        values = h.readlines()
        for i in range(9):
            for j in range(9):
                value = values[i * 9 + j].split()[2]
                if value != "0":
                    self.btns[i][j].setText(value)  # присваивание каждому известному элементу значение
        h.close()  # закрытие файла
        self.active_now_btn = None

    def active(self):  # запоминает какая кнонка была вкдючена
        self.active_now_btn = self.sender()
        index = [item for sublist in self.btns for item in sublist].index(self.active_now_btn)
        with open('files.txt', 'rt') as f:
            value = f.readlines()[index].split()[2]
        if value != "0":  # проврка на текст
            self.active_now_btn = None

    def assignment(self):
        self.assig_now_btnnum = self.sender().text()
        if self.active_now_btn:
            self.active_now_btn.setText(self.assig_now_btnnum)

    def check(self):
        f = open("files.txt", "rt")
        values = f.readlines()
        for i in range(9):
            for j in range(9):
                if self.btns[i][j].text() == "":
                    QMessageBox.information(self, 'Предупреждение', 'Проверьте ещё раз все ли ячейки заполнены.', QMessageBox.Ok | QMessageBox.Cancel)
                    return
                elif values[i * 9 + j].split()[1] != self.btns[i][j].text():
                    QMessageBox.information(self, 'Предупреждение', 'У вас есть ошибка. Проверьте ещё раз.', QMessageBox.Ok | QMessageBox.Cancel)
                    return
        else:
            self.difficulty_level = 'лёгкий'
            self.user = self.lineEdit.text()
            ful = f"Отличный результат, {self.user}!!!\nУровень: {self.difficulty_level}"
            QMessageBox.information(self, 'Вы победитель!!!', ful, QMessageBox.Ok | QMessageBox.Cancel)
            self.new_game()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_1:
            if self.active_now_btn:
                self.active_now_btn.setText(str(1))
        if event.key() == Qt.Key_2:
            if self.active_now_btn:
                self.active_now_btn.setText(str(2))
        if event.key() == Qt.Key_3:
            if self.active_now_btn:
                self.active_now_btn.setText(str(3))
        if event.key() == Qt.Key_4:
            if self.active_now_btn:
                self.active_now_btn.setText(str(4))
        if event.key() == Qt.Key_5:
            if self.active_now_btn:
                self.active_now_btn.setText(str(5))
        if event.key() == Qt.Key_6:
            if self.active_now_btn:
                self.active_now_btn.setText(str(6))
        if event.key() == Qt.Key_7:
            if self.active_now_btn:
                self.active_now_btn.setText(str(7))
        if event.key() == Qt.Key_8:
            if self.active_now_btn:
                self.active_now_btn.setText(str(8))
        if event.key() == Qt.Key_9:
            if self.active_now_btn:
                self.active_now_btn.setText(str(9))

    def new_game(self):
        self.difficulty_level = None
        self.choice = QMessageBox.question(self, "", "Вы точно хотите начать новую игру?\nПрогресс предыдущей игры будет потерян.", QMessageBox.Yes | QMessageBox.No)
        if self.choice == QMessageBox.No:
            return
        self.difficulty_level, ok_pressed = QInputDialog.getItem(self, "Уровень", "Выберите уровень сложности", ("лёгкий", "средний", "сложный(на стадии тестирования)"), 1, False)
        if self.difficulty_level == "сложный(на стадии тестирования)":
            self.difficulty_level = "сложный"
        sudoku = Generation_sudoku(self.difficulty_level)  # начало генерации судоку
        sudoku.mix()
        sudoku.eating_cells()
        full_sudoku, incomplete_sudoku = sudoku.listing()  # получаем значение полного и неполного судоку
        f = open("files.txt", 'w')  # создание файла
        for i in range(9):  # запись данных о судоку
            for g in range(9):
                f.write(str(i * 9 + g))  # номер клетки начиная с 0
                f.write(" ")
                f.write(str(full_sudoku[i][g]))  # значение в полном судоку
                f.write(" ")
                f.write(str(incomplete_sudoku[i][g]))  # значение в неполном судоку
                f.write('\n')
        else:
            f.write(f'{self.difficulty_level}')
        f.close()  # закрытие файла

        f = open("files.txt", "rt")  # открытие файла файла
        values = f.readlines()
        for i in range(9):
            for j in range(9):
                value = values[i * 9 + j].split()[2]
                if value != "0":
                    self.btns[i][j].setText(value)  # присваивание каждому известному элементу значение
                else:
                    self.btns[i][j].setText("")
        f.close()  # закрытие файла
        self.active_now_btn = None
        if self.difficulty_level == "лёгкий":
            self.label_3.setText("<html><head/><body><p><span style=\" font-size:16pt;\">лёгкий</span></p></body></html>")
        elif self.difficulty_level == "средний":
            self.label_3.setText("<html><head/><body><p><span style=\" font-size:16pt;\">средний</span></p></body></html>")
        else:
            self.label_3.setText("<html><head/><body><p><span style=\" font-size:16pt;\">сложный</span></p></body></html>")

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_flag(qp)
        # Завершаем рисование
        qp.end()

    def draw_flag(self, qp):
        # Рисуем прямоугольник
        for i in range(3):
            for j in range(3):
                qp.drawRect(29 + 93 * j, 139 + 93 * i, 93, 93)

    def clean(self):
        if self.active_now_btn:
            self.active_now_btn.setText("")



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
