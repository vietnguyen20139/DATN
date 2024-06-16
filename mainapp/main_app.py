
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFrame, QMessageBox, QTableWidgetItem, QTableView, QTableWidget, QHeaderView
from PySide6.QtCore import QFile, QDate
from ui_main import Ui_MainWindow
import connect_firebase
import test_word

class Driver:
    def __init__(self, name, phone, cccd, borntime, address, hascar, driver_own_car_name, driver_own_car_type, driver_own_car_ton):
        self.name = name
        self.phone = phone
        self.cccd = cccd
        self.borntime = borntime
        self.address = address
        self.hascar = hascar
        self.driver_own_car_name = driver_own_car_name
        self.driver_own_car_type = driver_own_car_type
        self.driver_own_car_ton = driver_own_car_ton
    
    def get_info_driver(self):
        return [
            self.name,
            self.phone,
            self.address,
            self.borntime,
            self.cccd,
            str("có xe" if self.hascar else "không xe"),
            self.driver_own_car_ton,
            self.driver_own_car_type,
            self.driver_own_car_name
        ]


class Lease:
    def __init__(self, name, phone, address, lease_own_car_name, lease_own_car_type, lease_own_car_ton):
        self.name = name
        self.phone = phone
        self.address = address
        self.lease_own_car_name = lease_own_car_name
        self.lease_own_car_type = lease_own_car_type
        self.lease_own_car_ton = lease_own_car_ton
    
    def get_info_lease(self):
        return [
            self.name,
            self.phone,
            self.address,
            self.lease_own_car_name,
            self.lease_own_car_ton,
            self.lease_own_car_type
        ]


