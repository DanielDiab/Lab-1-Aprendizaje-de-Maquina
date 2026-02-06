# Lab-1-Aprendizaje-de-Maquina
# AlpesHearth  
**Predicción de Riesgo Cardiovascular con Regresión Lineal**

---

## Integrantes

- Daniel Diab 
- Laura Martínez  

---

## Descripción general

En este laboratorio se desarrollará un modelo de regresión lineal para estimar el **CVD Risk Score** de pacientes, siguiendo el ciclo completo de machine learning. El objetivo es identificar los factores que más influyen en el riesgo cardiovascular y generar predicciones sobre un conjunto de datos no etiquetado.

Todo el proceso se documentará en un Notebook ejecutado y comentado.

---

## Estructura del proyecto

El proyecto está estructurado de la siguiente manera:
├── data/
│   ├── Datos Lab 1.csv
│   ├── Datos Test Lab 1.csv
│   └── DiccPacientes.xlsx
│
├── notebooks/
│   └── AlpesHearth_Lab1.ipynb
│
├── outputs/
│   └── Predicciones_Test.csv
│
└── README.md

---

## Herramientas

- Python  
- Pandas  
- NumPy  
- Scikit-Learn  
- Matplotlib  
- Seaborn  

Entorno: Visual Studio Code con Anaconda o Google Colab.

---

## Metodología de trabajo

El laboratorio se desarrollará siguiendo estas etapas:

---

### 1 Comprensión del conjunto de datos

- Revisar el diccionario de datos (`DiccPacientes.xlsx`).  
- Identificar variables numéricas, categóricas y variable objetivo (**CVD Risk Score**).  
- Verificar rangos, unidades y significado clínico básico.

---

### 2 Exploración de datos

Se realizará:

- Carga del dataset de entrenamiento.  
- `info()`, `describe()`, conteo de valores nulos.  
- Revisión de duplicados.  
- Histogramas y boxplots de variables principales.  
- Matriz de correlación.

**Resultado:** comprensión de la calidad del dataset y posibles problemas.

---

### 3 Preparación de datos

- Eliminación o imputación de valores faltantes.  
- Codificación de variables categóricas (si existen).  
- Escalamiento de variables numéricas cuando sea necesario.  
- Separación train/test con:

test_size = 0.25
random_state = 42

Las decisiones tomadas se justificarán en el notebook.

---

### 4 Construcción de modelos

Se entrenarán al menos dos modelos usando pipelines:

- Regresión lineal simple.  
- Regresión lineal con escalamiento y/o selección de características.

Ejemplo de pipeline:

- Preprocesamiento  
- Modelo de regresión  

---

### 5 Evaluación cuantitativa

Para cada modelo se calcularán:

- RMSE  
- MAE  
- R²  

Los resultados se organizarán en una tabla comparativa.

---

### 6 Selección del mejor modelo

Se escogerá el modelo con mejor desempeño en test considerando principalmente RMSE y R².

---

### 7 Evaluación cualitativa

Con el mejor modelo:

- Extraer coeficientes.  
- Identificar variables más influyentes.  
- Interpretar signo y magnitud de coeficientes.  
- Verificar supuestos básicos de regresión lineal (residuos, linealidad, homocedasticidad).

---

### 8 Análisis de sesgos

Se discutirán al menos dos posibles sesgos, por ejemplo:

- Sesgo de muestreo.  
- Sesgo por variables omitidas.  

---

### 9 Uso del modelo

- Entrenar el mejor modelo con todo el conjunto de entrenamiento.  
- Cargar `Datos Test Lab 1.csv`.  
- Generar predicciones de CVD Risk Score.  
- Exportar archivo CSV con las predicciones en carpeta `outputs/`.

---

### 10 Comunicación de resultados

Se elaborará un video (máx. 3 minutos) explicando:

- Datos utilizados.  
- Modelos construidos.  
- Métricas obtenidas.  
- Mejor modelo.  
- Variables más importantes.  
- Conclusiones.

---
