from PyQt6.QtWidgets import *  # Import specific widgets you need
from PyQt6.QtGui import *  # Import specific GUI elements you need
from PyQt6 import uic
import sys
import database

class Alert(QMessageBox):
    def error_message(self, message):
        self.setIcon(QMessageBox.Icon.Critical)
        self.setText(message)
        self.setWindowTitle('Error')
        self.exec()
        
    def success_message(self, message):
        self.setIcon(QMessageBox.Icon.Information)
        self.setText(message)
        self.setWindowTitle('Success')
        self.exec()

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/login.ui',self)
        
        self.email_input = self.findChild(QLineEdit, 'email_input')
        self.password_input = self.findChild(QLineEdit, 'password_input')
        self.btn_login = self.findChild(QPushButton, 'login_btn')
        self.btn_register = self.findChild(QPushButton, 'register_btn')
        self.btn_eye = self.findChild(QPushButton, 'eye_btn')
        
        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        self.btn_eye.clicked.connect(lambda: self.hiddenOrShow(self.password_input, self.btn_eye))
        
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))
        
    def login(self):
        email = self.email_input.text()
        password = self.password_input.text()
        
        if email == '':
            msg = Alert()
            self.email_input.setFocus()
            return
        
        if password == '':
            msg = Alert()
            self.password_input.setFocus()
            return
        
        user = database.find_user_by_email_and_password(email,password)
        if user:
            msg = Alert()
            self.show_main(user["id"])
            msg.success_message('Login successful')
            
        else:
            msg = Alert()
            msg.error_message('invalid email or password')
            
    def show_register(self):
        self.register = Register()
        self.register.show()
        self.close()
        
    def show_main(self, user_id):
        self.main = Main(user_id)
        self.main.show()
        self.close()
        
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/register.ui',self)
        
        self.email_input = self.findChild(QLineEdit, 'email_input')
        self.name_input = self.findChild(QLineEdit, 'name_input')
        self.password_input = self.findChild(QLineEdit, 'password_input')
        self.confirm_password_input = self.findChild(QLineEdit, 'confirm_password_input')
        
        self.btn_register = self.findChild(QPushButton, 'register_btn')
        self.btn_login = self.findChild(QPushButton, 'login_btn')
        self.btn_eye1 = self.findChild(QPushButton, 'eye_btn1')
        self.btn_eye2 = self.findChild(QPushButton, 'eye_btn2')
        
        self.btn_eye1.clicked.connect(lambda: self.hiddenOrShow(self.password_input, self.btn_eye1))
        self.btn_eye2.clicked.connect(lambda: self.hiddenOrShow(self.confirm_password_input, self.btn_eye2))
        
    def hiddenOrShow(self, input:QLineEdit, button:QPushButton):
        if input.echoMode() == QLineEdit.EchoMode.Password:
            input.setEchoMode(QLineEdit.EchoMode.Normal)
            button.setIcon(QIcon("img/eye-solid.svg"))
        else:
            input.setEchoMode(QLineEdit.EchoMode.Password)
            button.setIcon(QIcon("img/eye-slash-solid.svg"))
        
    def register(self):
        email = self.email_input.text()
        name = self.name_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        
        if email == '':
            msg = Alert()
            msg.error_message('Please enter email address')
            self.email_input.setFocus()
            return
        if name == '':
            msg = Alert()
            msg.error_message('Please enter name')
            self.name_input.setFocus()
            return
        
        if password == '':
            msg = Alert()
            msg.error_message('Please enter password')
            self.password_input.setFocus()
            return
        
        if password != confirm_password:
            msg = Alert()
            msg.error_message('Password and confirm password does not match')
            self.confirm_password_input.setFocus()
            return
        
        user = database.find_user_by_email(email)
        if user:
            msg = Alert()
            msg.error_message('Email already exists')
        else:
            database.create_user(email, email, password)
            msg = Alert()
            msg.success_message('Registration successful')
            self.close()
            
    def show_login(self):
        self.login = Login()
        self.login.show()
        self.close()
        
            
class Main(QMainWindow):
    def __init__(self, user_id):
        super().__init__()
        uic.loadUi('ui/main.ui',self)
        self.user_id = user_id
        self.user = database.find_user_by_id(user_id)

        self.nav_home_btn = self.findChild(QPushButton,'nav_home_btn')
        self.nav_movie_btn = self.findChild(QPushButton,'nav_movie_btn')
        self.btn_mylist_btn = self.findChild(QPushButton,'btn_mylist_btn')
        self.stackedWidget = self.findChild(QStackedWidget,'stackedWidget')
        self.btn_avatar = self.findChild(QPushButton, 'btn_avatar')
        # self.stackedWidget.setCurrentIndex(2)
        
        self.nav_home_btn.clicked.connect(lambda: self.navigateScreen(2))
        self.nav_movie_btn.clicked.connect(lambda: self.navigateScreen(0))
        self.btn_avatar.clicked.connect(self.update_avatar)
    
    def navigateScreen(self, page:int):
        self.stackedWidget.setCurrentIndex(page)
        
    def load_user_info(self):
        self.lb_name = self.findChild(QLabel, 'lb_name')
        self.lb_email = self.findChild(QLabel, 'lb_email')
        self.lb_name .setText(self.user["name"])
        self.lb_email.setText(self.user["email"])
        self.btn_avatar.setIcon(QIcon(self.user["avatar"]))
    
    def update_avatar(self):
        file, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file:
            self.user["avatar"] = file
            self.btn_avatar.setIcon(QIcon(file))
            database.update_user_avatar(self.user_id, file)
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    
    login = Main(1)
    login.show()
    sys.exit(app.exec())    
