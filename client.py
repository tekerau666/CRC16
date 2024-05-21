import random
import string

import crcmod
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from PySide6.QtNetwork import QTcpSocket
import sys

from interface import Ui_MainWindow


class Client(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Client, self).__init__()
        self.setupUi(self)
        self.sendButton.clicked.connect(self.send_message)
        self.socket = QTcpSocket(self)

    def send_message(self):
        message = self.messageLineEdit.text()
        if not self.limit_characters(message):
            QMessageBox.warning(self, "Ошибка", "Сообщение должно быть не длиннее 10 символов.")
            return
        crc = self.encrypt(message)
        self.crcLineEdit.setText(str(crc))
        self.check_collision(message)

    def limit_characters(self, message):
        return len(message) <= 10

    def encrypt(self, message):
        crc16 = crcmod.predefined.Crc('crc-aug-ccitt')
        crc16.update(message.encode('utf-8'))
        return crc16.hexdigest()

    def generate_random_string(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(10))

    def check_collision(self, message):
        message_hash = self.encrypt(message)
        while True:
            random_string = self.generate_random_string()
            random_hash = self.encrypt(random_string)
            if random_hash == message_hash:
                self.kolliziaLineEdit.setText(random_string)
                self.crcLineEdit_2.setText(str(random_hash))
                break

# Основная часть программы
app = QApplication([])
client = Client()
client.show()
sys.exit(app.exec())
