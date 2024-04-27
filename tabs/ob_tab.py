from PyQt6.QtWidgets import QWidget, QVBoxLayout, QDateEdit, QLabel,QPushButton
from PyQt6.QtCore import QDate

import yfinance as yf
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

class OnBalanceTab(QWidget):
    def __init__(self,stock_ticker_input):
        super().__init__()
        self.stock_ticker = stock_ticker_input


        self.layout = QVBoxLayout(self)

        self.beginning_date_label = QLabel("Beginning Date:")
        self.beginning_date = QDateEdit()

        self.ending_date_label = QLabel("Ending Date:")
        self.ending_date = QDateEdit(QDate.currentDate())

        self.layout.addWidget(self.beginning_date_label)
        self.layout.addWidget(self.beginning_date)
        self.layout.addWidget(self.ending_date_label)
        self.layout.addWidget(self.ending_date)

        self.button = QPushButton("Analyse RSI")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.analyze)

        self.setLayout(self.layout)
    
    def analyze(self):
        print(self.stock_ticker.text)
        data = yf.download(self.stock_ticker.text(), start=self.beginning_date.date().toString("yyyy-MM-dd"), end=self.ending_date.date().toString("yyyy-MM-dd"))
        obv = data.ta.obv(close='Adj Close', volume='Volume')


        data['OBV'] = obv

# 
        fig, ax1 = plt.subplots()


        data['Adj Close'].plot(ax=ax1, color='blue', label='Adj Close')
        ax1.set_ylabel('Adjusted Close Price', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')

        # Create a secondary y-axis for OBV
        ax2 = ax1.twinx()
        data['OBV'].plot(ax=ax2, color='orange', label='OBV')
        ax2.set_ylabel('On-Balance Volume', color='orange')
        ax2.tick_params(axis='y', labelcolor='orange')

        plt.title(self.stock_ticker.text() +' Adjusted Close and On-Balance Volume (OBV)')
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')

        plt.show()
