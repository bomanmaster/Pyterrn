__author__ = 'Konrad'
import sys, line, elipse, triangle, rectangle, polygon, text
from PyQt4 import QtGui, QtCore, Qt


class Main_Window(QtGui.QMainWindow):

    def __init__(self):

        QtGui.QMainWindow.__init__(self)

        self.view = View(self)
        self.window()
        self.menu()
        self.toolbar()
        self.statusBar()
        self.setCentralWidget(self.view)
        self.tool = 0
        self.show()


    def window(self):

        screen_size = QtGui.QApplication.desktop().screenGeometry()
        self.resize(screen_size.width()/1.5, screen_size.height()/1.5)
        self.setWindowTitle("Pyttern")


    def menu(self):

        new = QtGui.QAction('Nowy',self)
        new.triggered.connect(self.file_new)

        open = QtGui.QAction('Otwórz',self)
        open.triggered.connect(self.file_open)

        save = QtGui.QAction('Zapisz',self)
        save.setEnabled(False)
        save.triggered.connect(self.file_save_changes)

        save_as = QtGui.QAction('Zapisz jako',self)
        save_as.triggered.connect(self.file_save)

        print = QtGui.QAction('Drukuj', self)
        print.triggered.connect(self.file_print)

        exit = QtGui.QAction('Zakończ',self)
        exit.triggered.connect(self.close)


        file = self.menuBar().addMenu('&Plik')
        file.addAction(new)
        file.addAction(open)
        file.addAction(save)
        file.addAction(save_as)
        file.addAction(print)
        file.addSeparator()
        file.addAction(exit)


        undo = QtGui.QAction(QtGui.QIcon("img/tools/undo.png"),'Cofnij', self)
        redo = QtGui.QAction(QtGui.QIcon("img/tools/redo.png"), 'Przywróc', self)

        self.zoom_in = QtGui.QAction(QtGui.QIcon("img/tools/zoom_in.png"), "Powiększ", self)
        self.zoom_in.triggered.connect(self.zoom_in_change)

        self.zoom_out = QtGui.QAction(QtGui.QIcon("img/tools/zoom_out.png"), "Pomniejsz", self)
        self.zoom_out.triggered.connect(self.zoom_out_change)

        self.reset_zoom = QtGui.QAction("Widok wyjściowy", self)
        self.reset_zoom.triggered.connect(self.reset_transform)

        edit = self.menuBar().addMenu("&Edycja")
        edit.addAction(undo)
        edit.addAction(redo)
        edit.addSeparator()
        edit.addAction(self.zoom_in)
        edit.addAction(self.zoom_out)
        edit.addAction(self.reset_zoom)

        self.line_toolbar = line.Toolbar(self.view)
        self.line_toggle = self.line_toolbar.toggleViewAction()
        self.line = self.addAction(self.line_toggle)
        self.line_toggle.triggered.connect(self.line_change)

        self.elipse_toolbar = elipse.Toolbar(self.view)
        self.elipse_toggle = self.elipse_toolbar.toggleViewAction()
        self.elipse = self.addAction(self.elipse_toggle)
        self.elipse_toggle.triggered.connect(self.elipse_change)

        self.triangle_toolbar = triangle.Toolbar(self.view)
        self.triangle_toggle = self.triangle_toolbar.toggleViewAction()
        self.triangle = self.addAction(self.triangle_toggle)
        self.triangle_toggle.triggered.connect(self.triangle_change)

        self.rectangle_toolbar = rectangle.Toolbar(self.view)
        self.rectangle_toggle = self.rectangle_toolbar.toggleViewAction()
        self.rectangle = self.addAction(self.rectangle_toggle)
        self.rectangle_toggle.triggered.connect(self.rectangle_change)

        self.polygon_toolbar = polygon.Toolbar(self.view)
        self.polygon_toggle = self.polygon_toolbar.toggleViewAction()
        self.polygon = self.addAction(self.polygon_toggle)
        self.polygon_toggle.triggered.connect(self.polygon_change)

        self.text_toolbar = text.Toolbar(self.view)
        self.text_toggle = self.text_toolbar.toggleViewAction()
        self.text = self.addAction(self.text_toggle)
        self.text_toggle.triggered.connect(self.text_change)

        self.pixmap = QtGui.QAction(QtGui.QIcon("img/tools/pixmap.png"), "Wstaw grafikę", self)
        self.pixmap.triggered.connect(self.insert_pixmap)

        tools = self.menuBar().addMenu("&Narzędzia")
        tools.addAction(self.line_toggle)
        tools.addAction(self.elipse_toggle)
        tools.addAction(self.triangle_toggle)
        tools.addAction(self.rectangle_toggle)
        tools.addAction(self.polygon_toggle)
        tools.addAction(self.text_toggle)
        tools.addAction(self.pixmap)

        authors = QtGui.QAction('Autorzy',self)
        self.connect(authors, QtCore.SIGNAL('triggered()'), self.showAuthors)

        python = QtGui.QAction('Python',self)
        self.connect(python, QtCore.SIGNAL('triggered()'), self.openURL_Python)

        QT = QtGui.QAction('Qt',self)
        self.connect(QT, QtCore.SIGNAL('triggered()'), self.openURL_QT)

        info = self.menuBar().addMenu("&Informacje")
        info.addAction(authors)
        info.addAction(python)
        info.addAction(QT)


    def line_change(self):
        self.tool = 1

        self.elipse_toolbar.setVisible(False)
        self.triangle_toolbar.setVisible(False)
        self.rectangle_toolbar.setVisible(False)
        self.polygon_toolbar.setVisible(False)
        self.text_toolbar.setVisible(False)

        cursor_file = "img/cursor/line_cursor.png"
        cursor = QtGui.QPixmap(cursor_file)
        self.view.setCursor(QtGui.QCursor(cursor))

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " . Klinkij LPM i przytrzymaj aby narysować linie")

    def elipse_change(self):
        self.tool = 2

        self.line_toolbar.setVisible(False)
        self.triangle_toolbar.setVisible(False)
        self.rectangle_toolbar.setVisible(False)
        self.polygon_toolbar.setVisible(False)
        self.text_toolbar.setVisible(False)

        cursor_file = "img/cursor/elipse_cursor.png"
        cursor = QtGui.QPixmap(cursor_file)
        self.view.setCursor(QtGui.QCursor(cursor))

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " . Klinkij LPM i przytrzymaj aby narysować elipse ")

    def triangle_change(self):
        self.tool = 3

        self.line_toolbar.setVisible(False)
        self.elipse_toolbar.setVisible(False)
        self.rectangle_toolbar.setVisible(False)
        self.polygon_toolbar.setVisible(False)
        self.text_toolbar.setVisible(False)

        cursor_file = "img/cursor/triangle_cursor.png"
        cursor = QtGui.QPixmap(cursor_file)
        self.view.setCursor(QtGui.QCursor(cursor))

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " . Klinkij LPM i przytrzymaj aby narysować trójkąt")


    def rectangle_change(self):
        self.tool = 4

        self.line_toolbar.setVisible(False)
        self.elipse_toolbar.setVisible(False)
        self.triangle_toolbar.setVisible(False)
        self.polygon_toolbar.setVisible(False)
        self.text_toolbar.setVisible(False)

        cursor_file = "img/cursor/rectangle_cursor.png"
        cursor = QtGui.QPixmap(cursor_file)
        self.view.setCursor(QtGui.QCursor(cursor))

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " . Klinkij LPM i przytrzymaj aby narysować prostokąt")

    def polygon_change(self):
        self.tool = 5

        self.line_toolbar.setVisible(False)
        self.elipse_toolbar.setVisible(False)
        self.triangle_toolbar.setVisible(False)
        self.rectangle_toolbar.setVisible(False)
        self.text_toolbar.setVisible(False)

        cursor_file = "img/cursor/polygon_cursor.png"
        cursor = QtGui.QPixmap(cursor_file)
        self.view.setCursor(QtGui.QCursor(cursor))

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " . Kliknij LPM i i trzymając przesuń w dół aby narysować sześciokąt")

    def text_change(self):
        self.tool = 6

        self.line_toolbar.setVisible(False)
        self.elipse_toolbar.setVisible(False)
        self.triangle_toolbar.setVisible(False)
        self.rectangle_toolbar.setVisible(False)
        self.polygon_toolbar.setVisible(False)


        cursor_file = "img/cursor/text_cursor.png"
        cursor = QtGui.QPixmap(cursor_file)
        self.view.setCursor(QtGui.QCursor(cursor))

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " . Kliknij PPM w dowolnym miejscu wprowadzenia tekstu")

    def insert_pixmap(self, start):

        self.tool = 7
        dialog = QtGui.QFileDialog()
        fname = dialog.getOpenFileName(self, "Otwórz plik")
        self.background = QtGui.QGraphicsPixmapItem(QtGui.QPixmap(fname))
        cursor_file = "img/cursor/pixmap_cursor.png"
        cursor = QtGui.QPixmap(cursor_file)
        self.view.setCursor(QtGui.QCursor(cursor))
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + " . Kliknij PPM w dowolnym miejscu wprowadzenia grafiki")

    def zoom_in_change(self):

        self.view.scale(4/3, 4/3)
        self.view.setSceneRect(QtCore.QRectF(0,0, self.view.width(), self.view.height()))

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + "")

    def zoom_out_change(self):

        # old_view_width = self.view.width()
        # old_view_height = self.view.height()
        # new_view_width = old_view_width*3/4
        # new_view_height = old_view_height*3/4

        self.view.scale(3/4, 3/4)
        # self.view.setMaximumSize(new_view_width, old_view_hei)
        self.view.setSceneRect(QtCore.QRectF(0,0, self.view.width(), self.view.height()))

        sender = self.sender()
        self.statusBar().showMessage(sender.text() + "")


    def reset_transform(self):
        self.view.resetTransform()

    # def wheelEvent(self, event):
    #
    #     zoomInFactor = 1.25
    #     zoomOutFactor = 1 / zoomInFactor
    #
    #     self.view.setTransformationAnchor(QtGui.QGraphicsView.NoAnchor)
    #     self.view.setResizeAnchor(QtGui.QGraphicsView.NoAnchor)
    #
    #     oldPos = self.view.mapToScene(event.pos())
    #
    #     if event.delta() > 0:
    #         zoomFactor = zoomInFactor
    #     else:
    #         zoomFactor = zoomOutFactor
    #     self.view.scale(zoomFactor, zoomFactor)
    #
    #     newPos = self.view.mapToScene(event.pos())
    #
    #     delta = newPos - oldPos
    #     self.view.translate(delta.x(), delta.y())
    #     self.view.setSceneRect(QtCore.QRectF(0, 0, self.view.width(), self.view.height()))


    def openURL_Python(self):

        QtGui.QDesktopServices.openUrl(QtCore.QUrl("https://www.python.org/doc/"))


    def openURL_QT(self):

        QtGui.QDesktopServices.openUrl(QtCore.QUrl("http://doc.qt.io/"))


    def showAuthors(self):

        authors = QtGui.QMessageBox()
        authors.setIcon(QtGui.QMessageBox.Information)
        authors.setWindowTitle("Autorzy")
        authors.setText("""Program wykonali:
        Monika Bogusz
        Konrad Bomanowski
        Agnieszka Chmielowiec
        Gabriela Kiszka
        """)
        authors.exec_()


    def toolbar(self):

        toolbar = QtGui.QToolBar("Tools")

        toolbar.addAction(self.line_toggle)
        self.addToolBar(self.line_toolbar)

        toolbar.addAction(self.elipse_toggle)
        self.addToolBar(self.elipse_toolbar)

        toolbar.addAction(self.triangle_toggle)
        self.addToolBar(self.triangle_toolbar)

        toolbar.addAction(self.rectangle_toggle)
        self.addToolBar(self.rectangle_toolbar)

        toolbar.addAction(self.polygon_toggle)
        self.addToolBar(self.polygon_toolbar)

        toolbar.addAction(self.text_toggle)
        self.addToolBar(self.text_toolbar)

        toolbar.addAction(self.pixmap)

        toolbar.addAction(self.zoom_in)
        self.zoom_in.setToolTip("Powiększ")

        toolbar.addAction(self.zoom_out)
        self.zoom_out.setToolTip("Pomniejsz")

        toolbar.setOrientation(QtCore.Qt.Vertical)
        toolbar.setAllowedAreas(QtCore.Qt.LeftToolBarArea)
        self.addToolBar(QtCore.Qt.LeftToolBarArea, toolbar)


    def closeEvent(self, event):

        sure_close = QtGui.QMessageBox(self)
        sure_close.setFont(QtGui.QFont("Helvetica", 10))
        sure_close.setWindowTitle("Koniec?")
        sure_close.setText("Jesteś pewien, że chcesz zakończyć program?")
        yes = sure_close.addButton("Tak", QtGui.QMessageBox.AcceptRole)
        no = sure_close.addButton("Nie", QtGui.QMessageBox.RejectRole)
        sure_close.setDefaultButton(no)
        sure_close.setVisible(True)

        if sure_close.exec_() == QtGui.QMessageBox.AcceptRole:
            event.accept()
        else:
            event.ignore()


    def file_new(self):

        save = 'Zapisz'
        discard = 'Porzuć'
        cancel = 'Anuluj'

        response = False

        new = QtGui.QMessageBox(self)
        new.setFont(QtGui.QFont("Helvetica", 10))
        new.setText('Nie zapisano zmian w pliku')
        new.setWindowTitle('Nowy')
        new.setIcon(QtGui.QMessageBox.Question)
        odp1 = new.addButton(save, QtGui.QMessageBox.AcceptRole)
        odp2 = new.addButton(discard, QtGui.QMessageBox.DestructiveRole)
        odp3 = new.addButton(cancel, QtGui.QMessageBox.RejectRole)
        new.exec_()
        response = new.clickedButton().text()
            # zapis pliku
        if response == save:
            if self.save.isEnabled():
                self.file_save_changes()

                self.view.resetTransform()
                self.view.scene.clear()
                self.save.setEnabled(False)

            else:
                self.file_save()
                if self.image.save(self.fname):
                    self.view.resetTransform()
                    self.view.scene.clear()
                self.save.setEnabled(False)

        elif response == discard:
            self.view.resetTransform()
            self.view.scene.clear()
            self.save.setEnabled(False)

    def file_open(self):

        file_name = QtGui.QFileDialog.getOpenFileName(self, "Otwórz plik")
        #f = open(fname, 'r')
        image = QtGui.QPixmap(file_name)
        background = QtGui.QGraphicsPixmapItem(image)
        background.setPos(self.view.mapToScene(0,0))
        self.view.scene.addItem(background)
        self.centralWidget().setMaximumSize(image.size())
        self.view.setSceneRect(QtCore.QRectF(0,0, image.width(), image.height()))


    def file_save(self):

        self.file_name = QtGui.QFileDialog.getSaveFileName(self, "Zapisz plik", "Nowy obraz", "Obraz jpg(*.jpg)")
        Rect = QtCore.QRect(self.view.viewport().rect())
        self.image = QtGui.QPixmap.grabWidget(self.view, Rect)
        self.image.save(self.file_name)

        if self.image.save(self.file_name):
            self.save.setEnabled(True)


    def file_save_changes(self):

        Rect = QtCore.QRect(self.view.viewport().rect())
        self.image = QtGui.QPixmap.grabWidget(self.view, Rect)
        self.image.save(self.file_name)

    def file_print(self):
        qp = QtGui.QPrintDialog(self.printer, self)
        if qp.exec_():
            painter = QtGui.QPainter(self.printer)
            painter.setRenderHint(QtGui.QPainter.Antialiasing)
            self.view.scene.render(painter)
            qp.close()


