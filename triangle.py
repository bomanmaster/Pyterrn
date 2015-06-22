__author__ = 'Konrad'

from PyQt4 import QtGui, QtCore

class Toolbar(QtGui.QToolBar):

    frame = None
    color = None
    color_brush = None
    frame_brush = None
    width = 2
    style = QtCore.Qt.SolidLine
    brush = QtCore.Qt.NoBrush

    def __init__(self, view):

        QtGui.QToolBar.__init__(self)

        self.view = view
        self.toolbar_triangle()
        self.toggleViewAction().setText("Elipsa")
        self.setVisible(False)
        ikona = QtGui.QIcon("img/tools/triangle.png")
        self.toggleViewAction().setIcon(ikona)
        self.view.tool = 1


    def toolbar_triangle(self):

        col = QtGui.QColor(0, 0, 0)
        col_brush = QtGui.QColor(0, 0, 0)

        self.combo_brush = QtGui.QComboBox()
        self.combo_brush.addItem(QtGui.QIcon("img/brush/nofilling.png"), "Bez wypełnienia")
        self.combo_brush.insertSeparator(2)
        self.combo_brush.addItem(QtGui.QIcon("img/brush/filling.png"), "Pełny kolor")
        self.combo_brush.insertSeparator(4)
        self.combo_brush.addItem(QtGui.QIcon("img/brush/1.png"), "Deseń 1")
        self.combo_brush.insertSeparator(6)
        self.combo_brush.addItem(QtGui.QIcon("img/brush/2.png"), "Deseń 2")
        self.combo_brush.insertSeparator(8)
        self.combo_brush.addItem(QtGui.QIcon("img/brush/3.png"), "Deseń 3")
        self.combo_brush.insertSeparator(10)
        self.combo_brush.addItem(QtGui.QIcon("img/brush/4.png"), "Deseń 4")
        self.combo_brush.insertSeparator(12)
        self.combo_brush.addItem(QtGui.QIcon("img/brush/5.png"), "Deseń 5")
        self.combo_brush.insertSeparator(14)
        self.combo_brush.addItem(QtGui.QIcon("img/brush/6.png"), "Deseń 6")
        self.combo_brush.insertSeparator(16)
        self.combo_brush.addItem(QtGui.QIcon("img/brush/7.png"), "Deseń 7")
        self.combo_brush.setIconSize(QtCore.QSize(50, 45))
        self.combo_brush.activated[str].connect(self.brush_change)

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


        color_dialog = QtGui.QAction("Wybierz kolor linii", self)
        color_dialog.triggered.connect(self.color_change)
        self.frame = QtGui.QFrame(self)
        self.frame.setFixedSize(30, 30)
        self.frame.setStyleSheet("QWidget { background-color: %s }"
            % col.name())


        color_brush_dialog = QtGui.QAction("Wybierz kolor wypełnienia", self)
        color_brush_dialog.triggered.connect(self.color_brush_change)

        self.frame_brush = QtGui.QFrame(self)
        self.frame_brush.setFixedSize(30, 30)
        self.frame_brush.setStyleSheet("QWidget { background-color: %s }"
            % col_brush.name())


        self.addWidget(self.combo_style)
        self.addWidget(self.combo_width)
        self.addAction(color_dialog)
        self.addWidget(self.frame)
        self.addSeparator()
        self.addWidget(self.combo_brush)
        self.addAction(color_brush_dialog)
        self.addWidget(self.frame_brush)

        self.setOrientation(QtCore.Qt.Horizontal)
        self.setAllowedAreas(QtCore.Qt.TopToolBarArea)

        self.addSeparator()

        undo = QtGui.QAction(QtGui.QIcon("img/tools/undo.png"),'', self)
        undo.triggered.connect(self.view.undoStack.undo)
        self.addAction(undo)

        undo = QtGui.QAction(QtGui.QIcon("img/tools/redo.png"),'', self)
        undo.triggered.connect(self.view.undoStack.redo)
        self.addAction(undo)


    def color_change(self):

        col = QtGui.QColorDialog.getColor()
        Toolbar.color = col.name()
        if col.isValid():
            self.frame.setStyleSheet("QWidget { background-color: %s }"
                % col.name())

    def color_brush_change(self):

        col_brush = QtGui.QColorDialog.getColor()
        Toolbar.color_brush = col_brush.name()
        if col_brush.isValid():
            self.frame_brush.setStyleSheet("QWidget { background-color: %s }"
                % col_brush.name())

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

    def brush_change(self):

        if self.combo_brush.currentText() == "Bez wypełnienia":
            Toolbar.brush = QtCore.Qt.NoBrush

        elif self.combo_brush.currentText() == "Pełny kolor":
            Toolbar.brush = QtCore.Qt.SolidPattern

        elif self.combo_brush.currentText() == "Deseń 1":
            Toolbar.brush = QtCore.Qt.Dense1Pattern

        elif self.combo_brush.currentText() == "Deseń 2":
            Toolbar.brush = QtCore.Qt.Dense2Pattern

        elif self.combo_brush.currentText() == "Deseń 3":
            Toolbar.brush = QtCore.Qt.Dense3Pattern

        elif self.combo_brush.currentText() == "Deseń 4":
            Toolbar.brush = QtCore.Qt.Dense4Pattern

        elif self.combo_brush.currentText() == "Deseń 5":
            Toolbar.brush = QtCore.Qt.Dense5Pattern

        elif self.combo_brush.currentText() == "Deseń 6":
            Toolbar.brush = QtCore.Qt.CrossPattern

        elif self.combo_brush.currentText() == "Deseń 7":
            Toolbar.brush = QtCore.Qt.DiagCrossPattern
class Drawing(QtGui.QGraphicsView):

    def __init__(self):

        QtGui.QGraphicsView.__init__(self)

    def drawing(self, A1, A4, color, width, style, color_brush, brush):

        przek =(A1.x()-A4.x())**2+(A1.y()-A4.y())**2
        fg = przek**0.5
        hu = fg/2
        sqrt = 2**0.5
        print(sqrt)
        all = hu*(sqrt/2)

        a = A1
        b = QtCore.QPointF(A4.x(),A1.y())
        d = A4

        list = [a,b,d]

        self.triangle = QtGui.QGraphicsPolygonItem(QtGui.QPolygonF(list))
        self.triangle.setFlag(QtGui.QGraphicsItem.ItemIsMovable)
        self.triangle.setPen(QtGui.QPen(QtGui.QColor(str(color)), width, style))
        self.triangle.setBrush(QtGui.QBrush(QtGui.QColor(str(color_brush)), brush))
        command = Draw(self.scene, self.triangle)
        self.undoStack.push(command)


class Draw(QtGui.QUndoCommand):

    def __init__(self, scene, triangle):

        QtGui.QUndoCommand.__init__(self)
        self.scene = scene
        self.triangle = triangle

    def redo(self):
        self.scene.addItem(self.triangle)

    def undo(self):
        self.scene.removeItem(self.triangle)