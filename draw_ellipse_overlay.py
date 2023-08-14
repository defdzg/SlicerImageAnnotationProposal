import slicer
from PythonQt import QtCore, QtGui

# Custom overlay widget class
class OverlayWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        super(OverlayWidget, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowStaysOnTopHint)
        self.button_position = None

    def setButtonPosition(self, position):
        self.button_position = position
        self.update()

    def paintEvent(self, event):
        if self.button_position is None:
            return

        # Create a painter for the overlay widget
        painter = QtGui.QPainter(self)

        # Set rendering options and pen properties
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setPen(QtGui.QPen(QtGui.QColor("red"), 2))

        # Draw a red dot at the button position
        painter.drawEllipse(self.button_position, 10, 10)

        painter.end()

# Create an instance of the overlay widget
overlayWidget = OverlayWidget()

# Show the overlay widget
overlayWidget.show()

# Find the button by its object name
button = slicer.util.findChildren(slicer.util.mainWindow(), "OpenExtensionsManagerButton")[0]

# Connect the button's pressed signal to the overlay widget's setButtonPosition method
button.connect('pressed()', overlayWidget.setButtonPosition)

# Position the overlay widget over the main window
mainWindow = slicer.util.mainWindow()
overlayWidget.setGeometry(mainWindow.frameGeometry())
