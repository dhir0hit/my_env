from PySide6.QtCore import Qt, QMetaObject
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QLabel, QMainWindow)

from ui.Dashboard import MainWindow

from ui.Dashboard.ui_container import Ui_Container
from ui.Dashboard.ui_pass_manager import Ui_password_manager_container
from utils.PasswordManager import PasswordManager

# Main window of Landing Page
# TODO: if user is not sign in show main page otherwise direct user to dashboard


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        print("[+] Opened Dashboard ... ")
        # getting mainWindow UI
        self.ui = MainWindow.ui
        self.ui.setupUi(self)
