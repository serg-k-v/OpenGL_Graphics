import sys  # sys нужен для передачи argv в QApplication

from PyQt5 import QtWidgets
from qt_view import design # Это наш конвертированный файл дизайна


class MainWindow(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.onActivated)

    def onActivated(self, text):
        self.openGLWidget.changeFigure(text)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = MainWindow()  # Создаём объект класса MainWindow
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
