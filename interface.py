
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QMessageBox
from PySide6.QtCore import Qt

#função que verifica e exibe o nome  e a mensagem
def enviar():
    
    nome = nomeinput.text()
    mensagem = mensageminput.text()
    
    if nome and mensagem:
        janela.setStyleSheet("color: white; background-color: black; font-size: 18px;")
        QMessageBox.information(janela, "mensagemm Recebida", f"{nome} disse:   Palmeiras não tem... {mensagem}")
        janela.setStyleSheet("color: black; background-color: red;")
    else:
        janela.setStyleSheet("color: white; background-color: red; font-size: 18px;")
        QMessageBox.warning(janela, "Aviso", "Campo inválido. \nTente novamente.")
        janela.setStyleSheet("color: black; background-color: red;")


app = QApplication(sys.argv)
janela = QMainWindow()
janela.setWindowTitle(" by FELLIPE: heheha ")
janela.setStyleSheet("background-color: red;")

#texto
nome = QLabel(janela)
nome.setText("          Nome:")
nome.setStyleSheet("font-size: 18px; color: white;")
nome.setGeometry(10, 10, 200, 30)

#Cria a caixa de texto de nome
nomeinput = QLineEdit(janela)
nomeinput.setStyleSheet("font-size: 18px; background-color: white;")
nomeinput.setAlignment(Qt.AlignCenter)
nomeinput.setGeometry(10, 40, 200, 30)

#texto
mensagem = QLabel(janela)
mensagem.setText("      Mensagem:")
mensagem.setStyleSheet("font-size: 18px; color: white;")
mensagem.setGeometry(10, 80, 200, 30)

#Cria a caixa de texto de mensagem
mensageminput = QLineEdit(janela)
mensageminput.setStyleSheet("font-size: 16px; background-color: white;")
mensageminput.setAlignment(Qt.AlignCenter)
mensageminput.setGeometry(10, 110, 200, 30)

#botao de enviar que puxa a funçao criada no começo do código
submit_info = QPushButton(janela)
submit_info.setText("Enviar")
submit_info.setStyleSheet("font-size: 18px; background-color: red; color: black;")
submit_info.setGeometry(10, 150, 50, 30)
submit_info.clicked.connect(enviar)

#cria e delimita o tamanho da janela
janela.setGeometry(100, 100, 250, 200)
janela.show()

#fecha o app
sys.exit(app.exec())