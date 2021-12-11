# pyqt-music-sheet-graphics-view
PyQt music sheet graphics view (only music sheet lines exist currently)

## Requirements
PyQt5 >= 5.8

## Setup
```pip3 install git+https://github.com/yjg30737/pyqt-music-sheet-graphics-view.git --upgrade```

## Feature
* Using ```setMusicSheet(bars_group_cnt: int = 5, bars_group_height: int = 40)``` to set the count and height of group of bars.

## Example
Code Example
```python
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout
from pyqt_music_sheet_graphics_view.musicSheetGraphicsView import MusicSheetGraphicsView


class MusicSheetGenerator(QWidget):

    def __init__(self):
        super().__init__()
        self.__view = ''
        self.__initUI()

    def __initUI(self):
        self.__view = MusicSheetGraphicsView()
        self.__view.setMusicSheet()
        lay = QGridLayout()
        lay.addWidget(self.__view)

        self.setLayout(lay)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MusicSheetGenerator()
    ex.show()
    sys.exit(app.exec_())
```

Result

![image](https://user-images.githubusercontent.com/55078043/145660347-15db1e78-8925-4e28-90ce-39938bae295c.png)
