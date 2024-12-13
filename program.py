from PyQt6.QtWidgets import QMainWindow,QApplication,QLineEdit,QMessageBox, QPushButton
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
        
        self.btn_login.clicked.connect(self.login)
        self.btn_register.clicked.connect(self.show_register)
        
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
            msg.success_message('Login succesful')
            
        else:
            msg = Alert()
            msg.error_message('invalid email or password')
            
    def show_register(self):
        self.register = Register()
        self.register.show()
        self.close()
        
class Register(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.load_ui('ui/register.ui',self)
        
        self.email_input = self.findChild(QLineEdit, 'email_input')
        self.name_input = self.findChild(QLineEdit, 'name_input')
        self.password_input = self.findChild(QLineEdit, 'password_input')
        self.confirm_password_input = self.findChild(QLineEdit, 'confirm_password_input')
        
        self.btn_register = self.findChild(QPushButton, 'register_btn')
        self.btn_login = self.findChild(QPushButton, 'login_btn')
        
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
            msg.error_message('Password and confirm passord does not match')
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
            
        
                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(app.exec())