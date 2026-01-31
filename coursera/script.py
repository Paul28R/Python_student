import pandas as pd

ventas = {"producto":["camisa", "Pantalon", "Sueter", "Medias", "Tenis"],
        "precio":[100, 200, 150, 30, 20],
        "cantidad":[4, 2, 2, 4, 2]}

datos = pd.DataFrame(ventas)
print("--- Dataframe Original ---")
print(datos)

solo_productos = datos['producto']
print("\n---Columna Producto---")
print(solo_productos)

filtro_caros = datos['precio']
print("\n--- Producto con precio > 50 ---")
print(filtro_caros)

datos['total'] = datos['precio'] * datos['cantidad']
print("\n ---DataFrame final con Columna total---")