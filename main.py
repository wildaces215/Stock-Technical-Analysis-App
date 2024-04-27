from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from tabs.rsi_tab import RSI
from tabs.ob_tab import OnBalanceTab
from tabs.ad_tab import AccumulationDistributionTab
from tabs.average_d_tab import AverageDirectionalIndexTab

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stock Analysis App")

        self.stock_ticker_label = QLabel("Stock Ticker")
        self.stock_ticker_input = QLineEdit()

        self.top_layout = QHBoxLayout()
        self.top_layout.addWidget(self.stock_ticker_label)
        self.top_layout.addWidget(self.stock_ticker_input)

        self.tabwidget = QTabWidget()
        self.tabwidget.addTab(RSI(self.stock_ticker_input), "RSI")
        self.tabwidget.addTab(OnBalanceTab(self.stock_ticker_input), "On Balance")
        self.tabwidget.addTab(AccumulationDistributionTab(self.stock_ticker_input), "A/V Line")
        self.tabwidget.addTab(AverageDirectionalIndexTab(), "Average Directional Index")

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.top_layout)
        self.main_layout.addWidget(self.tabwidget)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()