import ui
import base_conocimiento
import motor_inferencia
import time
import sys

def hacer_cuestionario(lista_preguntas, titulo_modulo):
    respuestas = {}
    for id_var, pregunta in lista_preguntas:
        ui.limpiar_pantalla()
        print(f"=== {titulo_modulo} ===\n")
        ui.mostrar_escala()
        
        ui.escribir_lento(f"-> {pregunta}", velocidad=0.015)
        
        
        while True:
            respuesta = input("\n   Tu respuesta (1-5): ")
            if respuesta in ['1', '2', '3', '4', '5']:
                respuestas[id_var] = int(respuesta)
                break
            elif respuesta == '6':
                return KeyboardInterrupt
            else:
                ui.escribir_lento("    Por favor, ingresa un número válido entre 1 y 5.", velocidad=0.01)
    return respuestas

def iniciar_sistema():
    try:
        while True:
            opcion = ui.mostrar_menu_principal()
            
            if opcion == '1':
                # Pantalla de instrucciones
                ui.limpiar_pantalla()
                ui.escribir_lento("Inicializando el Motor de Inferencia...", velocidad=0.03)
                ui.escribir_lento("Hola. Soy tu orientador vocacional virtual.", velocidad=0.03)
                ui.escribir_lento("A continuación, evaluaremos tus intereses y habilidades.", velocidad=0.03)
                input("\n[Presiona ENTER para comenzar el diagnóstico...]")
                
                # FASE 1: RECOLECCIÓN DE HECHOS (INTERESES)
                respuestas_interes = {}
                for carrera, variables in base_conocimiento.PREGUNTAS_INTERES.items():
                    resp_carrera = hacer_cuestionario(variables, "MÓDULO 1: INTERESES ESPECÍFICOS")
                    respuestas_interes.update(resp_carrera)
                
                # FASE 2: RECOLECCIÓN DE HECHOS (TRONCO COMÚN)
                respuestas_tronco = hacer_cuestionario(base_conocimiento.PREGUNTAS_TRONCO, "MÓDULO 2: HABILIDADES DE TRONCO COMÚN")
                
                # FASE 3: PROCESAMIENTO DECLARATIVO 
                ui.limpiar_pantalla()
                ui.escribir_lento("Analizando tu perfil... Evaluando reglas... Aplicando pesos...", velocidad=0.04)
                time.sleep(1) 
                
                puntajes = motor_inferencia.calcular_puntajes(respuestas_interes)
                carreras_ideales = motor_inferencia.obtener_carrera_ideal(puntajes)
                
                # FASE 4: ENTREGA DE RESULTADOS
                ui.limpiar_pantalla()
                print("=========================================================")
                ui.escribir_lento("          ¡DIAGNÓSTICO COMPLETADO! ", velocidad=0.02)
                print("=========================================================\n")
                
                if carreras_ideales is None:
                    ui.escribir_lento("Todas tus respuestas estuvieron en las escalas más baja, sumando 0.\nQuizá no está en UPIIZ tu oferta ideal\n", velocidad=0.03)

                elif len(carreras_ideales) == 1:
                    ui.escribir_lento(f"  Tu carrera ideal es: {carreras_ideales[0].upper()}", velocidad=0.03)
                else:
                    ui.escribir_lento(f"  ¡Tienes un perfil híbrido! Tus carreras ideales son:", velocidad=0.03)
                    for c in carreras_ideales:
                        ui.escribir_lento(f"    - {c.upper()}", velocidad=0.03)
                

                if carreras_ideales is not None:
                    consejo = motor_inferencia.generar_retroalimentacion_tronco(carreras_ideales, respuestas_tronco)
                    print("\n---------------------------------------------------------")
                    ui.escribir_lento(consejo, velocidad=0.03)
                    print("---------------------------------------------------------\n")
                
                print("Marcador interno del Sistema Experto:")
                for c, p in puntajes.items():
                    print(f" - {c}: {p} pts")
                
                input("\n[Presiona ENTER para volver al menú principal]")
                
            elif opcion == '2':
                ui.limpiar_pantalla()
                ui.escribir_lento("Cerrando el sistema... ¡Mucho éxito en tu decisión!", velocidad=0.04)
                break
            else:
                ui.escribir_lento("Opción no válida. Intenta de nuevo.", velocidad=0.02)
                ui.limpiar_pantalla()       
    except:
        print("\n\nAdiós...")


if __name__ == "__main__":
    iniciar_sistema()