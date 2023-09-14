import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import GUI_MainWindow
from NewGameWindow1 import Ui_NewGameWindowDialog_1
from NewGameWindow2 import Ui_NewGameWindowDialog_2
from GameStatus import GameStatus
from GameClass import GuessTheWordGame


class GuessTheWordApp2(QtWidgets.QWidget, GUI_MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.CurrentGame = None
        self.__player_set_tries = 0
        self.__user_guess = ""
        self.ui_new_window1 = None
        self.new_game_window1 = None
        self.ui_new_window2 = None
        self.new_game_window2 = None
        self.__game_status = GameStatus.NOT_STARTED
        self.ExitButton.clicked.connect(self.close)
        self.NewGameButton.clicked.connect(self.new_game_1)
        self.StopButton.clicked.connect(self.stop_game)
        self.UserInputButton.clicked.connect(self.try_user_guess)

    # make exit by esc additionally

    def closeEvent(self, event):

        reply = QtWidgets.QMessageBox()
        reply.setWindowTitle("Выход из игры")
        reply.setText("Вы уверены, что хотите выйти?")
        reply.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        reply.setDefaultButton(QtWidgets.QMessageBox.No)
        buttonY = reply.button(QtWidgets.QMessageBox.Yes)
        buttonY.setText("Да")
        buttonN = reply.button(QtWidgets.QMessageBox.No)
        buttonN.setText("Нет")
        reply.exec_()

        if reply.clickedButton() == buttonY:
            event.accept()
        elif reply.clickedButton() == buttonN:
            event.ignore()

    def new_game_1(self):
        if self.__game_status == GameStatus.IN_PROGRESS:
            self.new_game_window2 = QtWidgets.QDialog()
            self.ui_new_window2 = Ui_NewGameWindowDialog_2()
            self.ui_new_window2.setupUi(self.new_game_window2)
            self.ui_new_window2.buttonBox.accepted.connect(self.change_status)
            self.ui_new_window2.buttonBox.accepted.connect(self.new_game_1)
            self.new_game_window2.exec_()
        elif self.__game_status == GameStatus.NOT_STARTED:
            self.UserInputLineEdit.clear()
            self.new_game_window1 = QtWidgets.QDialog()
            self.ui_new_window1 = Ui_NewGameWindowDialog_1()
            self.ui_new_window1.setupUi(self.new_game_window1)
            self.ui_new_window1.NewGameButtonBox.accepted.connect(
                lambda: self.generating_word(self.ui_new_window1.spinBox.
                                             value()))
            self.new_game_window1.exec_()
            self.UserInputLineEdit.setFocus()

    def stop_game(self):
        if self.__game_status == GameStatus.IN_PROGRESS:
            stop_window_reply = QtWidgets.QMessageBox()
            stop_window_reply.setWindowTitle("Остановить игру")
            stop_window_reply.setText("Если Вы остановите игру,\n"
                                      "текущий прогресс будет потерян.\n"
                                      "Вы уверенны, что хотите остановить игру?")
            stop_window_reply.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            stop_window_reply.setDefaultButton(QtWidgets.QMessageBox.No)
            buttonY = stop_window_reply.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText("Да")
            buttonN = stop_window_reply.button(QtWidgets.QMessageBox.No)
            buttonN.setText("Нет")
            stop_window_reply.exec_()

            if stop_window_reply.clickedButton() == buttonY:
                self.change_status()

    def attention_not_abc(self):
        if self.__game_status == GameStatus.IN_PROGRESS:
            not_abc_window = QtWidgets.QMessageBox()
            not_abc_window.setText("Вы должны использовать только буквы!")
            not_abc_window.setWindowTitle("Внимание!")
            not_abc_window.setIcon(QtWidgets.QMessageBox.Warning)
            not_abc_window.setStandardButtons(QtWidgets.QMessageBox.Ok)
            not_abc_window.setDefaultButton(QtWidgets.QMessageBox.Ok)
            self.UserInputLineEdit.clear()
            self.UserInputLineEdit.setFocus()
            not_abc_window.exec_()

    def attention_number_of_letters(self):
        if self.__game_status == GameStatus.IN_PROGRESS:
            dif_letters_num_window = QtWidgets.QMessageBox()
            dif_letters_num_window.setText("Вы должны ввести слово с тем же\n"
                                           "количеством букв, что и загаданное!")
            dif_letters_num_window.setWindowTitle("Внимание!")
            dif_letters_num_window.setIcon(QtWidgets.QMessageBox.Warning)
            dif_letters_num_window.setStandardButtons(QtWidgets.QMessageBox.Ok)
            dif_letters_num_window.setDefaultButton(QtWidgets.QMessageBox.Ok)
            self.UserInputLineEdit.clear()
            self.UserInputLineEdit.setFocus()
            dif_letters_num_window.exec_()

    def attention_repeated_letter(self):
        if self.__game_status == GameStatus.IN_PROGRESS:
            repeated_latter_window = QtWidgets.QMessageBox()
            repeated_latter_window.setText("Вы уже использовали эту букву!\nПопробуйте другую")
            repeated_latter_window.setWindowTitle("Внимание!")
            repeated_latter_window.setIcon(QtWidgets.QMessageBox.Warning)
            repeated_latter_window.setStandardButtons(QtWidgets.QMessageBox.Ok)
            repeated_latter_window.setDefaultButton(QtWidgets.QMessageBox.Ok)
            self.UserInputLineEdit.clear()
            self.UserInputLineEdit.setFocus()
            repeated_latter_window.exec_()

    def attention_repeated_word(self):
        if self.__game_status == GameStatus.IN_PROGRESS:
            repeated_word_window = QtWidgets.QMessageBox()
            repeated_word_window.setText("Вы уже использовали это слово!\nПопробуйте другое")
            repeated_word_window.setWindowTitle("Внимание!")
            repeated_word_window.setIcon(QtWidgets.QMessageBox.Warning)
            repeated_word_window.setStandardButtons(QtWidgets.QMessageBox.Ok)
            repeated_word_window.setDefaultButton(QtWidgets.QMessageBox.Ok)
            self.UserInputLineEdit.clear()
            self.UserInputLineEdit.setFocus()
            repeated_word_window.exec_()

    def change_status(self):
        self.__game_status = GameStatus.NOT_STARTED
        self.MessagesTextBrowser.clear()
        self.HiddenWordLineEdit.clear()
        self.UsedLettersTextBrowser.clear()
        self.UserInputLineEdit.clear()
        self.TriesLineEdit.clear()

    def generating_word(self, player_set_tries):
        self.__player_set_tries = player_set_tries
        self.__game_status = GameStatus.IN_PROGRESS
        self.MessagesTextBrowser.append("Вы начали новую игру!!!\n"
                                        "Слово загаданно\n"
                                        "Попробуйте угадать его")
        self.CurrentGame = GuessTheWordGame(self.__player_set_tries)
        self.TriesLineEdit.setText(str(self.CurrentGame.tries_remaining))
        self.CurrentGame.word_generation()
        #self.MessagesTextBrowser.append(self.CurrentGame.generated_word)
        self.HiddenWordLineEdit.setText(self.CurrentGame.show_hidden_word())
        self.UsedLettersTextBrowser.append("Использованные буквы:\n\n\nИспользованные слова:\n")

    def win_event(self):
        if self.__game_status == GameStatus.WIN:
            win_window_reply = QtWidgets.QMessageBox()
            win_window_reply.setWindowTitle("Победа")
            win_window_reply.setText(f"Вы угадали слово!\n"
                                     f"слово было "
                                     f"'{self.CurrentGame.generated_word}'\n"
                                     f"Хотите сыграть снова?")
            win_window_reply.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            win_window_reply.setDefaultButton(QtWidgets.QMessageBox.Yes)
            buttonY = win_window_reply.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText("Да")
            buttonN = win_window_reply.button(QtWidgets.QMessageBox.No)
            buttonN.setText("Нет")
            win_window_reply.exec_()

            if win_window_reply.clickedButton() == buttonY:
                self.change_status()
                self.new_game_1()
            elif win_window_reply.clickedButton() == buttonN:
                self.change_status()
            else:
                self.change_status()
                unknown_error_window = QtWidgets.QMessageBox()
                unknown_error_window.setText("Неизвестная ошибка!")
                unknown_error_window.setWindowTitle("Внимание!")
                unknown_error_window.setIcon(QtWidgets.QMessageBox.Warning)
                unknown_error_window.setStandardButtons(QtWidgets.QMessageBox.Ok)
                unknown_error_window.setDefaultButton(QtWidgets.QMessageBox.Ok)
                unknown_error_window.exec_()

    def lose_event(self):
        if self.__game_status == GameStatus.LOST:
            lose_window_reply = QtWidgets.QMessageBox()
            lose_window_reply.setWindowTitle("Победа")
            lose_window_reply.setText(f"Вы угадали слово!\n"
                                     f"слово было "
                                     f"'{self.CurrentGame.generated_word}'\n"
                                     f"Хотите сыграть снова?")
            lose_window_reply.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            lose_window_reply.setDefaultButton(QtWidgets.QMessageBox.Yes)
            buttonY = lose_window_reply.button(QtWidgets.QMessageBox.Yes)
            buttonY.setText("Да")
            buttonN = lose_window_reply.button(QtWidgets.QMessageBox.No)
            buttonN.setText("Нет")
            lose_window_reply.exec_()

            if lose_window_reply.clickedButton() == buttonY:
                self.change_status()
                self.new_game_1()
            elif lose_window_reply.clickedButton() == buttonN:
                self.change_status()
            else:
                self.change_status()
                unknown_error_window = QtWidgets.QMessageBox()
                unknown_error_window.setText("Неизвестная ошибка!")
                unknown_error_window.setWindowTitle("Внимание!")
                unknown_error_window.setIcon(QtWidgets.QMessageBox.Warning)
                unknown_error_window.setStandardButtons(QtWidgets.QMessageBox.Ok)
                unknown_error_window.setDefaultButton(QtWidgets.QMessageBox.Ok)
                unknown_error_window.exec_()

    def check_user_word(self):
        if self.CurrentGame.word_len_check(self.__user_guess):

            check = self.CurrentGame.checking_word(self.__user_guess)
            if check == "Right word":
                self.__game_status = GameStatus.WIN
                self.UserInputLineEdit.clear()
                self.win_event()
            elif check == "Wrong word":
                self.MessagesTextBrowser.append("\nВаша догадка неверна.\n"
                                                "Попробуйте другое слово\n")
                self.TriesLineEdit.setText(str(self.CurrentGame.tries_remaining))
                self.UsedLettersTextBrowser.setText(
                    f"Использованные буквы:\n{self.CurrentGame.show_used_letters()}\n\nИспользованные слова:\n"
                    f"{self.CurrentGame.show_used_words()}")
                self.UserInputLineEdit.clear()

                if self.CurrentGame.checking_remaining_tries():
                    self.__game_status = GameStatus.IN_PROGRESS
                else:
                    self.__game_status = GameStatus.LOST
                    self.lose_event()
            elif check == "Repeated word":
                self.attention_repeated_word()

        else:
            self.attention_number_of_letters()

    def check_user_letter(self):
        check = self.CurrentGame.checking_letter(self.__user_guess)
        if check == "Wrong letter":
            self.MessagesTextBrowser.append("\nВаша догадка неверна.\n"
                                            "Попробуйте другую букву\n")
            self.TriesLineEdit.setText(str(self.CurrentGame.tries_remaining))
            self.UsedLettersTextBrowser.setText(
                f"Использованные буквы:\n{self.CurrentGame.show_used_letters()}\n\nИспользованные слова:\n"
                f"{self.CurrentGame.show_used_words()}")
            self.UserInputLineEdit.clear()
            if self.CurrentGame.checking_remaining_tries():
                self.__game_status = GameStatus.IN_PROGRESS
            else:
                self.__game_status = GameStatus.LOST
                self.lose_event()
        elif check == "Right letter":
            self.MessagesTextBrowser.append("\nВерно! Такая буква есть.\n")
            self.HiddenWordLineEdit.setText(self.CurrentGame.show_hidden_word())
            self.UsedLettersTextBrowser.setText(
                f"Использованные буквы:\n{self.CurrentGame.show_used_letters()}\n\nИспользованные слова:\n"
                f"{self.CurrentGame.show_used_words()}")
            self.UserInputLineEdit.clear()
            if self.CurrentGame.checking_win_by_letter():
                self.__game_status = GameStatus.WIN
                self.win_event()
        elif check == "Repeated letter":
            self.attention_repeated_letter()

    # make input by enter additionally
    def try_user_guess(self):

        if self.__game_status == GameStatus.IN_PROGRESS:
            self.__user_guess = self.UserInputLineEdit.text()

            if self.CurrentGame.is_player_input_correct(self.__user_guess):

                if self.CurrentGame.letter_or_word(self.__user_guess) == "word":
                    self.check_user_word()
                    self.UserInputLineEdit.setFocus()

                elif self.CurrentGame.letter_or_word(self.__user_guess) == "letter":
                    self.check_user_letter()
                    self.UserInputLineEdit.setFocus()

            else:
                self.attention_not_abc()

        elif self.__game_status == GameStatus.NOT_STARTED:
            pass
        else:
            self.MessagesTextBrowser.append("Неизвестная ошибка!")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            self.try_user_guess()

        if event.key() == Qt.Key_Q:
            self.new_game_1()

        if event.key() == Qt.Key_Escape:
            self.close()


def mainApp():
    app = QtWidgets.QApplication(sys.argv)
    window = GuessTheWordApp2()
    window.show()
    app.exec_()


if __name__ == "__main__":
    mainApp()
