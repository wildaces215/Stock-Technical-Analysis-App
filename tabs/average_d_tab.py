from PyQt6.QtWidgets import QWidget, QVBoxLayout, QDateEdit, QLabel,QPushButton,QPushButtonf
from PyQt6.QtCore import QDate

import yfinance as yf
import pandas as pd
import pandas_ta as ta
import matplotlib.pyplot as plt

class AverageDirectionalIndexTab(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.beginning_date_label = QLabel("Beginning Date:")
        self.beginning_date = QDateEdit(QDate.currentDate())
        self.ending_date_label = QLabel("Ending Date:")
        self.ending_date = QDateEdit(QDate.currentDate())

        self.layout.addWidget(self.beginning_date_label)
        self.layout.addWidget(self.beginning_date)
        self.layout.addWidget(self.ending_date_label)
        self.layout.addWidget(self.ending_date)

        self.button = QPushButton("Calculate Average Directional Index")    
        self.setLayout(self.layout)
    