# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QDateEdit, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1177, 822)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setContextMenuPolicy(Qt.NoContextMenu)
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.sideBar = QFrame(self.centralwidget)
        self.sideBar.setObjectName(u"sideBar")
        self.sideBar.setStyleSheet(u"")
        self.sideBar.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.sideBar)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 70, 0, 0)
        self.pushButton_driver_page = QPushButton(self.sideBar)
        self.pushButton_driver_page.setObjectName(u"pushButton_driver_page")
        self.pushButton_driver_page.setMinimumSize(QSize(200, 50))
        self.pushButton_driver_page.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.pushButton_driver_page)

        self.pushButton_car_page = QPushButton(self.sideBar)
        self.pushButton_car_page.setObjectName(u"pushButton_car_page")
        self.pushButton_car_page.setMinimumSize(QSize(200, 50))
        self.pushButton_car_page.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"font: 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.pushButton_car_page)

        self.pushButton_order_page = QPushButton(self.sideBar)
        self.pushButton_order_page.setObjectName(u"pushButton_order_page")
        self.pushButton_order_page.setMinimumSize(QSize(200, 50))
        self.pushButton_order_page.setStyleSheet(u"font: 75 10pt \"MS Shell Dlg 2\";")

        self.verticalLayout.addWidget(self.pushButton_order_page)

        self.verticalSpacer = QSpacerItem(20, 439, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.sideBar)

        self.mainInfor = QFrame(self.centralwidget)
        self.mainInfor.setObjectName(u"mainInfor")
        self.mainInfor.setFrameShape(QFrame.NoFrame)
        self.gridLayout_2 = QGridLayout(self.mainInfor)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.stackedWidget = QStackedWidget(self.mainInfor)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.page)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.title_label = QLabel(self.frame_title)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_3.addWidget(self.title_label)


        self.verticalLayout_2.addWidget(self.frame_title)

        self.frame_form = QFrame(self.page)
        self.frame_form.setObjectName(u"frame_form")
        self.frame_form.setEnabled(True)
        self.frame_form.setAutoFillBackground(False)
        self.frame_form.setFrameShape(QFrame.NoFrame)
        self.gridLayout = QGridLayout(self.frame_form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(11, 11, 11, -1)
        self.label_21 = QLabel(self.frame_form)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 3, 0, 1, 1)

        self.label = QLabel(self.frame_form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.name_driver = QLineEdit(self.frame_form)
        self.name_driver.setObjectName(u"name_driver")

        self.gridLayout.addWidget(self.name_driver, 0, 1, 1, 1)

        self.label_2 = QLabel(self.frame_form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.phone_driver = QLineEdit(self.frame_form)
        self.phone_driver.setObjectName(u"phone_driver")

        self.gridLayout.addWidget(self.phone_driver, 1, 1, 1, 1)

        self.has_car = QCheckBox(self.frame_form)
        self.has_car.setObjectName(u"has_car")
        self.has_car.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.has_car, 2, 3, 1, 1)

        self.address_driver = QLineEdit(self.frame_form)
        self.address_driver.setObjectName(u"address_driver")

        self.gridLayout.addWidget(self.address_driver, 2, 1, 1, 1)

        self.label_5 = QLabel(self.frame_form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 1, 2, 1, 1)

        self.label_4 = QLabel(self.frame_form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.cmmd_driver = QLineEdit(self.frame_form)
        self.cmmd_driver.setObjectName(u"cmmd_driver")

        self.gridLayout.addWidget(self.cmmd_driver, 0, 3, 1, 1)

        self.label_3 = QLabel(self.frame_form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.label_7 = QLabel(self.frame_form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 2, 1, 1)

        self.born_time = QDateEdit(self.frame_form)
        self.born_time.setObjectName(u"born_time")
        self.born_time.setCalendarPopup(True)

        self.gridLayout.addWidget(self.born_time, 1, 3, 1, 1)

        self.label_22 = QLabel(self.frame_form)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 3, 2, 1, 1)

        self.label_23 = QLabel(self.frame_form)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 4, 0, 1, 1)

        self.driverHasCarBienSo = QLineEdit(self.frame_form)
        self.driverHasCarBienSo.setObjectName(u"driverHasCarBienSo")
        self.driverHasCarBienSo.setEnabled(False)

        self.gridLayout.addWidget(self.driverHasCarBienSo, 3, 1, 1, 1)

        self.driverHasCarTon = QLineEdit(self.frame_form)
        self.driverHasCarTon.setObjectName(u"driverHasCarTon")
        self.driverHasCarTon.setEnabled(False)

        self.gridLayout.addWidget(self.driverHasCarTon, 3, 3, 1, 1)

        self.driverHasCarType = QComboBox(self.frame_form)
        self.driverHasCarType.setObjectName(u"driverHasCarType")
        self.driverHasCarType.setEnabled(False)

        self.gridLayout.addWidget(self.driverHasCarType, 4, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_form)

        self.frame_btn = QFrame(self.page)
        self.frame_btn.setObjectName(u"frame_btn")
        self.frame_btn.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btn)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.add_btn = QPushButton(self.frame_btn)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.add_btn)

        self.update_btn = QPushButton(self.frame_btn)
        self.update_btn.setObjectName(u"update_btn")
        self.update_btn.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.update_btn)

        self.remove_btn = QPushButton(self.frame_btn)
        self.remove_btn.setObjectName(u"remove_btn")

        self.horizontalLayout_2.addWidget(self.remove_btn)

        self.find_btn = QPushButton(self.frame_btn)
        self.find_btn.setObjectName(u"find_btn")

        self.horizontalLayout_2.addWidget(self.find_btn)

        self.refresh_btn = QPushButton(self.frame_btn)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout_2.addWidget(self.refresh_btn)


        self.verticalLayout_2.addWidget(self.frame_btn)

        self.frame_table = QFrame(self.page)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_table)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.table_result = QTableWidget(self.frame_table)
        if (self.table_result.columnCount() < 9):
            self.table_result.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_result.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_result.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_result.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.table_result.setObjectName(u"table_result")
        self.table_result.setEnabled(True)
        self.table_result.setMinimumSize(QSize(904, 465))
        self.table_result.setFocusPolicy(Qt.NoFocus)
        self.table_result.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_result.setShowGrid(True)
        self.table_result.horizontalHeader().setVisible(False)
        self.table_result.horizontalHeader().setCascadingSectionResizes(False)
        self.table_result.horizontalHeader().setMinimumSectionSize(100)
        self.table_result.horizontalHeader().setDefaultSectionSize(50)
        self.table_result.horizontalHeader().setHighlightSections(True)
        self.table_result.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_result.horizontalHeader().setStretchLastSection(False)
        self.table_result.verticalHeader().setVisible(False)
        self.table_result.verticalHeader().setCascadingSectionResizes(False)
        self.table_result.verticalHeader().setProperty("showSortIndicator", False)
        self.table_result.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_4.addWidget(self.table_result)


        self.verticalLayout_2.addWidget(self.frame_table)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_title_2 = QFrame(self.page_2)
        self.frame_title_2.setObjectName(u"frame_title_2")
        self.frame_title_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_title_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.title_label_2 = QLabel(self.frame_title_2)
        self.title_label_2.setObjectName(u"title_label_2")
        self.title_label_2.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_7.addWidget(self.title_label_2)


        self.verticalLayout_3.addWidget(self.frame_title_2)

        self.frame_form_2 = QFrame(self.page_2)
        self.frame_form_2.setObjectName(u"frame_form_2")
        self.frame_form_2.setFrameShape(QFrame.NoFrame)
        self.gridLayout_3 = QGridLayout(self.frame_form_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_12 = QLabel(self.frame_form_2)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_3.addWidget(self.label_12, 3, 2, 1, 1)

        self.car_lease_ton = QLineEdit(self.frame_form_2)
        self.car_lease_ton.setObjectName(u"car_lease_ton")

        self.gridLayout_3.addWidget(self.car_lease_ton, 2, 4, 1, 1)

        self.label_6 = QLabel(self.frame_form_2)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)

        self.car_lease_number = QLineEdit(self.frame_form_2)
        self.car_lease_number.setObjectName(u"car_lease_number")

        self.gridLayout_3.addWidget(self.car_lease_number, 0, 4, 1, 1)

        self.phone_lease = QLineEdit(self.frame_form_2)
        self.phone_lease.setObjectName(u"phone_lease")

        self.gridLayout_3.addWidget(self.phone_lease, 2, 1, 1, 1)

        self.label_8 = QLabel(self.frame_form_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_3.addWidget(self.label_8, 0, 2, 1, 1)

        self.name_lease = QLineEdit(self.frame_form_2)
        self.name_lease.setObjectName(u"name_lease")

        self.gridLayout_3.addWidget(self.name_lease, 0, 1, 1, 1)

        self.label_9 = QLabel(self.frame_form_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)

        self.label_10 = QLabel(self.frame_form_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_3.addWidget(self.label_10, 2, 2, 1, 1)

        self.label_11 = QLabel(self.frame_form_2)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)

        self.address_car_lease = QLineEdit(self.frame_form_2)
        self.address_car_lease.setObjectName(u"address_car_lease")

        self.gridLayout_3.addWidget(self.address_car_lease, 3, 1, 1, 1)

        self.car_lease_type = QComboBox(self.frame_form_2)
        self.car_lease_type.setObjectName(u"car_lease_type")

        self.gridLayout_3.addWidget(self.car_lease_type, 3, 4, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_form_2)

        self.frame_btn_2 = QFrame(self.page_2)
        self.frame_btn_2.setObjectName(u"frame_btn_2")
        self.frame_btn_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btn_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.add_btn_2 = QPushButton(self.frame_btn_2)
        self.add_btn_2.setObjectName(u"add_btn_2")

        self.horizontalLayout_5.addWidget(self.add_btn_2)

        self.update_btn_2 = QPushButton(self.frame_btn_2)
        self.update_btn_2.setObjectName(u"update_btn_2")

        self.horizontalLayout_5.addWidget(self.update_btn_2)

        self.remove_btn_2 = QPushButton(self.frame_btn_2)
        self.remove_btn_2.setObjectName(u"remove_btn_2")

        self.horizontalLayout_5.addWidget(self.remove_btn_2)

        self.find_btn_2 = QPushButton(self.frame_btn_2)
        self.find_btn_2.setObjectName(u"find_btn_2")

        self.horizontalLayout_5.addWidget(self.find_btn_2)

        self.refresh_btn_2 = QPushButton(self.frame_btn_2)
        self.refresh_btn_2.setObjectName(u"refresh_btn_2")

        self.horizontalLayout_5.addWidget(self.refresh_btn_2)


        self.verticalLayout_3.addWidget(self.frame_btn_2)

        self.frame_table_2 = QFrame(self.page_2)
        self.frame_table_2.setObjectName(u"frame_table_2")
        self.frame_table_2.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_table_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.table_result_2 = QTableWidget(self.frame_table_2)
        if (self.table_result_2.columnCount() < 6):
            self.table_result_2.setColumnCount(6)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result_2.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result_2.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result_2.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result_2.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result_2.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result_2.setHorizontalHeaderItem(5, __qtablewidgetitem14)
        self.table_result_2.setObjectName(u"table_result_2")
        self.table_result_2.setFocusPolicy(Qt.NoFocus)
        self.table_result_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_result_2.setShowGrid(True)
        self.table_result_2.setSortingEnabled(False)
        self.table_result_2.horizontalHeader().setVisible(False)
        self.table_result_2.horizontalHeader().setCascadingSectionResizes(False)
        self.table_result_2.horizontalHeader().setMinimumSectionSize(100)
        self.table_result_2.horizontalHeader().setDefaultSectionSize(50)
        self.table_result_2.horizontalHeader().setHighlightSections(True)
        self.table_result_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_result_2.horizontalHeader().setStretchLastSection(False)
        self.table_result_2.verticalHeader().setVisible(False)
        self.table_result_2.verticalHeader().setCascadingSectionResizes(False)
        self.table_result_2.verticalHeader().setProperty("showSortIndicator", False)
        self.table_result_2.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_6.addWidget(self.table_result_2)


        self.verticalLayout_3.addWidget(self.frame_table_2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_4 = QVBoxLayout(self.page_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_title_3 = QFrame(self.page_3)
        self.frame_title_3.setObjectName(u"frame_title_3")
        self.frame_title_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_title_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.title_label_3 = QLabel(self.frame_title_3)
        self.title_label_3.setObjectName(u"title_label_3")
        self.title_label_3.setStyleSheet(u"font: 75 20pt \"MS Shell Dlg 2\";")

        self.horizontalLayout_10.addWidget(self.title_label_3)


        self.verticalLayout_4.addWidget(self.frame_title_3)

        self.frame_form_3 = QFrame(self.page_3)
        self.frame_form_3.setObjectName(u"frame_form_3")
        self.frame_form_3.setFrameShape(QFrame.NoFrame)
        self.gridLayout_4 = QGridLayout(self.frame_form_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.order_need_car = QLineEdit(self.frame_form_3)
        self.order_need_car.setObjectName(u"order_need_car")

        self.gridLayout_4.addWidget(self.order_need_car, 2, 5, 1, 2)

        self.label_13 = QLabel(self.frame_form_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 2, 4, 1, 1)

        self.label_14 = QLabel(self.frame_form_3)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_4.addWidget(self.label_14, 0, 0, 1, 1)

        self.label_16 = QLabel(self.frame_form_3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_4.addWidget(self.label_16, 1, 0, 1, 2)

        self.driver_name_order = QLineEdit(self.frame_form_3)
        self.driver_name_order.setObjectName(u"driver_name_order")

        self.gridLayout_4.addWidget(self.driver_name_order, 3, 2, 1, 1)

        self.car_chose_box = QComboBox(self.frame_form_3)
        self.car_chose_box.setObjectName(u"car_chose_box")
        self.car_chose_box.setMinimumSize(QSize(250, 0))

        self.gridLayout_4.addWidget(self.car_chose_box, 3, 6, 1, 1)

        self.label_17 = QLabel(self.frame_form_3)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_4.addWidget(self.label_17, 1, 4, 1, 1)

        self.name_orderID = QLineEdit(self.frame_form_3)
        self.name_orderID.setObjectName(u"name_orderID")

        self.gridLayout_4.addWidget(self.name_orderID, 0, 2, 1, 2)

        self.label_15 = QLabel(self.frame_form_3)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_4.addWidget(self.label_15, 0, 4, 1, 1)

        self.ton_cargo = QLineEdit(self.frame_form_3)
        self.ton_cargo.setObjectName(u"ton_cargo")

        self.gridLayout_4.addWidget(self.ton_cargo, 1, 5, 1, 2)

        self.label_19 = QLabel(self.frame_form_3)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_4.addWidget(self.label_19, 3, 0, 1, 1)

        self.driver_chose_box = QComboBox(self.frame_form_3)
        self.driver_chose_box.setObjectName(u"driver_chose_box")
        self.driver_chose_box.setMinimumSize(QSize(250, 0))

        self.gridLayout_4.addWidget(self.driver_chose_box, 3, 3, 1, 1)

        self.label_20 = QLabel(self.frame_form_3)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_4.addWidget(self.label_20, 3, 4, 1, 1)

        self.order_name = QLineEdit(self.frame_form_3)
        self.order_name.setObjectName(u"order_name")

        self.gridLayout_4.addWidget(self.order_name, 2, 2, 1, 2)

        self.car_name_order = QLineEdit(self.frame_form_3)
        self.car_name_order.setObjectName(u"car_name_order")

        self.gridLayout_4.addWidget(self.car_name_order, 3, 5, 1, 1)

        self.label_18 = QLabel(self.frame_form_3)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_4.addWidget(self.label_18, 2, 0, 1, 1)

        self.time_start = QLineEdit(self.frame_form_3)
        self.time_start.setObjectName(u"time_start")

        self.gridLayout_4.addWidget(self.time_start, 1, 2, 1, 2)

        self.order_status = QLineEdit(self.frame_form_3)
        self.order_status.setObjectName(u"order_status")

        self.gridLayout_4.addWidget(self.order_status, 0, 5, 1, 2)


        self.verticalLayout_4.addWidget(self.frame_form_3)

        self.frame_btn_3 = QFrame(self.page_3)
        self.frame_btn_3.setObjectName(u"frame_btn_3")
        self.frame_btn_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_btn_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.add_btn_3 = QPushButton(self.frame_btn_3)
        self.add_btn_3.setObjectName(u"add_btn_3")

        self.horizontalLayout_8.addWidget(self.add_btn_3)

        self.update_btn_3 = QPushButton(self.frame_btn_3)
        self.update_btn_3.setObjectName(u"update_btn_3")

        self.horizontalLayout_8.addWidget(self.update_btn_3)

        self.find_btn_3 = QPushButton(self.frame_btn_3)
        self.find_btn_3.setObjectName(u"find_btn_3")

        self.horizontalLayout_8.addWidget(self.find_btn_3)

        self.refresh_btn_3 = QPushButton(self.frame_btn_3)
        self.refresh_btn_3.setObjectName(u"refresh_btn_3")

        self.horizontalLayout_8.addWidget(self.refresh_btn_3)

        self.refresh_btn_order = QPushButton(self.frame_btn_3)
        self.refresh_btn_order.setObjectName(u"refresh_btn_order")

        self.horizontalLayout_8.addWidget(self.refresh_btn_order)


        self.verticalLayout_4.addWidget(self.frame_btn_3)

        self.frame_table_3 = QFrame(self.page_3)
        self.frame_table_3.setObjectName(u"frame_table_3")
        self.frame_table_3.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_table_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.table_result_3 = QTableWidget(self.frame_table_3)
        if (self.table_result_3.columnCount() < 11):
            self.table_result_3.setColumnCount(11)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_result_3.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_result_3.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_result_3.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result_3.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result_3.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_result_3.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_result_3.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_result_3.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result_3.setHorizontalHeaderItem(8, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_result_3.setHorizontalHeaderItem(9, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.table_result_3.setHorizontalHeaderItem(10, __qtablewidgetitem25)
        self.table_result_3.setObjectName(u"table_result_3")
        self.table_result_3.setFocusPolicy(Qt.NoFocus)
        self.table_result_3.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_result_3.setShowGrid(True)
        self.table_result_3.horizontalHeader().setVisible(False)
        self.table_result_3.horizontalHeader().setCascadingSectionResizes(False)
        self.table_result_3.horizontalHeader().setMinimumSectionSize(100)
        self.table_result_3.horizontalHeader().setDefaultSectionSize(50)
        self.table_result_3.horizontalHeader().setHighlightSections(True)
        self.table_result_3.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_result_3.horizontalHeader().setStretchLastSection(False)
        self.table_result_3.verticalHeader().setVisible(False)
        self.table_result_3.verticalHeader().setCascadingSectionResizes(False)
        self.table_result_3.verticalHeader().setProperty("showSortIndicator", False)
        self.table_result_3.verticalHeader().setStretchLastSection(False)

        self.horizontalLayout_9.addWidget(self.table_result_3)


        self.verticalLayout_4.addWidget(self.frame_table_3)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.frame = QFrame(self.page_4)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-20, -10, 621, 111))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame_2 = QFrame(self.page_4)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-21, 99, 621, 71))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_3 = QFrame(self.page_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(9, 189, 561, 61))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_4 = QFrame(self.page_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(0, 260, 591, 281))
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.tableWidget_2 = QTableWidget(self.frame_4)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(60, 50, 256, 192))
        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.mainInfor)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_driver_page.setText(QCoreApplication.translate("MainWindow", u"T\u00e0i x\u1ebf", None))
        self.pushButton_car_page.setText(QCoreApplication.translate("MainWindow", u"Xe h\u00e0ng", None))
        self.pushButton_order_page.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01a1n h\u00e0ng", None))
        self.title_label.setText(QCoreApplication.translate("MainWindow", u"Trang T\u00e0i X\u1ebf", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3n s\u1ed1", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.has_car.setText(QCoreApplication.translate("MainWindow", u"c\u00f3 xe:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"CMND/CCCD", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Xe ri\u00eang", None))
        self.born_time.setDisplayFormat(QCoreApplication.translate("MainWindow", u"d/M/yyyy", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ecdng t\u1ea3i", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i xe", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"th\u00eam", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"c\u1eadp nh\u1eadt", None))
        self.remove_btn.setText(QCoreApplication.translate("MainWindow", u"x\u00f3a", None))
        self.find_btn.setText(QCoreApplication.translate("MainWindow", u"t\u00ecm ki\u1ebfm", None))
        self.refresh_btn.setText(QCoreApplication.translate("MainWindow", u"l\u00e0m m\u1edbi \u00f4 nh\u1eadp li\u1ec7u", None))
        ___qtablewidgetitem = self.table_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean", None));
        ___qtablewidgetitem1 = self.table_result.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None));
        ___qtablewidgetitem2 = self.table_result.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9", None));
        ___qtablewidgetitem3 = self.table_result.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y sinh ", None));
        ___qtablewidgetitem4 = self.table_result.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"CMND/CCCD", None));
        ___qtablewidgetitem5 = self.table_result.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"C\u00f3 xe ri\u00eang", None));
        ___qtablewidgetitem6 = self.table_result.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ecdng t\u1ea3i (t\u1ea5n)", None));
        ___qtablewidgetitem7 = self.table_result.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i xe", None));
        ___qtablewidgetitem8 = self.table_result.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3n s\u1ed1", None));
        self.title_label_2.setText(QCoreApplication.translate("MainWindow", u"Trang xe v\u1eadn t\u1ea3i", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i xe", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ee7 xe", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3n s\u1ed1", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ecdng t\u1ea3i", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9", None))
        self.add_btn_2.setText(QCoreApplication.translate("MainWindow", u"th\u00eam", None))
        self.update_btn_2.setText(QCoreApplication.translate("MainWindow", u"c\u1eadp nh\u1eadt", None))
        self.remove_btn_2.setText(QCoreApplication.translate("MainWindow", u"x\u00f3a", None))
        self.find_btn_2.setText(QCoreApplication.translate("MainWindow", u"t\u00ecm ki\u1ebfm", None))
        self.refresh_btn_2.setText(QCoreApplication.translate("MainWindow", u"l\u00e0m m\u1edbi \u00f4 nh\u1eadp li\u1ec7u", None))
        ___qtablewidgetitem9 = self.table_result_2.horizontalHeaderItem(0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean", None));
        ___qtablewidgetitem10 = self.table_result_2.horizontalHeaderItem(1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None));
        ___qtablewidgetitem11 = self.table_result_2.horizontalHeaderItem(2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0110\u1ecba ch\u1ec9", None));
        ___qtablewidgetitem12 = self.table_result_2.horizontalHeaderItem(3)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3n s\u1ed1", None));
        ___qtablewidgetitem13 = self.table_result_2.horizontalHeaderItem(4)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ecdng t\u1ea3i (t\u1ea5n)", None));
        ___qtablewidgetitem14 = self.table_result_2.horizontalHeaderItem(5)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i xe", None));
        self.title_label_3.setText(QCoreApplication.translate("MainWindow", u"Trang \u0110\u01a1n H\u00e0ng", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i b\u1ea3o qu\u1ea3n", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 \u0111\u01a1n", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y kh\u1edfi h\u00e0nh", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 l\u01b0\u1ee3ng h\u00e0ng (T\u1ea5n)", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i \u0111\u01a1n", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn t\u00e0i x\u1ebf", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Ch\u1ecdn xe", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"T\u00ean h\u00e0ng", None))
        self.add_btn_3.setText(QCoreApplication.translate("MainWindow", u"xu\u1ea5t \u0111\u01a1n", None))
        self.update_btn_3.setText(QCoreApplication.translate("MainWindow", u"c\u1eadp nh\u1eadt t\u00e0i x\u1ebf v\u00e0 xe", None))
        self.find_btn_3.setText(QCoreApplication.translate("MainWindow", u"t\u00ecm ki\u1ebfm", None))
        self.refresh_btn_3.setText(QCoreApplication.translate("MainWindow", u"l\u00e0m m\u1edbi \u00f4 nh\u1eadp li\u1ec7u", None))
        self.refresh_btn_order.setText(QCoreApplication.translate("MainWindow", u"l\u00e0m m\u1edbi b\u1ea3ng \u0111\u01a1n", None))
        ___qtablewidgetitem15 = self.table_result_3.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"M\u00e3 \u0111\u01a1n", None));
        ___qtablewidgetitem16 = self.table_result_3.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ea1ng th\u00e1i", None));
        ___qtablewidgetitem17 = self.table_result_3.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y t\u1ea1o", None));
        ___qtablewidgetitem18 = self.table_result_3.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"H\u1ecd v\u00e0 t\u00ean", None));
        ___qtablewidgetitem19 = self.table_result_3.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"S\u1ed1 \u0111i\u1ec7n tho\u1ea1i", None));
        ___qtablewidgetitem20 = self.table_result_3.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i h\u00e0ng", None));
        ___qtablewidgetitem21 = self.table_result_3.horizontalHeaderItem(6)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Ng\u00e0y kh\u1edfi h\u00e0nh", None));
        ___qtablewidgetitem22 = self.table_result_3.horizontalHeaderItem(7)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Lo\u1ea1i xe", None));
        ___qtablewidgetitem23 = self.table_result_3.horizontalHeaderItem(8)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Tr\u1ecdng t\u1ea3i (t\u1ea5n)", None));
        ___qtablewidgetitem24 = self.table_result_3.horizontalHeaderItem(9)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"T\u00e0i x\u1ebf", None));
        ___qtablewidgetitem25 = self.table_result_3.horizontalHeaderItem(10)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Bi\u1ec3n s\u1ed1 xe", None));
        ___qtablewidgetitem26 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem27 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem28 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"3", None));
    # retranslateUi

