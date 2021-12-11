import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QGraphicsScene

from pyqt_music_sheet_graphics_view.musicSheetGraphicsView import MusicSheetGraphicsView


class MusicSheetGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.__view = ''
        self.__scene = QGraphicsScene()
        self.__initUI()

    def __initUI(self):
        self.setWindowTitle('drawLine')
        layout = QGridLayout()
        self.__view = MusicSheetGraphicsView()
        self.__view.setMusicSheet()
        layout.addWidget(self.__view)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MusicSheetGenerator()
    ex.show()
    sys.exit(app.exec_())