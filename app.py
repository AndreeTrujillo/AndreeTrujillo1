import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

st.title("Aplicación de Análisis de Datos con Streamlit")

# 1. Lectura de Datos
st.sidebar.header("Carga de Datos")
uploaded_file = st.sidebar.file_uploader("Cargar archivo CSV", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Datos Cargados:")
    st.write(data.head())

    # 2. Resumen de Datos
    st.write("Resumen de Datos:")
    st.write(data.describe())

    # 3. Visualización de Datos
    st.write("Visualización de Datos:")
    st.subheader("Histogramas")
    columns = data.columns.tolist()
    column = st.selectbox("Selecciona una columna para el histograma", columns)
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    st.pyplot(plt)

    st.subheader("Gráfico de Dispersión")
    x_column = st.selectbox("Selecciona la columna X", columns, index=0)
    y_column = st.selectbox("Selecciona la columna Y", columns, index=1)
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=data, x=x_column, y=y_column)
    st.pyplot(plt)

    # 4. Técnica Estadística: Regresión Lineal
    st.write("Técnica Estadística: Regresión Lineal")
    if st.button("Realizar Regresión Lineal"):
        X = data[[x_column]].values
        y = data[y_column].values

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LinearRegression()
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        st.write(f"Coeficiente de regresión: {model.coef_[0]}")
        st.write(f"Intercepto: {model.intercept_}")
        st.write(f"Error Cuadrático Medio: {mean_squared_error(y_test, y_pred)}")
        st.write(f"R^2: {r2_score(y_test, y_pred)}")

        plt.figure(figsize=(10, 6))
        plt.scatter(X_test, y_test, color="blue", label="Datos Reales")
        plt.plot(X_test, y_pred, color="red", linewidth=2, label="Predicción")
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title("Regresión Lineal")
        plt.legend()
        st.pyplot(plt)
else:
    st.write("Por favor, carga un archivo CSV para comenzar.")

