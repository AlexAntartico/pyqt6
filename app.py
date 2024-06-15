from PyQt6.QtWidgets import QApplication, QtWidget

# To access cli args
import sys

# one and only one QApplication instance per application
# pass in sys.argv to the instance to allow command line args for your app
# If you know you wont use cli, QApplication([]) works too.
app = QApplication(sys.argv)

# Create a Qt widget, which will be our window
window = QWidget()
window.show()  # Windows are hidden by default

# Start event loop
app.exec()


# Your app cont reach here until you exit and the event lop has stopped