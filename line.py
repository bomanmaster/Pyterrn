__author__ = 'Konrad'
from PyQt4 import QtGui, QtCore

class Toolbar(QtGui.QToolBar):

    frame = None
    color = None
    width = 2
    style = QtCore.Qt.SolidLine
    ending = QtCore.Qt.RoundCap

    def __init__(self, view):

        QtGui.QToolBar.__init__(self)

        self.view = view
        self.toolbar_line()
        self.toggleViewAction().setText("Linia")
        self.setVisible(False)
        ikona = QtGui.QIcon("img/tools/line.png")
        self.toggleViewAction().setIcon(ikona)
        self.view.tool = 1


    def toolbar_line(self):

        col = QtGui.QColor(0, 0, 0)

        self.combo_style = QtGui.QComboBox()
        self.combo_style.addItem(QtGui.QIcon("img/style/s1.jpg"),  "Style 1")
        self.combo_style.addItem(QtGui.QIcon("img/style/s2.jpg"), "Style 2")
        self.combo_style.addItem(QtGui.QIcon("img/style/s3.jpg"), "Style 3")
        self.combo_style.addItem(QtGui.QIcon("img/style/s4.jpg"), "Style 4")
        self.combo_style.addItem(QtGui.QIcon("img/style/s5.jpg"), "Style 5")

        self.combo_style.setIconSize(QtCore.QSize(150, 6))

        self.combo_style.activated[str].connect(self.style_change)

        self.combo_width = QtGui.QComboBox()
        self.combo_width.addItem(QtGui.QIcon("img/width/w1.jpg"), "width 1")
        self.combo_width.addItem(QtGui.QIcon("img/width/w2.jpg"), "width 2")
        self.combo_width.addItem(QtGui.QIcon("img/width/w3.jpg"), "width 3")
        self.combo_width.addItem(QtGui.QIcon("img/width/w4.jpg"), "width 4")
        self.combo_width.addItem(QtGui.QIcon("img/width/w5.jpg"), "width 5")
        self.combo_width.setIconSize(QtCore.QSize(60, 8))
        self.combo_width.activated[str].connect(self.width_change)

        self.combo_ending = QtGui.QComboBox()
        self.combo_ending.addItem(QtGui.QIcon("img/style/round.jpg"), "Round style")
        self.combo_ending.addItem(QtGui.QIcon("img/style/square.jpg"), "Square style")
        self.combo_ending.setIconSize(QtCore.QSize(60, 8))
        self.combo_ending.activated[str].connect(self.ending_change)


        color_dialog = QtGui.QAction("Wybierz Kolor", self)
        color_dialog.triggered.connect(self.color_line_change)
        self.frame = QtGui.QFrame(self)
        self.frame.setFixedSize(30, 30)
        self.frame.setStyleSheet("QWidget { background-color: %s }"
            % col.name())


        self.addWidget(self.combo_style)
        self.addWidget(self.combo_width)
        self.addWidget(self.combo_ending)
        self.addAction(color_dialog)
        self.addWidget(self.frame)

        self.setOrientation(QtCore.Qt.Horizontal)
        self.setAllowedAreas(QtCore.Qt.TopToolBarArea)

        self.addSeparator()

        undo = QtGui.QAction(QtGui.QIcon("img/tools/undo.png"),'', self)
        undo.triggered.connect(self.view.undoStack.undo)
        self.addAction(undo)

        undo = QtGui.QAction(QtGui.QIcon("img/tools/redo.png"),'', self)
        undo.triggered.connect(self.view.undoStack.redo)
        self.addAction(undo)



    def color_line_change(self):

        col = QtGui.QColorDialog.getColor()
        Toolbar.color = col.name()
        if col.isValid():
            self.frame.setStyleSheet("QWidget { background-color: %s }"
                % col.name())

    def width_change(self):

        if self.combo_width.currentText() == "width 1":
            Toolbar.width = 2
        elif self.combo_width.currentText() == "width 2":
            Toolbar.width = 4
        elif self.combo_width.currentText() == "width 3":
            Toolbar.width = 6
        elif self.combo_width.currentText() == "width 4":
            Toolbar.width = 9
        else:
            Toolbar.width = 12



    def style_change(self):

        if self.combo_style.currentText() == "Style 1":
            Toolbar.style = QtCore.Qt.SolidLine

        elif self.combo_style.currentText() == "Style 2":
            Toolbar.style = QtCore.Qt.DashLine

        elif self.combo_style.currentText() == "Style 3":
            Toolbar.style = QtCore.Qt.DashDotLine

        elif self.combo_style.currentText() == "Style 4":
            Toolbar.style = QtCore.Qt.DotLine

        else:
            Toolbar.style = QtCore.Qt.DashDotDotLine

    def ending_change(self):

        if self.combo_ending.currentText() == "Round style":
            Toolbar.ending = QtCore.Qt.RoundCap
        else:
            Toolbar.ending = QtCore.Qt.SquareCap

class Drawing(QtGui.QGraphicsView):

    def __init__(self):

        QtGui.QGraphicsView.__init__(self)

    def drawing(self, start, end, color, width_line, style, ending):

        self.line = QtGui.QGraphicsLineItem(QtCore.QLineF(start, end))
        self.line.setPen(QtGui.QPen(QtGui.QColor(str(color)), width_line, style, ending))
        command = Draw(self.scene, self.line)
        self.undoStack.push(command)


class Draw(QtGui.QUndoCommand):

    def __init__(self, scene, line):

        QtGui.QUndoCommand.__init__(self)
        self.scene = scene
        self.line = line

    def redo(self):
        self.scene.addItem(self.line)

    def undo(self):
        self.scene.removeItem(self.line)