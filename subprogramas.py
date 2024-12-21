import re
import datetime
from fpdf import FPDF
import json
import subprocess



def monitoreo_de_red():  # mauricio
    print("Bienvenido al modulo para monitorear la red.")
    

    
def analisis_de_registros(registro_sistema): #alonso
    
    
    print("----------------------------analizando eventos del sistema -----------------------------")
    
        # Desarrolla scripts en PY que analicen los registros del sistema en busca de eventos 
    # anomalos o patrones de comportamiento sospechoso que puedan un ataque en curso
    
    with open(registro_sistema, "r") as file:
        # se abre el archivo a analizar, en este caso el de logs
        registros = file.readlines()
        # exprexiones regulares a buscar
        expreciones_reg = [
            #tener en cuenta el idioma del sistema, en mi caso esta en espanol
            
            r"Contrasena fallida", 
            
            
            
        ]
        
        patrones = [re.compile(expreciones, re.IGNORECASE) for expreciones in expreciones_reg]# se compilan las expreciones regulares, para su busqueda
        
        sospechos = []# almacena lo que se encuentra
        for linea_texto in registros:
            for patron in patrones:# se analiza el documentos en busca 
                if patron.search(linea_texto):# de las palabras claves
                    sospechos.append(linea_texto)## guarda 
                    break
        return sospechos# retorna
    
    
    
def Deteccion_de_vulnerabilidades():# marco
    adsd = 0
    print()
    
    
def Prevencion_de_ataques():#alonso
    print()
    
    #desarrolla un modulo en PY que analice el trafico web entrante y saliente 
    #para detectar posibles amenazas, como inyecciones SQL, XSS, o ataques de fuerza bruta

def analisis_de_trafico_web():#mauricio
    print()
    patrones_sql = []
    
    
def generar_informe_seguridad(incidentes, formato='PDF'):
    if formato == 'PDF':
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Informe de Seguridad", ln=True, align='C')
        pdf.cell(200, 10, txt=f"Fecha: {datetime.datetime.now()}", ln=True, align='C')
        pdf.ln(10)
        
        for incidente in incidentes:
            pdf.cell(200, 10, txt=f"Fecha: {incidente['fecha']}", ln=True)
            pdf.cell(200, 10, txt=f"Tipo de ataque: {incidente['tipo']}", ln=True)
            pdf.cell(200, 10, txt=f"Acciones tomadas: {incidente['acciones']}", ln=True)
            pdf.ln(10)
        
        pdf.output("informe_seguridad.pdf")
    elif formato == 'HTML':
        with open("informe_seguridad.html", "w") as file:
            file.write("<html><body>")
            file.write("<h1>Informe de Seguridad</h1>")
            file.write(f"<p>Fecha: {datetime.datetime.now()}</p>")
            
            for incidente in incidentes:
                file.write(f"<p>Fecha: {incidente['fecha']}</p>")
                file.write(f"<p>Tipo de ataque: {incidente['tipo']}</p>")
                file.write(f"<p>Acciones tomadas: {incidente['acciones']}</p>")
                file.write("<br>")
            
            file.write("</body></html>")

def registrar_incidente(incidentes, tipo, acciones):
    incidente = {
        'fecha': str(datetime.datetime.now()),
        'tipo': tipo,
        'acciones': acciones
    }
    incidentes.append(incidente)
    with open("incidentes.json", "w") as file:
        json.dump(incidentes, file)

def deteccion_de_vulnerabilidades():
    print("Detección de vulnerabilidades en progreso...")

    try:
        # Ejecutar bandit para analizar el código en busca de vulnerabilidades
        bandit_result = subprocess.run(['bandit', '-r', '.'], capture_output=True, text=True, check=True)
        print("Resultados de Bandit:")
        print(bandit_result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar Bandit:")
        print(e.stderr)

    try:
        # Ejecutar safety para verificar las dependencias en busca de versiones vulnerables
        safety_result = subprocess.run(['safety', 'check'], capture_output=True, text=True, check=True)
        print("Resultados de Safety:")
        print(safety_result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error al ejecutar Safety:")
        print(e.stderr)

    # Guardar los resultados en un archivo
    with open("resultados_vulnerabilidades.txt", "w") as file:
        file.write("Resultados de Bandit:\n")
        file.write(bandit_result.stdout)
        file.write("\nResultados de Safety:\n")
        file.write(safety_result.stdout)

deteccion_de_vulnerabilidades()

def alertas(): # mauricio
    print()
    
    
def Registro_incidentes(): #marco
    print()
    
    
def Informes_seguridad(): #marco
    print()



def menu(): #alonso
    print("Seleccione el numero que desea realizar!\n")
    print("1. Monitorear red\n")
    print("2. Analisis de registros \n")
    print("3. Detectar Vulnerabilidades\n" )
    print("4. Salir\n")

def main():
    while True:
        menu()
        try:
            opcion = int(input("Cual seria su seleccion?\n"))

            if opcion == 1:

                print()                                                         
                                                                                                 
            elif opcion == 2:

                print()                                                 
                                                                                                                                                          
            elif opcion == 3:

                print()                                                               

            elif opcion == 4:
                print("Cerrando programa!")
                break
            else: 
                print("Ingrese un numero dentro de las opciones")

            input("\nPresione Enter para volver al menú...")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    


if name== "main":
    main()