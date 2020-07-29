from PyQt5.Qt import *
import mianwindow


class Window(QMainWindow, mianwindow.Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("XXXX")  # change tittle
        self.resize(500, 500)
        self.setupUi(self)
    #
    # def setupUi(self):
    #     pass


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec_())