class Order:
    def __init__(self, orderID, status):
        self.order_id = orderID
        self.status = status
    
    def get_info_order(self):
        return [
            self.order_id,
            self.status
        ]
        
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.stacked_widget = self.ui.stackedWidget

        self.switch_btn_page1 = self.ui.pushButton_driver_page
        self.switch_btn_page2 = self.ui.pushButton_car_page
        self.switch_btn_page3 = self.ui.pushButton_order_page

        # Connect button clicks to switch pages
        self.switch_btn_page1.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(0))
        self.switch_btn_page2.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        self.switch_btn_page3.clicked.connect(self.switchToOrderPage)

        ########################### 3 table config
        # set header of 3 table is visible
        self.driver_table = self.ui.table_result
        self.car_lease_table = self.ui.table_result_2
        self.order_table = self.ui.table_result_3
        
        # set when click select on row then highlight that row
        self.driver_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.car_lease_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.order_table.setSelectionBehavior(QTableWidget.SelectRows)
        
        # call function when click row in table
        self.driver_table.clicked.connect(self.show_data_from_table_to_form_driver)
        self.car_lease_table.clicked.connect(self.show_data_from_table_to_form_lease)
        self.order_table.clicked.connect(self.show_data_to_form_order)

        # set 3 table can sorting but cannot modify
        self.driver_table.setSortingEnabled(True)
        self.driver_table.setEditTriggers(QTableView.NoEditTriggers)

        self.car_lease_table.setSortingEnabled(True)
        self.car_lease_table.setEditTriggers(QTableView.NoEditTriggers)
        
        self.order_table.setSortingEnabled(True)
        self.order_table.setEditTriggers(QTableView.NoEditTriggers)

        # make the width of a table fit the screen
        self.driver_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.car_lease_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.order_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        # show header of 3 table
        self.ui.table_result_2.horizontalHeader().show()
        self.ui.table_result.horizontalHeader().show()
        self.ui.table_result_3.horizontalHeader().show()
        self.ui.table_result.verticalHeader().show()
        self.ui.table_result_2.verticalHeader().show()
        self.ui.table_result_3.verticalHeader().show()
        
        #######################################################
        # Connect UI elements in PAGE DRIVER to class variables
        self.driver_name = self.ui.name_driver
        self.driver_phone = self.ui.phone_driver
        self.driver_born_time = self.ui.born_time
        self.driver_cccd = self.ui.cmmd_driver
        self.driver_address = self.ui.address_driver
        self.driver_has_car = self.ui.has_car
        self.driver_own_car_name = self.ui.driverHasCarBienSo
        self.driver_own_car_ton = self.ui.driverHasCarTon
        self.driver_own_car_type = self.ui.driverHasCarType

        self.driver_own_car_type_options = ["xe đông lạnh", "xe khô", "xe hở"]

        # envent click is has car
        self.driver_has_car.checkStateChanged.connect(self.setEnableForDriverOwnCar)
        
        # button in driver page
        self.add_btn_page1 = self.ui.add_btn
        self.update_btn_page1 = self.ui.update_btn
        self.search_btn_page1 = self.ui.find_btn
        self.clear_btn_page1 = self.ui.refresh_btn
        self.delete_btn_page1 = self.ui.remove_btn

        # button event of btn in driver page
        self.add_btn_page1.clicked.connect(self.add_info_driver_page)
        self.clear_btn_page1.clicked.connect(self.clear_form_driver_page)
        self.search_btn_page1.clicked.connect(self.search_form_driver_page)
        self.update_btn_page1.clicked.connect(self.update_form_driver_page)
        self.delete_btn_page1.clicked.connect(self.delete_form_driver_page)
        
        self.buttons_list_page1 = self.ui.frame_btn.findChildren(QPushButton)

        self.driver_list = []
       
        #######################################################
        # Connect UI elements in PAGE LEASE to class variables
        self.lease_name = self.ui.name_lease
        self.lease_phone = self.ui.phone_lease
        self.lease_address = self.ui.address_car_lease
        self.lease_own_car_name = self.ui.car_lease_number
        self.lease_own_car_ton = self.ui.car_lease_ton
        self.lease_own_car_type = self.ui.car_lease_type
        
        self.lease_car_type_options = ["xe đông lạnh", "xe khô", "xe hở"]

        for option in self.lease_car_type_options:
            self.lease_own_car_type.addItem(option)
        
        # button in driver page
        self.add_btn_page2 = self.ui.add_btn_2
        self.update_btn_page2 = self.ui.update_btn_2
        self.search_btn_page2 = self.ui.find_btn_2
        self.clear_btn_page2 = self.ui.refresh_btn_2
        self.delete_btn_page2 = self.ui.remove_btn_2

        # button event of btn in driver page
        self.add_btn_page2.clicked.connect(self.add_info_lease_page)
        self.clear_btn_page2.clicked.connect(self.clear_form_lease_page)
        self.search_btn_page2.clicked.connect(self.search_form_lease_page)
        self.update_btn_page2.clicked.connect(self.update_form_lease_page)
        self.delete_btn_page2.clicked.connect(self.delete_form_lease_page)
        
        self.lease_list = []
        
        #######################################################
        # Connect UI elements in PAGE ORDER to class variables   
        self.order_id = self.ui.name_orderID
        self.order_name = self.ui.order_name
        self.order_status = self.ui.order_status
        self.ton_cargo = self.ui.ton_cargo
        self.time_start = self.ui.time_start
        self.type_car_need = self.ui.order_need_car
        
        self.box_car = self.ui.car_chose_box
        self.car_name_order = self.ui.car_name_order
        self.box_driver_order = self.ui.driver_chose_box
        self.driver_name_order = self.ui.driver_name_order
        
        self.order_name.setReadOnly(True)
        self.order_status.setReadOnly(True)
        self.ton_cargo.setReadOnly(True)
        self.time_start.setReadOnly(True)
        self.type_car_need.setReadOnly(True)
        self.car_name_order.setReadOnly(True)
        self.driver_name_order.setReadOnly(True)

        self.have_car = [] # list to indecate if the driver have car as bool to make chose when driver dont have car then box in box car is enable
        # button in driver page
        self.export_data_order_page3= self.ui.add_btn_3
        self.update_btn_page3= self.ui.update_btn_3
        self.search_btn_page3= self.ui.find_btn_3
        self.clear_btn_page3= self.ui.refresh_btn_3
        self.refresh_order_btn_page3= self.ui.refresh_btn_order
                
        # button event of btn in driver page
        self.export_data_order_page3.clicked.connect(self.export_data_order_page)
        self.update_btn_page3.clicked.connect(self.update_form_order_page)
        self.search_btn_page3.clicked.connect(self.search_form_order_page)
        self.clear_btn_page3.clicked.connect(self.clear_form_order_page)
        self.refresh_order_btn_page3.clicked.connect(self.refresh_order_driver_page)
        
        # call function when box_carx_chose change
        self.box_driver_order.currentIndexChanged.connect(self.doDriverBox)
        self.box_car.currentIndexChanged.connect(self.doCarBox)
        
        self.order_list = []
        
        self.open_first_time = True
        
        # Load data to table from firebase 
        self.load_driver_data_from_firebase_to_driver_table()
        self.load_lease_data_from_firebase_to_lease_table()
        self.refresh_order_driver_page()
        
    ####################################ORDER PAGE####################################
    def switchToOrderPage(self):
        self.stacked_widget.setCurrentIndex(2)
        
        self.box_car.clear()
        self.box_driver_order.clear()
        
        self.have_car.clear()
        
        # add driver name and car type to box driver
        for index, option in enumerate(self.driver_list):
            name = self.driver_list[index].name
            car = " ,không xe" if self.driver_list[index].driver_own_car_type == "" else f" ,{self.driver_list[index].driver_own_car_type}, {self.driver_list[index].driver_own_car_ton} tấn"
            
            # if driver have car then set 1 in self.have_car list else set 0 use to disable or enable box of lease car
            self.have_car.append(0 if self.driver_list[index].driver_own_car_type == "" else 1)
            name_and_if_car = name + car    
            self.box_driver_order.addItem(name_and_if_car)
        
        # print(self.have_car)
            
        # print(len(self.driver_list))
        # print(self.driver_list[0].name)
        # print((self.driver_list[0].driver_own_car_type)=="")
        
        # print(len(self.lease_list))
    
    # process when the box driver is change
    def doDriverBox(self):
        text_name = self.box_driver_order.currentText()
        index_box = self.box_driver_order.currentIndex()
        print(text_name)
        # print(index_box)
        
        # set tex of text_name to driver name
        self.driver_name_order.setText(f"{self.driver_list[index_box].name}, {self.driver_list[index_box].phone}")
        
        # set box car base on driver have car or not
        # print(self.have_car[index_box])
        if self.have_car[index_box] == 0:
            self.car_name_order.clear()

            # clear box_car to make it fresh and append lease data to it 
            self.box_car.clear()         
            self.box_car.setEnabled(True)
            
            for index, option in enumerate(self.lease_list):
                name = self.lease_list[index].name
                car_name = self.lease_list[index].lease_own_car_name
                car_ton = self.lease_list[index].lease_own_car_ton
                car_type = self.lease_list[index].lease_own_car_type
    
                infor = f"{name}, {car_name}, {car_type}, {car_ton} tấn"
                # name_and_if_car = name + car    
                self.box_car.addItem(infor)
            
        else:
            # have car then enable false to not chose box car
            
            self.car_name_order.clear()
            
            # clear box car and set name  " "
            self.box_car.clear()
            self.box_car.setEnabled(False)
            self.box_car.setCurrentText(" ")
            
            # set name of car of driver that have car to qline edit as driver option in box
            car_name = self.driver_list[index_box].driver_own_car_name
            # print(car_name)
            self.car_name_order.clear()
            self.car_name_order.setText(car_name)
       
    # when box_car change then change text of car_name_order if box_car is enable
    def doCarBox(self):
        text_car = self.box_car.currentText()
        # self.car_name_order.setText(text_car)
        index_box = self.box_car.currentIndex()
             
        # set tex of text_name to driver name
        self.car_name_order.setText(f"{self.lease_list[index_box].lease_own_car_name}")
        
    # update car and driver for order using combo box
    # must have orderID and chose driver_name and car_name to update
    def update_form_order_page(self):
        # if have 
        print("update_form_order_page")
        orderID = self.order_id.text().strip()
        
        found_order = False
        
        for order in self.order_list:
            # print(order.get_info_order())
            if order.get_info_order()[0] ==orderID:
                found_order = True
                if order.get_info_order()[-1] >= 2:
                    QMessageBox.warning(self, 'Lỗi', 'Không thể cập nhật tài xế và xe cho đơn hàng đang/đã chạy')
                    return
                else:
                    break
        
        driver_name = self.driver_name_order.text().strip()
        car_name = self.car_name_order.text().strip()
        
        if not driver_name and not car_name:
            QMessageBox.information(self, f"Lỗi", "Hãy chọn tài xế và xe cho đơn hàng")
            return
        
        if found_order:
            connect_firebase.setDriverToFirebase(driver_name, f"orders/{orderID}/driver")
            connect_firebase.setDriverToFirebase(car_name, f"orders/{orderID}/car")
            connect_firebase.setDriverToFirebase(1, f"orders/{orderID}/status")
            
            QMessageBox.information(self, "Thành công", f"cập nhật thành công tài xế và xe cho đơn hàng{orderID}")
            return
    
    # clear table and load data from firebase
    # delete all row in table and delete all in order_list 
    # then get data from firebase and create new table and order_list
    def refresh_order_driver_page(self):
        print("refresh_order_driver_page")
        
        # clear item in table
        self.order_table.clearContents()
        self.order_table.setRowCount(0)
        
        # clear order list
        self.order_list.clear()

        # print(len(self.order_list))

        data = connect_firebase.loadDataFromFirebase("orders")
        
        keys = ["orderID", "status", "dateCreateOrder", "phoneCreatePerson","createPerson", "cargo1", "getDay", "typeContainer", "carTon", "driver", "car"]
        if len(data.val()) >= 1:
            print("len of order data is " + f"{len(data.val())}")
            order_data = data.val()  # Get the dictionary of all drivers
            # print(order_data)
            for row, (order_id, order_info) in enumerate(order_data.items()):
                complete = order_info["complete"]
                data = order_info["datas"]
                value_status = order_info["status"]
                
                if data != 0:
                    value_status = 2
                if complete != 0:
                    value_status = 3
                    
                self.order_table.insertRow(row)
                for col, key in enumerate(keys):
                    # print(col)
                    # print(order_info[key])
                    value = order_info[key]
                    if key == "status":
                        if value_status == 0:
                            value = "chưa xử lý"
                        elif value_status == 1:
                            value = "đã xử lý"
                        elif value_status == 2:
                            value = "đang chạy"
                        elif value_status == 3:
                            value = "đã chạy"
                    
                    if key == "typeContainer":
                        if value == "openContainer":
                            value = "xe hở"
                        elif value == "dryContainer":
                            value = "xe khô"
                        elif value == "coldContainer":
                            value = "xe đông lạnh"
                            
                    item = QTableWidgetItem(value)
                    self.order_table.setItem(row, col, item)
                    
                # add order that contain order id and status to order list
                order = Order(orderID=order_id, 
                                  status=value_status)
                self.order_list.append(order)
        
        # print(len(self.order_list))
        
        # just car the log after open first time 
        if not self.open_first_time:
            QMessageBox.information(self, "Thành công", "Làm mới xong bảng đơn")
        
        self.open_first_time = False
          
    def clear_form_order_page(self):
        self.order_id.clear()
        self.order_name.clear()
        self.order_status.clear()
        self.ton_cargo.clear()
        self.time_start.clear()
        self.type_car_need.clear()

        self.car_name_order.clear()
        self.driver_name_order.clear()
        
        self.box_car.setCurrentText(" ")
        self.box_driver_order.setCurrentText(" ")
        
        # show all row of table
        for row in range(self.order_table.rowCount()):
            self.order_table.showRow(row)
    
    # load data when click
    def show_data_to_form_order(self, index):
        row = index.row()
        column_count = self.order_table.columnCount()

        # Retrieve the item values from the selected row
        item_values = []
        for column in range(column_count):
            item = self.order_table.item(row, column)
            item_values.append(item.text() if item is not None else "")

        # Populate the driver details fields
        self.order_id.setText(item_values[0])
        self.order_status.setText(item_values[1])
        self.time_start.setText(item_values[6])
        self.ton_cargo.setText(item_values[8])
        self.order_name.setText(item_values[5])
        self.driver_name_order.setText(item_values[9])
        self.car_name_order.setText(item_values[10])
        self.type_car_need.setText(item_values[7])    
        
    # export base on orderID
    def export_data_order_page(self):
        orderID = self.order_id.text().strip()
        
        found_order = False
        for order in self.order_list:
            # print(order.get_info_order())
            if order.get_info_order()[0] ==orderID:
                found_order = True
                break
        
        if found_order:
            # QMessageBox.information(self, "Thành công", "Tìm thấy đơn hàng")
            test_word.createDox(orderID)
        else:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy đơn hàng")
            return   
        
    # search order base on orderID
    def search_form_order_page(self):
        print("search_order_page")
        orderID = self.order_id.text().strip()
        found_order = False
        
        for order in self.order_list:
            # print(order.get_info_order())
            if order.get_info_order()[0] ==orderID:
                found_order = True
                break
                    
        if found_order:
            QMessageBox.information(self, "Thành công", "Tìm thấy đơn hàng")
            for row in range(self.order_table.rowCount()):
                order_item = self.order_table.item(row, 0)
                if order_item.text().lower().find(orderID.lower()) >= 0:
                    # print(f"row{row}")
                    self.order_table.showRow(row)
                else:
                    self.order_table.hideRow(row)
            return
        else:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy đơn hàng")
            return   

    ####################################LEASE PAGE####################################
    # 2 function of load data from firebase to driver table
    def load_lease_data_from_firebase_to_lease_table(self):
        print("load_lease_data_from_firebase_to_lease_table")
        data = connect_firebase.loadDataFromFirebase("leases")
        # print("leases")
        
        if len(data.val()) >= 1:
            # print(len(data.val()))
            # print(data)
            lease_data = data.val()  # Get the dictionary of all drivers
            for lease_id, lease_info in lease_data.items():
                lease = Lease(
                                name=lease_info['name'],
                                phone=lease_info['phone'],
                                address=lease_info['address'],
                                lease_own_car_name=lease_info['lease_own_car_name'],
                                lease_own_car_type=lease_info['lease_own_car_type'],
                                lease_own_car_ton=lease_info['lease_own_car_ton']
                                )
                # add driver to a list
                self.lease_list.append(lease)
                
            print(len(self.lease_list))
            # set data to table
            self.set_lease_table()

    def set_lease_table(self):
        # selftable.setRowCount(len(driver_list))
        # add data from driver list to table
        for row, lease in enumerate(self.lease_list):
            # print(row)
            # print(lease)
            info_lease = lease.get_info_lease()
            # print(info_lease)
            self.car_lease_table.insertRow(row)
            
            for col, value in enumerate(info_lease):
                item = QTableWidgetItem(value)
                self.car_lease_table.setItem(row, col, item)
    
    # when click row in driver table then show in driver form, index is parameter default of lib
    def show_data_from_table_to_form_lease(self, index):
        row = index.row()
        column_count = self.car_lease_table.columnCount()

        # Retrieve the item values from the selected row
        item_values = []
        for column in range(column_count):
            item = self.car_lease_table.item(row, column)
            item_values.append(item.text() if item is not None else "")

        # Populate the driver details fields
        self.lease_name.setText(item_values[0])
        self.lease_phone.setText(item_values[1])
        self.lease_address.setText(item_values[2])
        self.lease_own_car_name.setText(item_values[3])
        self.lease_own_car_ton.setText(item_values[4])
        
        # Setting the selected item, find text car_type in lease_own_car_type and set index of finding value to lease_own_car_name box
        car_type = item_values[5]
        index = self.lease_own_car_type.findText(car_type)
        if index >= 0:
            self.lease_own_car_type.setCurrentIndex(index)

    # function of button in lease page
    # add new lease to table and add to firebase when click add
    def add_info_lease_page(self):
        print("add_info_lease_page")
        
        name = self.lease_name.text().strip()
        phone = self.lease_phone.text().strip()
        address = self.lease_address.text().strip()
        lease_own_car_name = self.lease_own_car_name.text().strip()
        lease_own_car_ton = self.lease_own_car_ton.text().strip()
        lease_own_car_type = self.lease_own_car_type.currentText().strip()

        if not name or not phone or not address or not lease_own_car_name or not lease_own_car_ton or not lease_own_car_type:
            QMessageBox.warning(self, 'Lỗi', 'Tất cả các mục phải được điền')
            return
        # elif len(cccd) < 9:
        #     QMessageBox.warning(self, 'Lỗi', 'cccd/cmnd phải dài hơn 9 chữ số')
        #     return
        else:
            for lease_car in self.lease_list:
                if lease_own_car_name == lease_car.lease_own_car_name:
                    QMessageBox.warning(self, 'Lỗi', 'Xe vận tải đã có trong hệ thống (trùng biển số xe)')
                    return
                
            rowCount = self.car_lease_table.rowCount()
            self.car_lease_table.insertRow(rowCount)
            self.car_lease_table.setItem(rowCount,0,QTableWidgetItem(name))
            self.car_lease_table.setItem(rowCount,1,QTableWidgetItem(phone))
            self.car_lease_table.setItem(rowCount,2,QTableWidgetItem(address))
            self.car_lease_table.setItem(rowCount,3,QTableWidgetItem(lease_own_car_name))
            self.car_lease_table.setItem(rowCount,4,QTableWidgetItem(lease_own_car_ton))
            self.car_lease_table.setItem(rowCount,5,QTableWidgetItem(lease_own_car_type))

            # add new driver to firebase
            lease_data = {
                "name": name,
                "phone": phone,
                "address": address,
                
                "lease_own_car_name": lease_own_car_name,
                "lease_own_car_ton": lease_own_car_ton,
                "lease_own_car_type": lease_own_car_type
                }
            # add to firebase
            connect_firebase.setDriverToFirebase(lease_data, f"leases/{lease_own_car_name}")

            lease = Lease(
                            name=name,
                            phone=phone,
                            address=address,
                            lease_own_car_name=lease_own_car_name,
                            lease_own_car_type=lease_own_car_type,
                            lease_own_car_ton=lease_own_car_ton
                            )
            # add driver to a list
            self.lease_list.append(lease)
                
            print(len(self.lease_list))
            QMessageBox.information(self, 'Thành công', 'Thêm xe mới với thông tin chủ xe thành công')
          
    def clear_form_lease_page(self):
        self.lease_name.clear()
        self.lease_phone.clear()
        self.lease_address.clear()
        self.lease_own_car_name.clear()
        self.lease_own_car_ton.clear()
       
        # show all row of table
        for row in range(self.car_lease_table.rowCount()):
            self.car_lease_table.showRow(row)
           
    # find car base on car name or lease name and table show the result
    def search_form_lease_page(self):
        search_name_car_text = self.lease_own_car_name.text()
        search_name_text = self.lease_name.text()
        
        isFound = False
        # if len of 2 search_name_car_text and search_name_text < 5 char then alert warning
        if (len(search_name_text.strip()) >= 3) or (len(search_name_car_text.strip()) >= 5):
            for row in range(self.car_lease_table.rowCount()):
                name_item = self.car_lease_table.item(row, 0)
                car_names_item = self.car_lease_table.item(row, 3)
                # self.car_lease_table.hideRow(row)

                # print(len(search_name_text.strip()) >= 3 and name_item.text().lower().find(search_name_text.lower()) >= 0)
                if (len(search_name_text.strip()) >= 3 and name_item.text().lower().find(search_name_text.lower()) >= 0) or (len(search_name_car_text.strip()) >= 5 and car_names_item.text().lower().find(search_name_car_text.lower()) >= 0):
                    # print(f"row{row}")
                    self.car_lease_table.showRow(row)
                    isFound = True
                else:
                    self.car_lease_table.hideRow(row)
        else: 
            QMessageBox.warning(self, "Lỗi", "Hãy nhập đầy đủ tên hoặc ít nhất 6 số biển số xe của chủ xe để tìm kiếm")
            return


        if isFound:
            QMessageBox.information(self, "Thành công", "Tìm thấy chủ xe và xe")
            return
        else:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy chủ xe và xe")
            return

    # delete car then set new car
    # must fill all input and update base on name car, name car must not change while update
    def update_form_lease_page(self):
        print("update_form_lease_page")
        name = self.lease_name.text().strip()
        phone = self.lease_phone.text().strip()
        address = self.lease_address.text().strip()
        lease_own_car_name = self.lease_own_car_name.text().strip()
        lease_own_car_ton = self.lease_own_car_ton.text().strip()
        lease_own_car_type = self.lease_own_car_type.currentText().strip()

        isFound = False
        
        if not name or not phone or not address or not lease_own_car_name or not lease_own_car_ton or not lease_own_car_type:
            QMessageBox.warning(self, 'Lỗi', 'Tất cả các mục phải được điền')
            return
        # elif len(cccd) < 9:
        #     QMessageBox.warning(self, 'Lỗi', 'cccd/cmnd phải dài hơn 9 chữ số')
        #     return
        else:
            for lease in self.lease_list:
                if lease_own_car_name == lease.lease_own_car_name:
                    isFound = True

            if not isFound:
                QMessageBox.warning(self, 'Lỗi', 'Xe vận tải không có trong hệ thống')
                return
            
            reply = QMessageBox.question(self, 'Cập nhật xe và chủ xe', f'Bạn có muốn cập nhật thông tin xe {lease_own_car_name}, chủ xe: {name}',
                                            QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                selected_row = 0
                
                for row in range(self.car_lease_table.rowCount()):
                    # name_item = self.car_lease_table.item(row, 0)
                    car_name_item = self.car_lease_table.item(row, 3)
                    # print((len(search_name_text.strip()) >= 3 and search_name_text.lower().find(name_item.text().lower()) >= 0) and (len(search_name_car_text.strip()) >= 9 and search_name_car_text.lower().lower().find(car_name_item.text()) >= 0))
                    if (len(lease_own_car_name) >= 5 and lease_own_car_name.lower().find(car_name_item.text().lower()) >= 0):
                        selected_row = row
                                        
                old_car_name_item = self.car_lease_table.item(selected_row, 3)
                # print(old_car_name_item.text())
                # delete old lease from firebase and lease_list
                for lease in self.lease_list:
                    if lease.lease_own_car_name == old_car_name_item.text():
                        print(lease.lease_own_car_name)
                        self.lease_list.remove(lease)
                
                # delete from firebase and lease_list
                connect_firebase.deleteDataToFirebase(f"leases/{old_car_name_item.text()}")
                
                # remove old row of old data in table
                self.car_lease_table.removeRow(selected_row)
                
                # insert new update lease from top of table
                row_first = 0
                self.car_lease_table.insertRow(row_first)
                self.car_lease_table.setItem(row_first,0,QTableWidgetItem(name))
                self.car_lease_table.setItem(row_first,1,QTableWidgetItem(phone))
                self.car_lease_table.setItem(row_first,2,QTableWidgetItem(address))
                self.car_lease_table.setItem(row_first,3,QTableWidgetItem(lease_own_car_name))
                self.car_lease_table.setItem(row_first,4,QTableWidgetItem(lease_own_car_ton))
                self.car_lease_table.setItem(row_first,5,QTableWidgetItem(lease_own_car_type))
                
                # add new lease to firebase
                lease_data = {
                    "name": name,
                    "phone": phone,
                    "address": address,
                    "lease_own_car_name": lease_own_car_name,
                    "lease_own_car_ton": lease_own_car_ton,
                    "lease_own_car_type": lease_own_car_type
                    }
                # add to firebase
                connect_firebase.setDriverToFirebase(lease_data, f"leases/{lease_own_car_name}")
                
                lease = Lease(
                        name=name,
                        phone=phone,
                        address=address,
                        lease_own_car_name=lease_own_car_name,
                        lease_own_car_type=lease_own_car_type,
                        lease_own_car_ton=lease_own_car_ton
                        )
                # add driver to a list
                self.lease_list.append(lease)
                    
                print(len(self.lease_list))
                
                QMessageBox.information(self, 'Thành công', 'Cập nhật thành công xe và chủ xe')
                
    # delete car lease when click 
    # must have car name and lease name in input table to delete            
    def delete_form_lease_page(self):
        # if have then del else error dont have
        print("delete_form_lease_page")
        search_name_car_text = self.lease_own_car_name.text().strip()
        search_name_text = self.lease_name.text().strip()
        
        print(len(search_name_car_text))
        print(len(search_name_text))
        
        isFound = False
        # if len of 2 search_name_car_text and search_name_text < 5 char then alert warning
        if len(search_name_text) >= 3 and len(search_name_car_text) >= 9:
            
            for lease in self.lease_list:
                if search_name_car_text == lease.lease_own_car_name:
                    isFound = True

            if not isFound:
                QMessageBox.warning(self, 'Lỗi', 'Xe vận tải không có trong hệ thống')
                return
                
            for row in range(self.car_lease_table.rowCount()):
                name_item = self.car_lease_table.item(row, 0)
                car_name_item = self.car_lease_table.item(row, 3)
                # print((len(search_name_text.strip()) >= 3 and search_name_text.lower().find(name_item.text().lower()) >= 0) and (len(search_name_car_text.strip()) >= 9 and search_name_car_text.lower().lower().find(car_name_item.text()) >= 0))
                if (len(search_name_text) >= 3 and search_name_text.lower().find(name_item.text().lower()) >= 0) and (len(search_name_car_text) >= 5 and search_name_car_text.lower().find(car_name_item.text().lower()) >= 0):
                    reply = QMessageBox.question(self, 'Xác nhận xóa xe', f'Bạn có muốn xóa xe {car_name_item.text()}, chủ xe: {name_item.text()}',
                                            QMessageBox.Yes | QMessageBox.No)

                    if reply == QMessageBox.Yes:
                        # delete from firebase and driver_list
                        for lease in self.lease_list:
                            if lease.lease_own_car_name == search_name_car_text:
                                print(lease.lease_own_car_name)
                                self.lease_list.remove(lease)
                        
                        print(len(self.lease_list))
                        # delete from firebase and lease_list
                        connect_firebase.deleteDataToFirebase(f"leases/{car_name_item.text()}")
                        
                        # remove row in table
                        self.car_lease_table.removeRow(row)
                        isFound = True
                        QMessageBox.information(self, 'Thành công', 'Xóa thành xe vận tải')
                        return
                    
        else: 
            QMessageBox.warning(self, "Lỗi", "Hãy nhập đầy đủ tên và ít nhất 9 số cmnd/cccd của tài xế để xóa tài xế")
            return
    
    ####################################DRIVER PAGE####################################
    # 2 function of load data from firebase to driver table
    def load_driver_data_from_firebase_to_driver_table(self):
        data = connect_firebase.loadDataFromFirebase("drivers")

        if len(data.val()) >= 1:
            # print(data)
            driver_data = data.val()  # Get the dictionary of all drivers
            for driver_id, driver_info in driver_data.items():
                driver = Driver(
                                name=driver_info['name'],
                                phone=driver_info['phone'],
                                cccd=driver_info['cccd'],
                                borntime=driver_info['borntime'],
                                address=driver_info['address'],
                                hascar=driver_info['hascar'],
                                driver_own_car_name=driver_info['driver_own_car_name'],
                                driver_own_car_type=driver_info['driver_own_car_type'],
                                driver_own_car_ton=driver_info['driver_own_car_ton']
                                )
                # add driver to a list
                self.driver_list.append(driver)
            
            print("load_driver_data_from_firebase_to_driver_table")
            print(len(self.driver_list))
            # set data to table
            self.set_driver_table()

    def set_driver_table(self):
        # selftable.setRowCount(len(driver_list))
        # add data from driver list to table
        for row, driver in enumerate(self.driver_list):
            # print(row)
            # print(driver)
            info_driver = driver.get_info_driver()
            # print(info_driver)  # object
            self.driver_table.insertRow(row)
            
            for col, value in enumerate(info_driver):
                item = QTableWidgetItem(value)
                self.driver_table.setItem(row, col, item)
    
    # 2 function for set driver own car when check state is change
    def setEnableForDriverOwnCar(self):
        if self.driver_has_car.isChecked():
            self.driver_own_car_name.setEnabled(True)
            self.driver_own_car_type.setEnabled(True)
            self.driver_own_car_ton.setEnabled(True)
            
            # add option ti boxcombo dropdown
            for option in self.driver_own_car_type_options:
                self.driver_own_car_type.addItem(option)

        else:
            self.setEnableFalseToDriverOwncarInfor()

    def setEnableFalseToDriverOwncarInfor(self):
            self.driver_own_car_name.setEnabled(False)
            self.driver_own_car_type.setEnabled(False)
            self.driver_own_car_ton.setEnabled(False)
            
            # remove option in boxcombo dropdown
            self.driver_own_car_type.clear()
            self.driver_own_car_type.setCurrentText("")
            
            # clear text
            self.driver_own_car_name.clear()
            self.driver_own_car_ton.clear()
    
    # when click row in driver table then show in driver form, index is parameter default of lib
    def show_data_from_table_to_form_driver(self, index):
        row = index.row()
        column_count = self.driver_table.columnCount()

        # Retrieve the item values from the selected row
        item_values = []
        for column in range(column_count):
            item = self.driver_table.item(row, column)
            item_values.append(item.text() if item is not None else "")

        # Populate the driver details fields
        self.driver_name.setText(item_values[0])
        self.driver_phone.setText(item_values[1])
        self.driver_address.setText(item_values[2])
        self.driver_born_time.setDate(QDate.fromString(item_values[3], "d/M/yyyy"))
        self.driver_cccd.setText(item_values[4])
        has_car = item_values[5]
        self.driver_has_car.setChecked(has_car == "có xe")
        self.driver_own_car_ton.setText(item_values[6])
        
        # Setting the selected item, find text car_type in driver_own_car_type and set index of finding value to driver_own_car_name box
        # find cartype in combo box, if have then set current index of combo box to that car type 
        car_type = item_values[7]
        index = self.driver_own_car_type.findText(car_type)
        if index >= 0:
            self.driver_own_car_type.setCurrentIndex(index)

        self.driver_own_car_name.setText(item_values[8])
   
    # function of button in driver page
    # add new driver to table and add to firebase when click add
    def add_info_driver_page(self):
        # driver should not have in driver list then can add to list
        print("add_info_driver_page")
        
        name = self.driver_name.text().strip()
        phone = self.driver_phone.text().strip()
        address = self.driver_address.text().strip()
        borntime = self.driver_born_time.text().strip()
        cccd = self.driver_cccd.text().strip()
        hascar = self.driver_has_car.isChecked()
        driver_own_car_name = self.driver_own_car_name.text().strip()
        driver_own_car_ton = self.driver_own_car_ton.text().strip()
        driver_own_car_type = self.driver_own_car_type.currentText().strip()

        if not name or not phone or not address or not borntime or not cccd:
            QMessageBox.warning(self, 'Lỗi', 'Tất cả các mục phải được điền')
            return
        # check cccd
        elif len(cccd) < 9:
            QMessageBox.warning(self, 'Lỗi', 'cccd/cmnd phải dài hơn 9 chữ số')
            return
        else:
            # check if driver is have or not
            for driver in self.driver_list:
                if cccd == driver.cccd:
                    QMessageBox.warning(self, 'Lỗi', 'Tài xế đã có trong hệ thống (trùng cccd/cmnd)')
                    return
            
            # add driver to table
            rowCount = self.driver_table.rowCount()
            self.driver_table.insertRow(rowCount)
            self.driver_table.setItem(rowCount,0,QTableWidgetItem(name))
            self.driver_table.setItem(rowCount,1,QTableWidgetItem(phone))
            self.driver_table.setItem(rowCount,2,QTableWidgetItem(address))
            self.driver_table.setItem(rowCount,3,QTableWidgetItem(borntime))
            self.driver_table.setItem(rowCount,4,QTableWidgetItem(cccd))
            self.driver_table.setItem(rowCount,5,QTableWidgetItem("có xe" if hascar else "không xe"))
            self.driver_table.setItem(rowCount,6,QTableWidgetItem(driver_own_car_ton))
            self.driver_table.setItem(rowCount,7,QTableWidgetItem(driver_own_car_type))
            self.driver_table.setItem(rowCount,8,QTableWidgetItem(driver_own_car_name))

            # add new driver to firebase
            driver_data = {
                "name": name,
                "phone": phone,
                "address": address,
                "borntime": borntime,
                "cccd": cccd,
                "hascar": hascar,
                "driver_own_car_name": driver_own_car_name,
                "driver_own_car_ton": driver_own_car_ton,
                "driver_own_car_type": driver_own_car_type
                }
            # add to firebase
            connect_firebase.setDriverToFirebase(driver_data, f"drivers/{cccd}")
            
            # add driver to driver list
            driver = Driver(
                            name=name,
                            phone=phone,
                            cccd=cccd,
                            borntime=borntime,
                            address=address,
                            hascar=hascar,
                            driver_own_car_name=driver_own_car_name,
                            driver_own_car_type=driver_own_car_type,
                            driver_own_car_ton=driver_own_car_ton
                            )
            
            self.driver_list.append(driver)
            print(len(self.driver_list))
            # print(self.driver_list[-1]) 
            # add driver to a list
            QMessageBox.information(self, 'Thành công', 'Thêm tài xế thành công')

    # clear form and clear search, set all row of table show when click clear
    def clear_form_driver_page(self):
        self.driver_name.clear()
        self.driver_phone.clear()
        self.driver_born_time.clear()
        self.driver_cccd.clear()
        self.driver_address.clear()
        self.driver_has_car.setChecked(False)
        self.driver_own_car_name.clear()
        self.driver_own_car_ton.clear()
        self.driver_born_time.setDate(QDate(2000, 1, 1))
        
        # show all row of table
        for row in range(self.driver_table.rowCount()):
            self.driver_table.showRow(row)
    
    # find driver base on cccd or name and table show the result
    # find base on cccd or name 
    def search_form_driver_page(self):
        search_cccd_text = self.driver_cccd.text()
        search_name_text = self.driver_name.text()
        
        # print(len(search_cccd_text))
        # print(len(search_name_text))
        
        # print(self.driver_table.rowCount())
        
        # for row in range(self.driver_table.rowCount()):
        #     name_item = self.driver_table.item(row, 0).text()
        #     cccd_item = self.driver_table.item(row, 4).text()
            
        #     print(row)
        #     print(name_item)
        #     self.driver_table.hideRow(row)
        isFound = False
        # if len of 2 search_cccd_text and search_name_text < 5 char then alert warning
        if (len(search_name_text.strip()) >= 3) or (len(search_cccd_text.strip()) >= 6):
            for row in range(self.driver_table.rowCount()):
                name_item = self.driver_table.item(row, 0)
                cccd_item = self.driver_table.item(row, 4)
                # self.driver_table.hideRow(row)

                # print(len(search_name_text.strip()) >= 3 and name_item.text().lower().find(search_name_text.lower()) >= 0)
                if (len(search_name_text.strip()) >= 3 and name_item.text().lower().find(search_name_text.lower()) >= 0) or (len(search_cccd_text.strip()) >= 6 and cccd_item.text().lower().find(search_cccd_text.lower()) >= 0):
                    # print(f"row{row}")
                    self.driver_table.showRow(row)
                    isFound = True
                else:
                    self.driver_table.hideRow(row)
        else: 
            QMessageBox.warning(self, "Lỗi", "Hãy nhập đầy đủ tên hoặc ít nhất 6 số cmnd/cccd của tài xế để tìm kiếm")
            return


        if isFound:
            QMessageBox.information(self, "Thành công", "Tìm thấy tài xế")
            return
        else:
            QMessageBox.warning(self, "Lỗi", "Không tìm thấy tài xế")
            return

    # delete driver when click 
    # must have name and cccd in input table to delete
    def delete_form_driver_page(self):
        # if driver have in driver list then delete driver, if not then show not have driver
        search_cccd_text = self.driver_cccd.text().strip()
        search_name_text = self.driver_name.text().strip()
        
        print(search_cccd_text)
        print(search_name_text)
        
        isFound = False
        
        # if len of 2 search_cccd_text and search_name_text < 5 char then alert warning
        if len(search_name_text.strip()) >= 3 and len(search_cccd_text.strip()) >= 9:
            for driver in self.driver_list:
                if search_cccd_text == driver.cccd:
                    if search_name_text == driver.name:
                        isFound = True
                        break
                
            if not isFound:
                QMessageBox.warning(self, 'Lỗi', 'Tài xế không có trong hệ thống hoặc thông tin tài xế nhập sai')
                return
        
            for row in range(self.driver_table.rowCount()):
                name_item = self.driver_table.item(row, 0)
                cccd_item = self.driver_table.item(row, 4)
                # print(row)
                # print((len(search_name_text.strip()) >= 3 and search_name_text.lower().find(name_item.text().lower()) >= 0) and (len(search_cccd_text.strip()) >= 9 and search_cccd_text.lower().lower().find(cccd_item.text()) >= 0))
                # print(len(search_name_text.strip()) >= 3 and name_item.text().lower().find(search_name_text.lower()) >= 0)
                if (len(search_name_text.strip()) >= 3 and search_name_text.lower().find(name_item.text().lower()) >= 0) and (len(search_cccd_text.strip()) >= 9 and search_cccd_text.lower().find(cccd_item.text()) >= 0):
                    reply = QMessageBox.question(self, 'Xác nhận xóa tài xế', f'Bạn có muốn xóa tài xế {name_item.text()}, cccd/cmnd: {cccd_item.text()}',
                                            QMessageBox.Yes | QMessageBox.No)

                    if reply == QMessageBox.Yes:
                        # delete from firebase and driver_list
                        for driver in self.driver_list:
                            if driver.cccd == search_cccd_text:
                                print(driver.cccd)
                                self.driver_list.remove(driver)
                        
                        # delete from firebase and driver_list
                        connect_firebase.deleteDataToFirebase(f"drivers/{cccd_item.text()}")
                        
                        # remove row in table
                        self.driver_table.removeRow(row)
                        isFound = True
                        QMessageBox.information(self, 'Thành công', 'Xóa thành công tài xế')
                        return
                    
        else: 
            QMessageBox.warning(self, "Lỗi", "Hãy nhập đầy đủ tên và ít nhất 9 số cmnd/cccd của tài xế để xóa tài xế")
            return

    # update driver when click update
    # delete driver then set new driver
    # must fill all input and update base on cccd, cccd must not change while update
    def update_form_driver_page(self):
        # if have driver then update, else error dont have driver
        print("update_form_driver_page")
        
        name = self.driver_name.text().strip()
        phone = self.driver_phone.text().strip()
        address = self.driver_address.text().strip()
        borntime = self.driver_born_time.text().strip()
        cccd = self.driver_cccd.text().strip()
        hascar = self.driver_has_car.isChecked()
        driver_own_car_name = self.driver_own_car_name.text().strip()
        driver_own_car_ton = self.driver_own_car_ton.text().strip()
        driver_own_car_type = self.driver_own_car_type.currentText().strip()

        isFound = False
        
        if not name or not phone or not address or not borntime or not cccd:
            QMessageBox.warning(self, 'Lỗi', 'Tất cả các mục phải được điền')
            return
        elif len(cccd) < 9:
            QMessageBox.warning(self, 'Lỗi', 'cccd/cmnd phải dài hơn 9 chữ số')
            return
        else:
            for driver in self.driver_list:
                if cccd == driver.cccd:
                    isFound = True
                    break
                    
            if not isFound:
                QMessageBox.warning(self, 'Lỗi', 'Tài xế không có trong hệ thống')
                return
            
            reply = QMessageBox.question(self, 'Cập nhật tài xế', f'Bạn có muốn cập nhật thông tin tài xế {name}, cccd/cmnd: {cccd}',
                                            QMessageBox.Yes | QMessageBox.No)

            if reply == QMessageBox.Yes:
                # find driver in which row then delete that row 
                
                # selected_row = self.driver_table.currentRow()
                selected_row = 0
                
                for row in range(self.driver_table.rowCount()):
                    cccd_item = self.driver_table.item(row, 4)

                    # find which current row is update driver
                    if (len(cccd.strip()) >= 6 and cccd_item.text().lower().find(cccd.lower()) >= 0):
                        # print(f"row{row}")
                        selected_row = row
                        
                old_cccd_item = self.driver_table.item(selected_row, 4)
                
                # delete old driver from firebase and driver_list
                for driver in self.driver_list:
                    if driver.cccd == old_cccd_item.text():
                        # print(driver.cccd)
                        # print(old_cccd_item) # object
                        print(old_cccd_item.text()) # name text
                        self.driver_list.remove(driver)
                        break
                # print(len(self.driver_list))
                
                # delete from firebase and driver_list
                connect_firebase.deleteDataToFirebase(f"drivers/{old_cccd_item.text()}")
                
                # remove old row of old data in table
                self.driver_table.removeRow(selected_row)
                
                # insert new update driver from top of table
                row_first = 0
                self.driver_table.insertRow(row_first)
                self.driver_table.setItem(row_first,0,QTableWidgetItem(name))
                self.driver_table.setItem(row_first,1,QTableWidgetItem(phone))
                self.driver_table.setItem(row_first,2,QTableWidgetItem(address))
                self.driver_table.setItem(row_first,3,QTableWidgetItem(borntime))
                self.driver_table.setItem(row_first,4,QTableWidgetItem(cccd))
                self.driver_table.setItem(row_first,5,QTableWidgetItem("có xe" if hascar else "không xe"))
                self.driver_table.setItem(row_first,6,QTableWidgetItem(driver_own_car_ton))
                self.driver_table.setItem(row_first,7,QTableWidgetItem(driver_own_car_type))
                self.driver_table.setItem(row_first,8,QTableWidgetItem(driver_own_car_name))
                
                # add new driver to firebase
                driver_data = {
                    "name": name,
                    "phone": phone,
                    "address": address,
                    "borntime": borntime,
                    "cccd": cccd,
                    "hascar": hascar,
                    "driver_own_car_name": driver_own_car_name,
                    "driver_own_car_ton": driver_own_car_ton,
                    "driver_own_car_type": driver_own_car_type
                    }
                # add to firebase
                connect_firebase.setDriverToFirebase(driver_data, f"drivers/{cccd}")
                
                driver = Driver(
                        name=name,
                        phone=phone,
                        cccd=cccd,
                        borntime=borntime,
                        address=address,
                        hascar=hascar,
                        driver_own_car_name=driver_own_car_name,
                        driver_own_car_type=driver_own_car_type,
                        driver_own_car_ton=driver_own_car_ton
                        )
                # add driver to a list
                self.driver_list.append(driver)
                
                print(len(self.driver_list))
                # print(self.driver_list[-1])
                # add new update driver to driver_list
                QMessageBox.information(self, 'Thành công', 'Cập nhật thành công tài xế')
    ########################################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())