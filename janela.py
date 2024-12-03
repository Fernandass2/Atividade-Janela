from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,
    QListWidget, QPushButton, QLineEdit, QGridLayout
)
from PyQt5.QtGui import QPixmap
import sys


class PaymentApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Pagamentos")
        self.resize(800, 600)

        # Layout principal
        main_layout = QVBoxLayout(self)

        # Adicionar logo da empresa
        logo_label = QLabel()
        pixmap = QPixmap("C:/Users/fernanda.bneris/Documents/JanelaAtividade")  # colocar sua logo e trocar as /
        logo_label.setPixmap(pixmap)
        logo_label.setStyleSheet("margin-bottom: 10px;")
        logo_label.setScaledContents(True)
        logo_label.setFixedHeight(80)  # Define altura fixa para a logo
        main_layout.addWidget(logo_label)

        # Layout horizontal principal
        horizontal_layout = QHBoxLayout()

        # Painel esquerdo - Métodos de pagamento
        left_widget = QWidget()
        left_layout = QVBoxLayout()
        left_widget.setLayout(left_layout)

        # Adicionar rótulo
        payment_methods_label = QLabel("Formas de pagamentos")
        payment_methods_label.setStyleSheet("font-weight: bold; font-size: 14px; color: black;")
        left_layout.addWidget(payment_methods_label)

        # Adicionar lista de métodos de pagamento
        self.payment_list = QListWidget()
        self.payment_list.addItems([
            "1 DINHEIRO", "PRAZO (NOTA)", "6 CHEQUE-PRE", "CREDITO", "DEBITO",
            "TEF ALIMENTACAO", "WEB CARD ALIMENTACAO", "2 VENDA ATACADO A VISTA",
            "TEF-CREDITO", "TEF-DEBITO", "ALIMENTACAO"
        ])
        self.payment_list.setStyleSheet("""
            background-color: white;
            border: 1px solid #ccc;
            font-size: 14px;
        """)
        left_layout.addWidget(self.payment_list)

        # Configuração de estilo para o painel esquerdo
        left_widget.setStyleSheet("background-color: #e6f7ff;")
        horizontal_layout.addWidget(left_widget, 1)

        # Painel direito - Detalhes e finalização
        right_widget = QWidget()
        right_layout = QVBoxLayout()
        right_widget.setLayout(right_layout)

        # Título do cliente
        client_label = QLabel("**CLIENTE A VISTA**")
        client_label.setStyleSheet("font-weight: bold; font-size: 16px; color: blue;")
        right_layout.addWidget(client_label)

        # Campo para exibir o valor restante
        grid_layout = QGridLayout()
        remaining_label = QLabel("Restante:")
        remaining_label.setStyleSheet("font-size: 14px;")
        grid_layout.addWidget(remaining_label, 0, 0)

        self.remaining_value = QLabel("9,14")
        self.remaining_value.setStyleSheet("font-size: 20px; font-weight: bold; color: red;")
        grid_layout.addWidget(self.remaining_value, 0, 1)

        # Campo para desconto
        discount_label = QLabel("Desconto:")
        discount_label.setStyleSheet("font-size: 14px;")
        grid_layout.addWidget(discount_label, 1, 0)

        self.discount_value = QLineEdit()
        self.discount_value.setPlaceholderText("0,00")
        self.discount_value.setStyleSheet("font-size: 14px;")
        self.discount_value.textChanged.connect(self.update_total)  # Atualiza o total ao mudar o texto
        grid_layout.addWidget(self.discount_value, 1, 1)

        # Campo para acréscimo
        increase_label = QLabel("Acréscimo:")
        increase_label.setStyleSheet("font-size: 14px;")
        grid_layout.addWidget(increase_label, 2, 0)

        self.increase_value = QLineEdit()
        self.increase_value.setPlaceholderText("0,00")
        self.increase_value.setStyleSheet("font-size: 14px;")
        self.increase_value.textChanged.connect(self.update_total)  # Atualiza o total ao mudar o texto
        grid_layout.addWidget(self.increase_value, 2, 1)

        # Adicionar layout em grid ao painel direito
        right_layout.addLayout(grid_layout)

        # Botão de finalização
        finalize_button = QPushButton("[F5] - Finalizar")
        finalize_button.setStyleSheet("""
            background-color: green;
            color: white;
            font-size: 16px;
            border-radius: 5px;
            padding: 10px;
        """)
        right_layout.addWidget(finalize_button)

        # Configuração de estilo para o painel direito
        right_widget.setStyleSheet("background-color: #f9f9f9;")
        horizontal_layout.addWidget(right_widget, 1)

        # Adicionar layout horizontal ao layout principal
        main_layout.addLayout(horizontal_layout)

        # Configuração de estilo para o fundo da janela principal
        self.setStyleSheet("background-color: #f0f0f0;")

    def update_total(self):
        """Atualiza o valor restante com base no desconto e acréscimo."""
        try:
            base_value = 9.14
            discount = float(self.discount_value.text().replace(",", ".") or "0")
            increase = float(self.increase_value.text().replace(",", ".") or "0")
            total = base_value - discount + increase
            self.remaining_value.setText(f"{total:.2f}")
        except ValueError:
            self.remaining_value.setText("Erro")  # Exibe erro se o valor for inválido



app = QApplication(sys.argv)
window = PaymentApp()
window.show()
sys.exit(app.exec_())
