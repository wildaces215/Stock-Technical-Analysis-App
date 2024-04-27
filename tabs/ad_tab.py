from PyQt6.QtWidgets import QWidget, QVBoxLayout, QDateEdit, QLabel,QPushButton
from PyQt6.QtCore import QDate

import yfinance as yf
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

class AccumulationDistributionTab(QWidget):
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

        self.button = QPushButton("Analyse A/D Line")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.analyze)

        self.setLayout(self.layout)
    
    def analyze(self):
        print(self.stock_ticker.text)