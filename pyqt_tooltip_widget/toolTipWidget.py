from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt


class ToolTipWidget(QWidget):
    def __init__(self, widget_to_set_tooltip_widget: QWidget):
        super().__init__()
        self.__initVal(widget_to_set_tooltip_widget)
        self.__initUi()

    def __initVal(self, widget_to_set_tooltip_widget):
        self.__widget_to_set_tooltip_widget = widget_to_set_tooltip_widget
        self.__obj_name = 'widgetToSetToolTipWidget'

    def __initUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)
        self.__widget_to_set_tooltip_widget.setObjectName(self.__obj_name)
        self.__widget_to_set_tooltip_widget.setMouseTracking(True)
        self.__widget_to_set_tooltip_widget.installEventFilter(self)

    def eventFilter(self, obj, e):
        if obj.objectName() == self.__obj_name:
            if e.type() == 10:
                p = self.__widget_to_set_tooltip_widget.mapToGlobal(
                    self.__widget_to_set_tooltip_widget.rect().bottomLeft())
                geo = self.geometry()
                geo.moveTopLeft(p)
                self.setGeometry(geo)
                self.show()
            elif e.type() == 11:
                self.close()
        return super().eventFilter(obj, e)