from PySide6.QtCore import Slot
from PySide6.QtWidgets import (QMainWindow)

from ui.PasswordManager.ui_passwordManager_dashboard import Ui_password_manager_dashboard

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
                               QVBoxLayout, QWidget, QPushButton)
import image_rc


class MainWindow(QMainWindow):
    def __init__(self, window):
        super(MainWindow, self).__init__(window)
        print("[+] Opened Password Manager")

        self.upper_class = window
        self.Window = window.Window

    def run(self, accounts_data, main_window):
        """
        Run the app
        add elements in app
        """

        # password manager dashboard container in UI
        self.password_manager_dashboard = Ui_password_manager_dashboard()
        self.password_manager_dashboard.setupUi(self.Window.current_app_container)

        self.Window.verticalLayout_7.addWidget(self.password_manager_dashboard.password_manager_container)

        # Add item in favorite container
        self.password_manager_dashboard.label.setText("Total Account")
        # self.password_manager_dashboard.FavoriteAccounts.setText()
        # self.password_manager_dashboard.TotalAccounts.setText()
        # self.upper_class.password_manager()

        self.password_manager_dashboard.pushButton_2.clicked.connect(
            lambda: main_window.password_manager_create())

        print(f"Total {accounts_data.TotalAccounts} ")
        for account in accounts_data.AllAccounts:
            self.password_manager_dashboard.FavoriteScrollContainer.addWidget(self.addAccount(account, main_window))

    def addAccount(self, account, main_window):
        """
        adding account in list
        by getting account param
        :param account: takes account class
        :return: new account container
        """
        account_container = QWidget()
        if not account_container.objectName():
            account_container.setObjectName(u"Form" + str(account.Id()))
        font = QFont()
        font.setPointSize(14)
        account_container.resize(607, 120)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(account_container.sizePolicy().hasHeightForWidth())
        account_container.setSizePolicy(sizePolicy)
        account_container.setStyleSheet(u"background-color: rgb(51, 53, 51);")
        horizontalLayout = QHBoxLayout(account_container)
        horizontalLayout.setSpacing(20)
        horizontalLayout.setObjectName(u"horizontalLayout" + str(account.Id()))
        horizontalLayout.setContentsMargins(10, 10, 10, 10)
        label = QLabel(account_container)

        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(sizePolicy1)

        horizontalLayout.addWidget(label)

        verticalWidget = QWidget(account_container)
        verticalWidget.setObjectName(u"verticalWidget" + str(account.Id()))
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(verticalWidget.sizePolicy().hasHeightForWidth())
        verticalWidget.setSizePolicy(sizePolicy2)
        verticalLayout = QVBoxLayout(verticalWidget)
        verticalLayout.setObjectName(u"verticalLayout" + str(account.Id()))
        label_3 = QLabel(verticalWidget)
        label_3.setObjectName(u"label_3" + str(account.Id()))
        label_3.setFont(font)
        label_3.setObjectName(u"label" + str(account.Id()))

        verticalLayout.addWidget(label_3)

        label_2 = QLabel(verticalWidget)
        label_2.setObjectName(u"label_2" + str(account.Id()))

        verticalLayout.addWidget(label_2)

        open_button = QPushButton(verticalWidget)
        open_button.setObjectName(u"open_button")
        open_button.setText(u"Open")
        open_button.setFont(font)
        open_button.setStyleSheet(u"border: none;\n"
                                  u"padding: 3;\n"
                                  u"background-color: rgb(245, 203, 92);\n"
                                  u"color: rgb(51, 53, 51);")
        open_button.clicked.connect(lambda:
                                    main_window.password_manager_detail(account))

        verticalLayout.addWidget(open_button)


        horizontalLayout.addWidget(verticalWidget)

        QMetaObject.connectSlotsByName(account_container)
        label.setText(QCoreApplication.translate("Form" + str(account.Id()), u"<html><head/><body><p><img src=\":/resources/deer_logo_template_dark_flat_handdrawn_design_6854205.jpg\" wdith=\"100\" height=\"100\"/></p></body></html>", None))
        label_3.setText(QCoreApplication.translate(f"Form" + str(account.Id()), account.Platform(), None))
        label_2.setText(QCoreApplication.translate("Form" + str(account.Id()), account.Username(), None))

        return account_container
