from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt


class ToolTipWidget(QWidget):
    def __init__(self, widget_to_set_tooltip_widget: QWidget):
        super().__init__()
        self.__initVal(widget_to_set_tooltip_widget)
        self.__initUi()

    def __initVal(self, widget_to_set_tooltip_widget):
        self.__stillOpenWhenCursorLeaveFromToolTipWidget = False
        self.__tooltip_widget_name = 'toolTipWidget'

        self.__widget_to_set_tooltip_widget = widget_to_set_tooltip_widget
        self.__widget_name = 'widgetToSetToolTipWidget'

    def __initUi(self):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.SubWindow)

        self.setObjectName(self.__tooltip_widget_name)
        self.setMouseTracking(True)
        self.installEventFilter(self)

        self.__widget_to_set_tooltip_widget.setObjectName(self.__widget_name)
        self.__widget_to_set_tooltip_widget.setMouseTracking(True)
        self.__widget_to_set_tooltip_widget.installEventFilter(self)

    def isStillOpenWhenCursorLeaveFromToolTipWidget(self) -> bool:
        return self.__stillOpenWhenCursorLeaveFromToolTipWidget

    def setStillOpenWhenCursorLeaveFromToolTipWidget(self, f: bool):
        self.__stillOpenWhenCursorLeaveFromToolTipWidget = f

    def eventFilter(self, obj, e):
        if self.isStillOpenWhenCursorLeaveFromToolTipWidget():
            if obj.objectName() == self.__tooltip_widget_name or obj.objectName() == self.__widget_name:
                if obj.objectName() == self.__widget_name:
                    self.__execToolTip(e)
                else:
                    if e.type() == 10:
                        self.__show()
                    elif e.type() == 11:
                        self.close()
        else:
            if obj.objectName() == self.__widget_name:
                self.__execToolTip(e)
        return super().eventFilter(obj, e)

    def __execToolTip(self, e):
        if e.type() == 10:
            self.__show()
        elif e.type() == 11:
            self.close()
        elif e.type() == 2:
            self.close()

    def __show(self):
        p = self.__widget_to_set_tooltip_widget.mapToGlobal(
            self.__widget_to_set_tooltip_widget.rect().bottomLeft())
        geo = self.geometry()
        geo.moveTopLeft(p)
        self.setGeometry(geo)
        self.show()