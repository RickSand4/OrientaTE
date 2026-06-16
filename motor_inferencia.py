import base_conocimiento

def calcular_puntajes(respuestas_usuario):
    # Inicializar memoria de trabajo (marcador) en 0 para todas las carreras
    puntajes = {carrera: 0 for carrera in base_conocimiento.PREGUNTAS_INTERES.keys()}
    
    # Evaluar cada respuesta basándose en las reglas de la base de conocimiento
    for carrera, variables in base_conocimiento.PREGUNTAS_INTERES.items():
        for id_var, _ in variables:
            if id_var in respuestas_usuario:
                respuesta = respuestas_usuario[id_var]

                puntos_a_sumar = base_conocimiento.TABULADOR_PUNTOS.get(respuesta, 0)
                puntajes[carrera] += puntos_a_sumar
                
    return puntajes

def obtener_carrera_ideal(puntajes):
    puntaje_maximo = max(puntajes.values())
    if  puntaje_maximo != 0:
        carreras_ganadoras = [carrera for carrera, puntos in puntajes.items() if puntos == puntaje_maximo]
        return carreras_ganadoras
    else:
        return None

def generar_retroalimentacion_tronco(carreras_ganadoras, respuestas_tronco):
    # Tomamos la primera carrera en caso de empate para el consejo principal
    carrera = carreras_ganadoras[0] 
    
    if carrera in base_conocimiento.CONSEJOS_TRONCO_COMUN:
        reglas_consejo = base_conocimiento.CONSEJOS_TRONCO_COMUN[carrera]
        
        # Buscar qué habilidad le importa a esta carrera (ej. Hab_Matematicas)
        for habilidad_clave, mensajes in reglas_consejo.items():
            if habilidad_clave in respuestas_tronco:
                nivel_usuario = respuestas_tronco[habilidad_clave]
                
                # Definir si su habilidad es "alta" (4-5) o "baja" (1-3)
                if nivel_usuario >= 4:
                    return mensajes["alta"]
                else:
                    return mensajes["baja"]
                    
    return "Recuerda mantener un buen promedio general y repasar tus bases de ingeniería."