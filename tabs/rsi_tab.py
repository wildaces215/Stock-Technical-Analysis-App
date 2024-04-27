from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QDateEdit, QLabel,QMessageBox
import yfinance as yf
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt


class RSI(QWidget):
    def __init__(self, stock_ticker_input):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.beginning_date_label = QLabel("Beginning Date")
        self.layout.addWidget(self.beginning_date_label)

        self.beginning_date = QDateEdit()
        self.layout.addWidget(self.beginning_date)

        self.ending_date_label = QLabel("Ending Date")
        self.layout.addWidget(self.ending_date_label)

        self.ending_date = QDateEdit()
        self.layout.addWidget(self.ending_date)


        self.button = QPushButton("Analyse RSI")
        self.button.clicked.connect(self.print_label)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

        self.stock_ticker = stock_ticker_input

    def print_label(self):
        if self.stock_ticker.text() == "":
            QMessageBox.critical(self, "Error", "Please enter a stock ticker")
            return
        
        
        data = yf.download(str(self.stock_ticker.text()), start=self.beginning_date.date().toString("yyyy-MM-dd"), end='2024-01-01')
       
        rsi_period = 14  # You can adjust the RSI period
        data['RSI'] = ta.rsi(data['Close'], length=rsi_period)

        plt.figure(figsize=(8.33, 8.33))

        

        plt.subplot(2, 1, 1)
        plt.plot(data.index, data['Close'], label='Close Price')
        plt.title(self.stock_ticker.text() +' Close Price and RSI')
        plt.legend()

        plt.subplot(2, 1, 2)
        plt.plot(data.index, data['RSI'], label='RSI', color='orange')
        plt.axhline(70, color='red', linestyle='--')  # Overbought level
        plt.axhline(30, color='green', linestyle='--')  # Oversold level
        plt.title('RSI')
        plt.legend()
        
        plt.tight_layout()
        plt.show()


    

    

    
