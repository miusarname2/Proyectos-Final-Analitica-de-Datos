# Proyectos Finales Analisis de Datos
# Proyecto 1

# Proyecto 2

## Guía para ejecutar el proyecto

Para ejecutar este proyecto, sigue estos pasos:

1. **Instalación de Dependencias**:
   Asegúrate de tener Python instalado en tu sistema. Luego, instala las bibliotecas necesarias utilizando el archivo `requirements.txt` que has proporcionado. Sigue los pasos a continuación:

   1. Crea un entorno virtual (opcional pero recomendado):
      - En **Windows**:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```
      - En **macOS/Linux**:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

   2. Instala las dependencias desde `requirements.txt`:
      ```bash
      pip install -r requirements.txt
      ```

2. **Ejecución del Proyecto**:
   El proyecto utiliza la librería `flet` para la interfaz gráfica, junto con `pandas`, `matplotlib` y `seaborn` para análisis de datos y visualización.

   - Para ejecutar el proyecto, guarda el código Python que has proporcionado en un archivo, por ejemplo, `app.py`.
   - Desde la terminal, en el mismo directorio donde está el archivo `app.py`, ejecuta el siguiente comando:
     ```bash
     python app.py
     ```

   Esto abrirá la aplicación en una ventana del navegador donde podrás interactuar con la interfaz y cargar tus archivos CSV para análisis.

---

### Descripción del Proyecto

**Descripción General**:
Este proyecto tiene como objetivo desarrollar una herramienta interactiva de análisis de datos en Python, diseñada para evaluar y optimizar el rendimiento de las máquinas en una planta de ensamblaje automotriz. El análisis se basa en los datos de producción de máquinas, que incluyen tiempos de operación, inactividad, fallos y cantidades producidas, almacenados en archivos CSV.

La herramienta permitirá a los usuarios cargar archivos CSV, seleccionar parámetros como máquinas, turnos y fechas, y generar gráficos y reportes detallados para facilitar la toma de decisiones en la planta de producción.

**Tecnologías Utilizadas**:
- **Flet**: Para la creación de interfaces gráficas interactivas.
- **Pandas**: Para la manipulación y análisis de datos.
- **Matplotlib y Seaborn**: Para la creación de gráficos y visualización de datos.
- **Tkinter**: Para la selección de archivos CSV de manera fácil y rápida.

---

### Funcionalidades del Proyecto

**1. Carga y Lectura de Datos:**
El proyecto permite leer archivos CSV que contienen datos sobre el rendimiento de las máquinas en la planta de ensamblaje. Los datos incluyen detalles como la identificación de la máquina, tiempos de operación, tiempos de inactividad, tipo de error, unidades producidas, fecha y turno de trabajo. El script está diseñado para manejar grandes volúmenes de datos de múltiples máquinas y turnos.

**2. Estructuración y Limpieza de Datos:**
Los datos son procesados mediante listas y diccionarios para organizarlos por máquina, turno de trabajo o tipo de error. Se implementa una limpieza de datos para corregir valores nulos o inconsistentes.

**3. Análisis de la Eficiencia de Producción:**
Se calcula el índice de eficiencia de cada máquina dividiendo el tiempo de operación efectivo entre el tiempo total (operación + inactividad). Además, se evalúan los tiempos de inactividad para identificar las máquinas más problemáticas y los tipos de error más comunes.

**4. Visualización de Datos:**
Se generan gráficos de barras, líneas, pie y dispersión para mostrar:
- Unidades producidas por máquina.
- Distribución de tipos de errores.
- Relación entre tiempo de inactividad y unidades producidas.

**5. Optimización y Mejora de Procesos:**
Utilizando los resultados del análisis, se proponen mejoras en los procesos de producción, como la implementación de mantenimiento preventivo o la optimización de los turnos de trabajo. También se identifican cuellos de botella y se estiman posibles ahorros de tiempo y costos.

**6. Interactividad y Reportes:**
El sistema ofrece una interfaz interactiva donde los usuarios pueden seleccionar parámetros específicos (como máquinas, turnos o fechas) para personalizar el análisis. Además, genera un informe automatizado que resume los hallazgos clave, estadísticas de eficiencia, tiempos de inactividad y recomendaciones de mejora.