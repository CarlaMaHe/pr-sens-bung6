import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Datei einlesen 
file_path = '/content/drive/MyDrive/Mikroanalytik/Data /Projekt_rohDaten.xlsx'
basename = os.path.basename(file_path)
file_name = os.path.splitext(basename)[0]
print(file_name)
