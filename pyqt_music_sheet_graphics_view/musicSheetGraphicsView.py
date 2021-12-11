from PyQt5.QtGui import QPen
from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene
from PyQt5.QtCore import Qt


class MusicSheetGraphicsView(QGraphicsView):
    MUSIC_BAR_COUNT = 5

    def __init__(self):
        super().__init__()
        self.__style_dict = {'color': Qt.black,
                             'weight': 1,
                             'x_start': 10,
                             'x_end': self.width()-10,
                             'line_height': 10}
        self.__color = Qt.black
        self.__scene = QGraphicsScene()

    def setMusicSheet(self, bar_cnt=5, bar_height=40):
        y = 10
        for i in range(bar_cnt):
            self.setMusicBar(y)
            y += (MusicSheetGraphicsView.MUSIC_BAR_COUNT * self.__style_dict['line_height'] + bar_height)

    def setMusicBar(self, y):
        self.drawLine(MusicSheetGraphicsView.MUSIC_BAR_COUNT, y)

    def drawLine(self, cnt: int, y):
        for i in range(cnt):
            self.__scene.addLine(self.__style_dict['x_start'], y, self.__style_dict['x_end'], y,
                                 QPen(self.__style_dict['color'], self.__style_dict['weight']))
            y += self.__style_dict['line_height']
        self.setScene(self.__scene)

    def resizeEvent(self, e):
        self.fitInView(self.sceneRect())