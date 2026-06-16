import time
import sys
import os

def limpiar_pantalla():
    """Limpia la terminal dependiendo del sistema operativo (Linux/Windows)."""
    os.system('clear' if os.name == 'posix' else 'cls')

def escribir_lento(texto, velocidad=0.03, pausa_final=0.5):
    for caracter in texto:
        sys.stdout.write(caracter)
        sys.stdout.flush()
        time.sleep(velocidad)
    print() 
    time.sleep(pausa_final)

def mostrar_logo():
    logo = """
    ================================================================================
     ██████╗ ██████╗ ██╗███████╗███╗   ██╗████████╗ █████╗ ████████╗███████╗
    ██╔═══██╗██╔══██╗██║██╔════╝████╗  ██║╚══██╔══╝██╔══██╗╚══██╔══╝██╔════╝
    ██║   ██║██████╔╝██║█████╗  ██╔██╗ ██║   ██║   ███████║   ██║   █████╗  
    ██║   ██║██╔══██╗██║██╔══╝  ██║╚██╗██║   ██║   ██╔══██║   ██║   ██╔══╝  
    ╚██████╔╝██║  ██║██║███████╗██║ ╚████║   ██║   ██║  ██║   ██║   ███████╗
     ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝   ╚══════╝
                          SISTEMA EXPERTO VOCACIONAL - UPIIZ 
    ================================================================================
    """
    print(logo)

def mostrar_menu_principal():
    limpiar_pantalla()
    mostrar_logo()
    print(" [1] Iniciar diagnóstico vocacional")
    print(" [2] Salir del sistema\n")
    
    opcion = input(" -> Selecciona una opción: ")
    return opcion

def mostrar_escala():
    """Imprime la escala de valoración de forma estática."""
    print("   [1] Totalmente en desacuerdo / Me desagrada")
    print("   [2] En desacuerdo / No me interesa")
    print("   [3] Neutral / Indiferente (Me da igual)")
    print("   [4] De acuerdo / Me llama la atención")
    print("   [5] Totalmente de acuerdo / ¡Me encanta!")
    print("   [6] Salir\n")
    