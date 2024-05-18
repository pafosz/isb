# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab4.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from modules import work_with_files, number_card
import multiprocessing as mp


class CardSelectionWindow(QtWidgets.QMainWindow):
    """
    A window for selecting a card by hash value.

    This class provides a user interface for entering a hash value, selecting a file with bin numbers,
    and entering the last four digits of a card number. It then uses the `select_card_number` function
    from the `number_card` module to search for a matching card number and displays the result.
    """
    def __init__(self, parent=None):
        """
        Initializes the CardSelectionWindow.

        Args:
            parent (QWidget, optional): The parent widget of this window.
        """
        super().__init__(parent)
        self.setWindowTitle("Подбор карты по хешу")
        self.setGeometry(100, 100, 400, 300)

        self.centralwidget = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.hash_label = QtWidgets.QLabel("Введите хэш:")
        self.hash_label.setStyleSheet("color: rgb(16, 243, 0);")
        self.hash_input = QtWidgets.QLineEdit()
        self.hash_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.layout.addWidget(self.hash_label)
        self.layout.addWidget(self.hash_input)

        self.file_label = QtWidgets.QLabel("Выберите файл с бинами:")
        self.file_label.setStyleSheet("color: rgb(16, 243, 0);")
        self.file_input = QtWidgets.QLineEdit()
        self.file_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.file_button = QtWidgets.QPushButton("Выбрать файл")
        self.file_button.setStyleSheet("""
            QPushButton {
                color: rgb(221, 221, 221);
                background-color: rgb(89, 0, 221);
            }
            QPushButton:hover {
                background-color: rgb(139, 0, 255);
            }
        """)
        self.file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.file_label)
        self.layout.addWidget(self.file_input)
        self.layout.addWidget(self.file_button)

        self.card_label = QtWidgets.QLabel(
            "Введите последние 4 цифры номера карты:")
        self.card_label.setStyleSheet("color: rgb(16, 243, 0);")
        self.card_input = QtWidgets.QLineEdit()
        self.card_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.layout.addWidget(self.card_label)
        self.layout.addWidget(self.card_input)

        self.submit_button = QtWidgets.QPushButton("Подобрать карту")
        self.submit_button.setStyleSheet("""
            QPushButton {
                color: rgb(221, 221, 221);
                background-color: rgb(89, 0, 221);
            }
            QPushButton:hover {
                background-color: rgb(139, 0, 255);
            }
        """)
        self.submit_button.clicked.connect(self.search_card)
        self.layout.addWidget(self.submit_button)

        self.setCentralWidget(self.centralwidget)

    def select_file(self):
        """
        Opens a file dialog to select a file with bin numbers.

        The selected file path is then displayed in the file input field.
        """
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setNameFilter("File with bins (*.txt)")
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.file_input.setText(selected_file)

    def search_card(self):
        """
        Searches for a card number that matches the given hash and last four digits.

        The function reads the bin numbers from the selected file, and then calls the `select_card_number`
        function from the `number_card` module to search for a matching card number. The result is
        displayed in a message box.
        """
        hash_value = self.hash_input.text()
        file_path = self.file_input.text()
        bins = work_with_files.read_txt(file_path)
        last_digits = self.card_input.text()

        progress_dialog = QtWidgets.QProgressDialog("Идёт подбор карты...",
                                                    "Отмена", 0, 100, self)
        progress_dialog.setWindowTitle("Поиск карты")
        progress_dialog.setWindowModified(QtCore.Qt.ApplicationModal)
        progress_dialog.setGeometry(100, 100, 500, 150)
        progress_dialog.show()

        card_number = number_card.select_card_number(hash_value, int(last_digits),
                                                     bins, mp.cpu_count())

        if card_number:
            progress_dialog.close()
            result_dialog = QtWidgets.QMessageBox()
            result_dialog.setWindowTitle("Результат поиска")
            result_dialog.setText(f"Найденный номер карты: {card_number}")
            result_dialog.exec_()
        else:
            progress_dialog.close()
            result_dialog = QtWidgets.QMessageBox()
            result_dialog.setWindowTitle("Результат поиска")
            result_dialog.setText("Не удалось найти карту.")
            result_dialog.exec_()

        progress_dialog.close()


