import flet as ft
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import filedialog
from flet import Text, Column, Row, Dropdown, ElevatedButton

class DataAnalysisApp:
    def __init__(self):
        self.df = None

    def main(self, page: ft.Page):
        page.title = "Análisis de Rendimiento de Máquinas"
        page.horizontal_alignment = "center"
        
        # Pantalla de bienvenida
        welcome_text = Text("Bienvenido al Análisis de Rendimiento de Máquinas")
        upload_button = ElevatedButton("Subir archivo CSV", on_click=self.pick_file)
        
        page.add(Column([welcome_text, upload_button]))

    def pick_file(self, e):
        # Uso de Tkinter para la selección del archivo
        root = tk.Tk()
        root.withdraw()  # Ocultar la ventana principal de Tkinter
        file_path = filedialog.askopenfilename(
            filetypes=[("CSV files", "*.csv")],
            title="Selecciona un archivo CSV"
        )
        if file_path:
            self.df = pd.read_csv(file_path)
            self.df = self.clean_data(self.df)  # Limpiar datos
            self.show_analysis_options(e.page)

    def clean_data(self, df):
        # Limpieza básica de datos
        df.fillna(0, inplace=True)
        return df

    def handle_change(e):
        page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))
    
    def handle_dismissal(e):
        page.add(ft.Text("DatePicker dismissed"))

    def show_analysis_options(self, page):
        page.clean()
        
        # Opciones de análisis
        machine_selector = Dropdown(label="Selecciona máquina", options=[
            ft.dropdown.Option(text=machine, key=machine) for machine in self.df['Maquina'].unique()
        ])
        shift_selector = Dropdown(label="Selecciona turno", options=[
            ft.dropdown.Option(text="Mañana", key="Mañana"),
            ft.dropdown.Option(text="Tarde", key="Tarde"),
            ft.dropdown.Option(text="Noche", key="Noche")
        ])
        
        start_date_picker = ft.DatePicker()
        end_date_picker = ft.DatePicker()
        
        analyze_button = ElevatedButton("Analizar", on_click=lambda e: self.generate_plots(
            e, machine_selector.value, shift_selector.value, start_date_picker.value, end_date_picker.value
        ))
        
        report_button = ElevatedButton("Generar Informe", on_click=lambda e: self.handleGenerateReport(
            e, machine_selector.value, shift_selector.value, start_date_picker.value, end_date_picker.value,page
        ))
        
        page.add(ft.Column([
            Text("Personaliza el análisis"),
            Row([machine_selector, shift_selector]),
            Row([start_date_picker, end_date_picker]),
            Row([analyze_button, report_button])
        ]))


    def generate_plots(self, e, machine, shift, start_date, end_date):
        filtered_df = self.df
        
        # Filtrar por los parámetros seleccionados
        if machine:
            prefix = ''.join([char for char in machine if not char.isdigit()])
            filtered_df = filtered_df[filtered_df['Maquina'].str.startswith(prefix)]
            
        if shift:
            filtered_df = filtered_df[filtered_df['Turno'] == shift]
        if start_date and end_date:
            filtered_df = filtered_df[
                (filtered_df['Fecha'] >= start_date) & (filtered_df['Fecha'] <= end_date)
            ]
        
        # Generación de gráficos con Matplotlib
        
        # Gráfica de barras: Unidades producidas por máquinas con nombres similares
        plt.figure(figsize=(10, 6))
        sns.barplot(x="Maquina", y="Unidades Producidas", data=filtered_df)
        plt.title(f"Comparación de Unidades Producidas entre máquinas similares a '{prefix}'")
        plt.show()

        # Gráfica de pie: Distribución de tipos de errores
        error_counts = filtered_df["Tipo de Error"].value_counts()
        plt.figure(figsize=(6, 6))
        error_counts.plot.pie(autopct='%1.1f%%')
        plt.title(f"Distribución de Tipos de Errores en máquinas '{prefix}'")
        plt.ylabel('')
        plt.show()

        # Diagrama de dispersión: Tiempo de inactividad vs Unidades producidas
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x="Tiempo de Inactividad", y="Unidades Producidas", data=filtered_df, hue="Maquina")
        plt.title(f"Relación entre Tiempo de Inactividad y Unidades Producidas en máquinas '{prefix}'")
        plt.show()

    def generate_report(self, e, machine, shift, start_date, end_date):
        filtered_df = self.df

        if machine:
            filtered_df = filtered_df[filtered_df['Maquina'] == machine]
        if shift:
            filtered_df = filtered_df[filtered_df['Turno'] == shift]
        if start_date and end_date:
            filtered_df = filtered_df[
                (filtered_df['Fecha'] >= start_date) & (filtered_df['Fecha'] <= end_date)
            ]
        
        # Generar informe de rendimiento
        total_production = filtered_df["Unidades Producidas"].sum()
        avg_operating_time = filtered_df["Tiempo de Operación"].mean()
        avg_downtime = filtered_df["Tiempo de Inactividad"].mean()
        efficiency_index = avg_operating_time / (avg_operating_time + avg_downtime) if avg_operating_time + avg_downtime > 0 else 0
        
        report = (
            f"Informe de Rendimiento\n\n"
            f"Total de unidades producidas: {total_production}\n"
            f"Tiempo promedio de operación: {avg_operating_time:.2f} horas\n"
            f"Tiempo promedio de inactividad: {avg_downtime:.2f} horas\n"
            f"Índice de eficiencia: {efficiency_index:.2f}\n\n"
            f"Recomendaciones: Implementar mantenimiento preventivo para máquinas con alto tiempo de inactividad.\n"
            f"Optimizar turnos de trabajo para mejorar la eficiencia.\n"
        )

        return report
    
    def handleGenerateReport(self, e, machine, shift, start_date, end_date,page):
        report = self.generate_report(e, machine, shift, start_date, end_date)
        dlg = ft.AlertDialog(
            title=ft.Text('Reporte General.'),
            content=ft.Text(report),
        )
        page.open(dlg)


app = DataAnalysisApp()
ft.app(target=app.main)
