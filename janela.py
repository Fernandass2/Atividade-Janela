
import sys
# importar a contrução da janela 

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QLabel, QTableWidget, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QComboBox, QListWidget

from PyQt5.QtCore import QPixmap


class PaymentWindow(QMainWindow):  # A classe principal que define  janela do programa.
    def __init__(self):            # Método incializador onde a interface é configurada.
        super().__init__()         #Chama o construtor da classe QMainWindow.
        self.setWindowTitle("MEC GESTÃO")       # Define o título da janela.
        self.setGeometry(100, 100, 800, 600)    # Define a posição e o tamanho da janela.

        # Main container

        main_widget = QWidget()                     # Um container que conterá os outros widget.
        main_layout = QGridLayout()                 # Layout de grade, que é usado para organizar os widget.
        main_widget.setLayout(main_layout)          
        self.setCentralWidget(main_widget)          # Define o Widget principal da janela.

        # Left Panel - Payment Methods

        payment_methods_label = QLabel("Formas de pagamentos")                      # Criar uma etiqueta
        payment_methods_label.setStyleSheet("font-weight: bold; font-size: 14px; color: black;")  # Estilizar o texto com negrito e tamanho da fonte

        self.payment_list = QListWidget()           # Criar lista aonde o métodos  de pagamentos são exibidos
        payment_methods = [
            "1 DINHEIRO", "PRAZO (NOTA)", "6 CHEQUE-PRE", "CREDITO",
            "DEBITO", "TEF ALIMENTACAO", "WEB CARD ALIMENTACAO",
            "2 VENDA ATACADO A VISTA", "TEF-CREDITO", "TEF-DEBITO", "ALIMENTACAO"
        ]
        self.payment_list.addItems(payment_methods)     # Adiciona o método de pagamento ao widget
        self.payment_list.setStyleSheet("""
                                background-color: white;
                                border: 1px solid #ccc;
                                font-size: 14px
                                        """)

        left_layout = QVBoxLayout()                     # Layout que organiza os widget verticalmente
        left_layout.addWidget(payment_methods_label)
        left_layout.addWidget(self.payment_list)

        left_widget = QWidget()
        left_widget.setLayout(left_layout)              # Um container para o painel esquerdo
        left_widget.setStyleSheet("Background-color: #0749b3") # Fundo de azul claro
        main_layout.addWidget(left_widget, 0, 0)        # Posiciona o painel na grade principal


        # Right Panel - Payment Details

        client_label = QLabel("**CLIENTE A VISTA**")
        client_label.setStyleSheet("font-weight: bold; font-size: 16px;")
        
        dependent_label = QLabel("Dependente: *** Não informado ***")

        self.remaining_label = QLabel("Restante:")      #   Exibir os textos dos clientes
        self.remaining_label.setStyleSheet("font-size: 16px;")  # Estiliza o texto

        self.remaining_value = QLabel("9,14")           # Exibe os valores restante
        self.remaining_value.setStyleSheet("font-size: 24px; font-weight: bold; color: blue;")

        sub_total_label = QLabel("Sub-Total:")
        sub_total_value = QLabel("9,14")
        sub_total_value.setStyleSheet("font-size: 16px;")

        discount_label = QLabel("Desconto:")
        discount_input = QLineEdit()

        increase_label = QLabel("Acréscimo:")
        increase_input = QLineEdit()

        finalize_button = QPushButton("[F5] - Finalizar")
        finalize_button.setStyleSheet("background-color: green; color: white; font-size: 16px; border-radius: 5px; padding: 10px")

        right_layout = QVBoxLayout()
        right_layout.addWidget(client_label, alignment=Qt.AlignCenter)
        right_layout.addWidget(dependent_label, alignment=Qt.AlignCenter)

        right_layout.addWidget(self.remaining_label, alignment=Qt.AlignRight)
        right_layout.addWidget(self.remaining_value, alignment=Qt.AlignRight)
        
        grid = QGridLayout()
        grid.addWidget(discount_label, 0, 0)
        grid.addWidget(discount_input, 0, 1)
        grid.addWidget(increase_label, 1, 0)
        grid.addWidget(increase_input, 1, 1)
        
        right_layout.addLayout(grid)

        right_layout.addWidget(sub_total_label, alignment=Qt.AlignRight)
        right_layout.addWidget(sub_total_value, alignment=Qt.AlignRight)
        right_layout.addWidget(finalize_button, alignment=Qt.AlignRight)

        right_widget = QWidget()
        right_widget.setLayout(right_layout)
        right_widget.setStyleSheet("background-color: #f9f9f9;")        # Fundo cinza
        main_layout.addWidget(right_widget, 0, 1)


app = QApplication([])
window = PaymentWindow()
window.show()
app.exec_()