class CardValidationWindow(QtWidgets.QMainWindow):
    """
    A window for validating a credit card number.

    This class provides a user interface for entering a credit card number and displays
    whether the number is valid or not based on the Luhn algorithm.
    """
    def __init__(self, parent=None):
        """
        Initializes the CardValidationWindow.

        Args:
            parent (QWidget, optional): The parent widget of this window.
        """
        super().__init__(parent)
        self.setWindowTitle("Проверка корректности номера карты")
        self.setGeometry(100, 100, 400, 200)

        self.centralwidget = QtWidgets.QWidget(self)
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.card_label = QtWidgets.QLabel("Введите номер карты:")
        self.card_label.setStyleSheet("color: rgb(16, 243, 0);")
        self.card_input = QtWidgets.QLineEdit()
        self.card_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.card_input.textChanged.connect(self.validate_card_number)
        self.layout.addWidget(self.card_label)
        self.layout.addWidget(self.card_input)

        self.result_label = QtWidgets.QLabel()
        self.result_label.setStyleSheet("color: rgb(255, 0, 0);")
        self.layout.addWidget(self.result_label)

        self.setCentralWidget(self.centralwidget)

    def validate_card_number(self):
        """
        Validates the credit card number entered by the user.

        The function checks if the length of the card number is 16 and if the number is valid
        according to the Luhn algorithm. The result is displayed in a label.
        """
        card_number = self.card_input.text()
        if len(card_number) == 16 and number_card.algorithm_Luna(card_number):
            self.result_label.setText("Номер карты введен корректно")
            self.result_label.setStyleSheet("color: rgb(16, 243, 0);")
        else:
            self.result_label.setText("Номер карты введен некорректно")
            self.result_label.setStyleSheet("color: rgb(255, 0, 0);")


class SearchTimeWindow(QtWidgets.QMainWindow):
    """
    A window for measuring the time it takes to search for a collision.

    This class provides a user interface for entering a hash value, selecting a file with bin numbers,
    and entering the last four digits of a card number. It then calls the `time_to_search_for_collision`
    function from the `number_card` module to measure the time it takes to search for a matching card
    number using different numbers of CPU processes.
    """
    def __init__(self, parent=None):
        """
        Initializes the SearchTimeWindow.

        Args:
            parent (QWidget, optional): The parent widget of this window.
        """
        super().__init__(parent)
        self.setGeometry(100, 100, 400, 300)

        self.centralwidget = QtWidgets.QWidget(self)
        self.setWindowTitle("Узнать время поиска коллизии")
        self.layout = QtWidgets.QVBoxLayout(self.centralwidget)

        self.hash_label = QtWidgets.QLabel("Введите хэш: ")
        self.hash_label.setStyleSheet("color: rgb(16, 243, 0);")
        self.hash_input = QtWidgets.QLineEdit()
        self.hash_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.layout.addWidget(self.hash_label)
        self.layout.addWidget(self.hash_input)

        self.file_label = QtWidgets.QLabel("Выберите файл с бинами: ")
        self.file_label.setStyleSheet("color: rgb(16, 243, 0);")
        self.file_input = QtWidgets.QLineEdit()
        self.file_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.file_button = QtWidgets.QPushButton("Выбрать файл")
        self.file_button.setStyleSheet("""
            QPushButton {
                color: rgb(221, 221, 221);
                background-color: rgb(89, 0, 221);
            }
            QPushButton:hover {
                background-color: rgb(139, 0, 255);
            }
        """)
        self.file_button.clicked.connect(self.select_file)
        self.layout.addWidget(self.file_label)
        self.layout.addWidget(self.file_input)
        self.layout.addWidget(self.file_button)

        self.card_label = QtWidgets.QLabel(
            "Введите последние 4 цифры номера карты:")
        self.card_label.setStyleSheet("color: rgb(16, 243, 0);")
        self.card_input = QtWidgets.QLineEdit()
        self.card_input.setStyleSheet("color: rgb(255, 255, 255);")
        self.layout.addWidget(self.card_label)
        self.layout.addWidget(self.card_input)

        self.submit_button = QtWidgets.QPushButton("Узнать время поиска")
        self.submit_button.setStyleSheet("""
            QPushButton {
                color: rgb(221, 221, 221);
                background-color: rgb(89, 0, 221);
            }
            QPushButton:hover {
                background-color: rgb(139, 0, 255);
            }
        """)
        self.submit_button.clicked.connect(self.time_to_search_for_collision)
        self.layout.addWidget(self.submit_button)

        self.setCentralWidget(self.centralwidget)

    def select_file(self):
        """
        Opens a file dialog to select a file with bin numbers.

        The selected file path is then displayed in the file input field.
        """
        file_dialog = QtWidgets.QFileDialog()
        file_dialog.setNameFilter("File with bins (*.txt)")
        if file_dialog.exec_():
            selected_file = file_dialog.selectedFiles()[0]
            self.file_input.setText(selected_file)

    def time_to_search_for_collision(self):
        """
        Measures the time it takes to search for a collision.

        The function reads the bin numbers from the selected file, and then calls the
        `time_to_search_for_collision` function from the `number_card` module to measure
        the time it takes to search for a matching card number using different numbers of
        CPU processes. The results are then displayed in a plot.
        """
        hash_value = self.hash_input.text()
        file_path = self.file_input.text()
        bins = work_with_files.read_txt(file_path)
        last_digits = self.card_input.text()

        progress_dialog = QtWidgets.QProgressDialog("Идёт поиск коллизии...",
                                                    "Отмена", 0, 100, self)
        progress_dialog.setWindowTitle("Поиск коллизии")
        progress_dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        progress_dialog.setGeometry(100, 100, 500, 150)
        progress_dialog.show()

        number_card.time_to_search_for_collision(hash_value, last_digits,
                                                 bins)


