# pyqt-tooltip-widget
PyQt QWidget as a tooltip

## Requirements
* PyQt5 >= 5.8

## Setup
`pip3 install git+https://github.com/yjg30737/pyqt-tooltip-widget.git --upgrade`

## Detailed Description
This is `QWidget` which is activated like tooltip. When mouse cursor enters to the widget, `ToolTipWidget` pops up at the bottom left of the widget. Leave from the widget tooltip will be disappeared.

I made it work by catching `QEnterEvent` and `QLeaveEvent` of widget.

`ToolTipWidget` inherits `QWidget`, so you can decorate it just like `QWidget`.

### Usage

Just make instance of it like `self.toolTip = ToolTipWidget(yourWidget)`. `yourWidget` argument is the widget which you want to set tooltip of. Instance should be class variable. 


## Example
Code Sample
```python
from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QPushButton, QApplication, QTextEdit, QVBoxLayout
from pyqt_tooltip_widget import ToolTipWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        btn = QPushButton('OK')
        lay = QHBoxLayout()
        lay.addWidget(btn)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        lay = QVBoxLayout()
        lay.addWidget(QTextEdit())

        self.__tooltip = ToolTipWidget(btn) # Set button's tooltip
        self.__tooltip.setFixedSize(200, 200) # Set the size
        self.__tooltip.setLayout(lay) # Set the layout of tooltip

        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    example = MainWindow()
    example.show()
    app.exec_()
```

Result

![image](https://user-images.githubusercontent.com/55078043/161880140-7cf7ad82-41f4-4046-85a9-4e7cfad2e725.png)

