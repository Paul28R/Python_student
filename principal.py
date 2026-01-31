# import sys 
# print(f"Hola desde Python en {sys.platform}")
import os
print(f"carpeta actual: {os.getcwd()}")
print(f"archivo en esta carpeta: {os.listdir(".")}")

import pandas as pd
dataset2 = pd.read_csv("cars.csv")
print(dataset2.head())