class Ui_CardSelectionAssistant(object):
    """
    The main user interface for the Card Selection Assistant application.

    This class sets up the main window of the application, including the layout and three
    buttons for the different functionalities: card selection, card validation, and search
    time measurement.
    """
    def setupUi(self, CardSelectionAssistant):
        """
        Sets up the user interface for the Card Selection Assistant application.

        Args:
            CardSelectionAssistant (QMainWindow): The main window of the application.
        """
        CardSelectionAssistant.setObjectName("CardSelectionAssistant")
        CardSelectionAssistant.resize(420, 410)
        CardSelectionAssistant.setStyleSheet(
            "background-color: rgb(58, 58, 58);")
        self.centralwidget = QtWidgets.QWidget(CardSelectionAssistant)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 411, 61))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(20, 90, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn1.setFont(font)
        self.btn1.setStyleSheet("""
            QPushButton {
                color: rgb(221, 221, 221);
                background-color: rgb(89, 0, 221);
            }
            QPushButton:hover {
                background-color: rgb(139, 0, 255);
            }
        """)
        self.btn1.setObjectName("btn1")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(20, 180, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn2.setFont(font)
        self.btn2.setStyleSheet("""
            QPushButton {
                color: rgb(221, 221, 221);
                background-color: rgb(89, 0, 221);
            }
            QPushButton:hover {
                background-color: rgb(139, 0, 255);
            }
        """)
        self.btn2.setObjectName("btn2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(20, 270, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btn3.setFont(font)
        self.btn3.setStyleSheet("""
            QPushButton {
                color: rgb(221, 221, 221);
                background-color: rgb(89, 0, 221);
            }
            QPushButton:hover {
                background-color: rgb(139, 0, 255);
            }
        """)
        self.btn3.setObjectName("btn3")
        self.label.raise_()
        self.btn2.raise_()
        self.btn3.raise_()
        self.btn1.raise_()
        CardSelectionAssistant.setCentralWidget(self.centralwidget)
        self.Assistant = QtWidgets.QMenuBar(CardSelectionAssistant)
        self.Assistant.setGeometry(QtCore.QRect(0, 0, 420, 26))
        self.Assistant.setObjectName("Assistant")
        CardSelectionAssistant.setMenuBar(self.Assistant)
        self.statusbar = QtWidgets.QStatusBar(CardSelectionAssistant)
        self.statusbar.setObjectName("statusbar")
        CardSelectionAssistant.setStatusBar(self.statusbar)

        self.retranslateUi(CardSelectionAssistant)
        QtCore.QMetaObject.connectSlotsByName(CardSelectionAssistant)
        self.btn1.clicked.connect(self.open_card_selection_window)
        self.btn2.clicked.connect(self.open_card_validation_window)
        self.btn3.clicked.connect(self.open_search_time_window)

    def retranslateUi(self, CardSelectionAssistant):
        """
        Translates the user interface text to the desired language.

        Args:
            CardSelectionAssistant (QMainWindow): The main window of the application.
        """
        _translate = QtCore.QCoreApplication.translate
        CardSelectionAssistant.setWindowTitle(_translate(
            "CardSelectionAssistant", "Помощник по подбору карты"))
        self.label.setText(_translate("CardSelectionAssistant",
                           "Выберите режим работы приложения"))
        self.btn1.setWhatsThis(_translate(
            "CardSelectionAssistant", "<html><head/><body><p><br/></p></body></html>"))
        self.btn1.setText(_translate(
            "CardSelectionAssistant", "Подбор карты по хешу"))
        self.btn2.setText(_translate("CardSelectionAssistant",
                          "Проверка корректности номера карты"))
        self.btn3.setText(_translate("CardSelectionAssistant",
                          "Узнать время поиска коллизии"))

    def open_card_selection_window(self):
        """
        Opens the Card Selection Window.
        """
        self.card_selection_window = CardSelectionWindow(
            CardSelectionAssistant)
        self.card_selection_window.show()

    def open_card_validation_window(self):
        """
        Opens the Card Validation Window.
        """
        self.open_card_validation_window = CardValidationWindow(
            CardSelectionAssistant)
        self.open_card_validation_window.show()

    def open_search_time_window(self):
        """
        Opens the Search Time Window.
        """
        self.search_time_window = SearchTimeWindow(CardSelectionAssistant)
        self.search_time_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CardSelectionAssistant = QtWidgets.QMainWindow()
    ui = Ui_CardSelectionAssistant()
    ui.setupUi(CardSelectionAssistant)
    CardSelectionAssistant.show()
    sys.exit(app.exec_())
