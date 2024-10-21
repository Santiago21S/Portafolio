# Importar librerías necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from prettytable import PrettyTable
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Cargar los datos
data = pd.read_csv('winequality-red.csv', sep=';')

# Separar características (X) y el objetivo (y)
X = data.drop('quality', axis=1)  # Todas las columnas excepto 'quality'
y = data['quality']               # La columna 'quality' es la que queremos predecir

# Dividir los datos en conjunto de entrenamiento (80%) y prueba (20%)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Estandarizar los datos para mejorar el rendimiento de la red neuronal
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Definir la arquitectura de la red neuronal
model = Sequential()
model.add(Dense(64, input_dim=X_train.shape[1], activation='relu'))  # Capa oculta con 64 neuronas
model.add(Dense(32, activation='relu'))  # Segunda capa oculta con 32 neuronas
model.add(Dense(1))  # Capa de salida con 1 neurona (predicción del valor quality)

# Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Entrenar la red neuronal
model.fit(X_train, y_train, epochs=50, batch_size=10, verbose=1)

# Realizar predicciones sobre el conjunto de prueba
y_pred = model.predict(X_test).flatten()
# Crear una tabla PrettyTable para mostrar los resultados predichos y reales
table = PrettyTable()
table.field_names = ["Índice", "Valor Real", "Valor Previsto"]

# Agregar los resultados a la tabla
for index, (real, pred) in enumerate(zip(y_test, y_pred)):
    table.add_row([index, real, round(pred, 2)])  # Mostrar el índice, el valor real y el valor predicho

# Imprimir la tabla con los resultados
print("\nResultados Predichos y Reales (Conjunto de Prueba):")
print(table)
# Gráfico de la pérdida
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'])
plt.title('Curva de Entrenamiento')
plt.xlabel('Epocas')
plt.ylabel('Perdida')
# Graficar los valores reales
indices = range(len(y_test))  # Índices para el eje x
valores_reales = y_test  # Valores reales para el eje y
valores_pred = y_pred  # Valores reales para el eje y

plt.title('Valores Reales del Conjunto de Prueba')
plt.plot(indices, valores_reales)
plt.plot(indices, valores_pred)
plt.xlabel('Vinos')
plt.ylabel('Valor Real')
# Convertir las predicciones a clases discretas (redondear los valores predichos)
y_pred_clases = np.round(y_pred).astype(int)

# Limitar las predicciones al rango de calidad (asumiendo que la calidad del vino está entre 0 y 10)
y_pred_clases = np.clip(y_pred_clases, 0, 10)

# Tomar los primeros 10 valores reales y predichos
y_real_clases = y_test[:10].astype(int)  # Asegurarse de que los valores reales sean enteros
y_pred_clases = y_pred_clases[:10]  # Tomar solo los primeros 10 valores predichos

# Crear la matriz de confusión
cm = confusion_matrix(y_real_clases, y_pred_clases, labels=np.arange(11))  # Etiquetas de 0 a 10

# Mostrar la matriz de confusión
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=np.arange(11))
disp.plot(cmap=plt.cm.Blues)  # Usar un mapa de colores azul
plt.title('Matriz de Confusión (Primeros 10 Valores)')
plt.show()