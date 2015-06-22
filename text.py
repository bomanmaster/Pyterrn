__author__ = 'Konrad'


from PyQt4 import QtGui, QtCore

class Toolbar(QtGui.QToolBar):

    frame = None
    font = None
    bold = -1
    italic = False
    size = 14
    color = QtGui.QColor("black")

    def __init__(self, view):

        QtGui.QToolBar.__init__(self)

        self.view = view
        self.toggleViewAction().setText("abra")
        self.setVisible(False)
        icon = QtGui.QIcon("img/tools/text.png")
        self.toggleViewAction().setIcon(icon)
        self.toolbar_line()

    def toolbar_line(self):

        col = QtGui.QColor(0, 0, 0)


        self.combo_font = QtGui.QFontComboBox()

        self.combo_font.activated[str].connect(self.font_change)

        self.combo_size = QtGui.QComboBox()
        self.combo_size.addItem("8")
        self.combo_size.addItem("10")
        self.combo_size.addItem("12")
        self.combo_size.addItem("14")
        self.combo_size.addItem("16")
        self.combo_size.addItem("18")
        self.combo_size.addItem("20")
        self.combo_size.addItem("22")
        self.combo_size.addItem("24")
        self.combo_size.addItem("26")

        self.combo_size.activated[str].connect(self.size_change)

        self.cb_bold = QtGui.QCheckBox("Pogrubienie")
        self.cb_bold.stateChanged.connect(self.bold_change)
        self.cb_italic = QtGui.QCheckBox("Pochylenie")
        self.cb_italic.stateChanged.connect(self.italic_change)
        #self.cb_underline =QtGui.QCheckBox("Podkreślenie")
        #self.cb_underline.stateChanged.connect(self.underlinie)

        color_dialog = QtGui.QAction("Wybierz Kolor", self)
        color_dialog.triggered.connect(self.color_change)
        self.frame = QtGui.QFrame(self)
        self.frame.setFixedSize(40, 40)
        self.frame.setStyleSheet("QWidget { background-color: %s }"
            % col.name())

        self.addWidget(self.combo_font)
        self.addWidget(self.combo_size)
        self.addWidget(self.cb_bold)
        self.addWidget(self.cb_italic)
        #self.addWidget(self.cb_underline)

        self.addAction(color_dialog)
        self.addWidget(self.frame)

        self.setOrientation(QtCore.Qt.Horizontal)
        self.setAllowedAreas(QtCore.Qt.TopToolBarArea)
        #toolbar_position = self.addToolBar(QtCore.Qt.TopToolBarArea, toolbar_line)


    def color_change(self):

        col = QtGui.QColorDialog.getColor()
        Toolbar.color = col.name()
        if col.isValid():
            self.frame.setStyleSheet("QWidget { background-color: %s }"
                % col.name())

    def font_change(self):

        Toolbar.font = self.combo_font.currentText()



    def size_change(self):

        if self.combo_size.currentText() == "8":
            Toolbar.size = 8
        if self.combo_size.currentText() == "10":
            Toolbar.size = 10
        if self.combo_size.currentText() == "12":
            Toolbar.size = 12
        if self.combo_size.currentText() == "14":
            Toolbar.size = 14
        if self.combo_size.currentText() == "16":
            Toolbar.size = 16
        if self.combo_size.currentText() == "18":
            Toolbar.size = 18
        if self.combo_size.currentText() == "20":
            Toolbar.size = 20
        if self.combo_size.currentText() == "22":
            Toolbar.size = 22
        if self.combo_size.currentText() == "24":
            Toolbar.size = 24
        if self.combo_size.currentText() == "26":
            Toolbar.size = 26

    def bold_change(self, state):
        if state == QtCore.Qt.Checked:
            Toolbar.bold = 75
        else:
            Toolbar.bold = -1

    def italic_change(self, state):
        if state == QtCore.Qt.Checked:
            Toolbar.italic = True
        else:
            Toolbar.italic = False


class Text(QtGui.QGraphicsTextItem):
        def __init__(self, start, font, size, bold, italic, color):
                QtGui.QGraphicsTextItem.__init__(self)

                self.setSelected(True)
                self.setAcceptDrops(True)
                self.setFlag(QtGui.QGraphicsItem.ItemIsFocusable)
                self.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
                self.setFlag(QtGui.QGraphicsItem.ItemIsSelectable)
                self.setTextInteractionFlags(QtCore.Qt.TextEditable)

                self.setPlainText("Wpisz dowolny tekst")

                self.setZValue(20.20)
                self.setPos(start)
                self.setFont(QtGui.QFont(font, size, bold, italic))
                self.setVisible(True)
                self.setDefaultTextColor(QtGui.QColor(str(color)))
                kursor = QtGui.QCursor()
                self.setCursor(kursor)


class Draw(QtGui.QUndoCommand):

    def __init__(self, scene, text):

        QtGui.QUndoCommand.__init__(self)
        self.scene = scene
        self.text = text

    def redo(self):
        self.scene.addItem(self.text)

    def undo(self):
        self.scene.removeItem(self.text)