from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from phonebook import PhoneBook

def run_gui():
    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("PhoneBook")

    pb = PhoneBook()

    label_name = QLabel("Name:")
    input_name = QLineEdit()
    label_num  = QLabel("Number:")
    input_num  = QLineEdit()

    btn_add    = QPushButton("Add")
    btn_get    = QPushButton("Get")
    btn_update = QPushButton("Update")
    btn_remove = QPushButton("Remove")
    btn_hascontact = QPushButton("Contact exist?")
    btn_allcontact = QPushButton("All contacts")

    layout = QVBoxLayout()
    layout.addWidget(label_name)
    layout.addWidget(input_name)
    layout.addWidget(label_num)
    layout.addWidget(input_num)
    layout.addWidget(btn_add)
    layout.addWidget(btn_get)
    layout.addWidget(btn_update)
    layout.addWidget(btn_remove)
    layout.addWidget(btn_hascontact)
    layout.addWidget(btn_allcontact)

    window.setLayout(layout)

    def show_msg(text):
        QMessageBox.information(window, "Info", text)

    btn_add.clicked.connect(lambda: (
        pb.add_contact(input_name.text(), input_num.text()),
        show_msg(f"Added {input_name.text()}")
    ))
    btn_get.clicked.connect(lambda: (
        show_msg(f"{input_name.text()}: {pb.get_number(input_name.text())}")
    ))
    btn_update.clicked.connect(lambda: (
        pb.update_contact(input_name.text(), input_num.text()),
        show_msg(f"Updated {input_name.text()}")
    ))
    btn_remove.clicked.connect(lambda: (
        pb.remove_contact(input_name.text()),
        show_msg(f"Removed {input_name.text()}")
    ))
    btn_hascontact.clicked.connect(lambda: (
        show_msg(f"{input_name.text()}: {pb.has_contact(input_name.text())}")
    ))
    btn_allcontact.clicked.connect(lambda: (
        show_msg(f"{pb.all_contacts()}")
    ))

    window.show()
    app.exec()

if __name__ == "__main__":
    run_gui()
