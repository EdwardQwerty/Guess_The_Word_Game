# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NewGameWindow1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NewGameWindowDialog_1(object):
    def setupUi(self, NewGameWindowDialog_1):
        NewGameWindowDialog_1.setObjectName("NewGameWindowDialog_1")
        NewGameWindowDialog_1.setWindowModality(QtCore.Qt.WindowModal)
        NewGameWindowDialog_1.setEnabled(True)
        NewGameWindowDialog_1.resize(350, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(NewGameWindowDialog_1.sizePolicy().hasHeightForWidth())
        NewGameWindowDialog_1.setSizePolicy(sizePolicy)
        NewGameWindowDialog_1.setMinimumSize(QtCore.QSize(350, 300))
        NewGameWindowDialog_1.setMaximumSize(QtCore.QSize(350, 300))
        NewGameWindowDialog_1.setSizeGripEnabled(False)
        NewGameWindowDialog_1.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewGameWindowDialog_1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(NewGameWindowDialog_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(100, 10, 100, 10)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spinBox = QtWidgets.QSpinBox(NewGameWindowDialog_1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QtCore.QSize(50, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox.setFont(font)
        self.spinBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.spinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox.setMinimum(5)
        self.spinBox.setMaximum(15)
        self.spinBox.setProperty("value", 11)
        self.spinBox.setObjectName("spinBox")
        self.gridLayout_2.addWidget(self.spinBox, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.NewGameButtonBox = QtWidgets.QDialogButtonBox(NewGameWindowDialog_1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NewGameButtonBox.setFont(font)
        self.NewGameButtonBox.setOrientation(QtCore.Qt.Horizontal)
        self.NewGameButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.NewGameButtonBox.setCenterButtons(True)
        self.NewGameButtonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("Отмена")
        self.NewGameButtonBox.button(QtWidgets.QDialogButtonBox.Ok).setText("Ок")
        self.NewGameButtonBox.setObjectName("NewGameButtonBox")
        self.gridLayout_3.addWidget(self.NewGameButtonBox, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)

        self.retranslateUi(NewGameWindowDialog_1)
        self.NewGameButtonBox.accepted.connect(NewGameWindowDialog_1.accept) # type: ignore
        self.NewGameButtonBox.rejected.connect(NewGameWindowDialog_1.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(NewGameWindowDialog_1)

    def retranslateUi(self, NewGameWindowDialog_1):
        _translate = QtCore.QCoreApplication.translate
        NewGameWindowDialog_1.setWindowTitle(_translate("NewGameWindowDialog_1", "Новая игра"))
        self.label.setText(_translate("NewGameWindowDialog_1", "<html><head/><body><p align=\"center\">Это игра 'Угадай слово'. </p><p align=\"center\">Компьютер загадает слово и </p><p align=\"center\">Вы должны отгадать это слово </p><p align=\"center\">буква за буквой или слово целиком.</p><p align=\"center\">Но сначала задайте количество попыток </p><p align=\"center\">и нажмите \'Ок\' чтобы начать игру</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NewGameWindowDialog_1 = QtWidgets.QDialog()
    ui = Ui_NewGameWindowDialog_1()
    ui.setupUi(NewGameWindowDialog_1)
    NewGameWindowDialog_1.show()
    sys.exit(app.exec_())