class View(QtGui.QGraphicsView):

    def __init__(self, parent):

        QtGui.QGraphicsView.__init__(self, parent)

        self.parent = parent
        self.undoStack = QtGui.QUndoStack(self)
        self.setViewportUpdateMode(4)
        self.scene = QtGui.QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRect(QtCore.QRectF(self.viewport().rect()))


    def mousePressEvent(self, event):

        if self.parent.tool >  0 and self.parent.tool < 5:
            if event.button() == QtCore.Qt.LeftButton:
                self.start = event.pos()

        elif self.parent.tool == 5:
            if event.button() == QtCore.Qt.LeftButton:
                self.A1 = event.pos()

        elif self.parent.tool == 6:
            if event.button() == QtCore.Qt.LeftButton:
                super(View, self).mousePressEvent(event)
            if event.button() == QtCore.Qt.RightButton:
                self.start = event.pos()
                self.start = QtCore.QPointF(self.mapToScene(self.start))
                item = text.Text(self.start, text.Toolbar.font, text.Toolbar.size, text.Toolbar.bold, text.Toolbar.italic, text.Toolbar.color)
                self.scene.addItem(item)

        elif self.parent.tool == 7:
            if event.button() == QtCore.Qt.LeftButton:
                super(View, self).mousePressEvent(event)
            if event.button() == QtCore.Qt.RightButton:
                self.start = event.pos()
                self.parent.background.setPos(self.start)
                self.scene.addItem(self.parent.background)

    def mouseReleaseEvent(self, event):

        if self.parent.tool == 1:
            if event.button() == QtCore.Qt.LeftButton:
                self.start = QtCore.QPointF(self.mapToScene(self.start))
                self.end = QtCore.QPointF(self.mapToScene(event.pos()))

                line.Drawing.drawing(self, self.start, self.end, line.Toolbar.color, line.Toolbar.width, line.Toolbar.style, line.Toolbar.ending)

        elif self.parent.tool == 2:
            if event.button() == QtCore.Qt.LeftButton:
                self.start = QtCore.QPointF(self.mapToScene(self.start))
                self.end = QtCore.QPointF(self.mapToScene(event.pos()))

                elipse.Drawing.drawing(self, self.start, self.end, elipse.Toolbar.color, elipse.Toolbar.width, elipse.Toolbar.style, elipse.Toolbar.color_brush, elipse.Toolbar.brush)

        elif self.parent.tool == 3:
            if event.button() == QtCore.Qt.LeftButton:
                self.start = QtCore.QPointF(self.mapToScene(self.start))
                self.end = QtCore.QPointF(self.mapToScene(event.pos()))

                triangle.Drawing.drawing(self, self.start, self.end, triangle.Toolbar.color,triangle.Toolbar.width, triangle.Toolbar.style, triangle.Toolbar.color_brush, triangle.Toolbar.brush)

        elif self.parent.tool == 4:
            if event.button() == QtCore.Qt.LeftButton:
                self.start = QtCore.QPointF(self.mapToScene(self.start))
                self.end = QtCore.QPointF(self.mapToScene(event.pos()))

                rectangle.Drawing.drawing(self, self.start, self.end, rectangle.Toolbar.color, rectangle.Toolbar.width, rectangle.Toolbar.style, rectangle.Toolbar.color_brush, rectangle.Toolbar.brush)

        elif self.parent.tool == 5:
            if event.button() == QtCore.Qt.LeftButton:
                self.A1 = QtCore.QPointF(self.mapToScene(self.A1))
                self.A4 = QtCore.QPointF(self.mapToScene(event.pos()))

                polygon.Drawing.drawing(self, self.A1, self.A4, polygon.Toolbar.color, polygon.Toolbar.width, polygon.Toolbar.style, polygon.Toolbar.color_brush, polygon.Toolbar.brush)

    def showEvent(self, event):
        self.fitInView(self.scene.sceneRect())

    def resizeEvent(self, event):
        self.update()

def Main():

    app = QtGui.QApplication(sys.argv)
    obj = Main_Window()

    sys.exit(app.exec_())


if __name__ == "__main__":
    Main()