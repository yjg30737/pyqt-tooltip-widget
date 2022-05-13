# pyqt-tooltip-widget
PyQt QWidget as a tooltip

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-tooltip-widget`

## Detailed Description
This is `QWidget` which is activated like tooltip. When mouse cursor enters to the widget, `ToolTipWidget` pops up at the bottom left of the widget. Leave from the widget tooltip will be disappeared.

I made it work by catching `QEnterEvent` and `QLeaveEvent` of widget.

`ToolTipWidget` inherits `QWidget`, so you can decorate it just like `QWidget`.

### Usage

Just make instance of it like `self.toolTip = ToolTipWidget(yourWidget)`. `yourWidget` argument is the widget which you want to set tooltip of. Instance should be class variable.

### Method Overview
* `setStillOpenWhenCursorLeaveFromToolTipWidget(f: bool)` - Tooltip will be kept showing when cursor is inside the tooltip. (this is disabled by default) 
* `isStillOpenWhenCursorLeaveFromToolTipWidget() -> bool`

## Example
Code Sample
```python
from PyQt5.QtWidgets import QWidget, QMainWindow, QHBoxLayout, QPushButton, QApplication, QVBoxLayout
from pyqt_date_table_widget import DateTableWidget
from pyqt_tooltip_widget import ToolTipWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.__initUi()

    def __initUi(self):
        btn = QPushButton('Show Date Table Widget')
        lay = QHBoxLayout()
        lay.addWidget(btn)

        mainWidget = QWidget()
        mainWidget.setLayout(lay)

        ### Make tooltip start ###
        dateTableWidget = DateTableWidget() # https://github.com/yjg30737/pyqt-date-table-widget.git
        lay = QVBoxLayout()
        lay.addWidget(dateTableWidget)
        lay.setContentsMargins(0, 0, 0, 0)

        self.__tooltip = ToolTipWidget(btn)
        self.__tooltip.setFixedSize(200, 200)
        self.__tooltip.setLayout(lay)
        ### Make tooltip end ###

        self.setCentralWidget(mainWidget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    example = MainWindow()
    example.show()
    app.exec_()

```

Result

![image](https://user-images.githubusercontent.com/55078043/161909861-a724e0c5-4b16-4fa0-ab0b-7144b1386d82.png)

