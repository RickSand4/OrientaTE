TABULADOR_PUNTOS = {
    5: 2,  # Totalmente de acuerdo / ¡Me encanta! -> +2 puntos
    4: 1,  # De acuerdo / Me llama la atención -> +1 punto
    3: 0,  # Neutral / Indiferente -> 0 puntos (No aporta afinidad)
    2: 0,  # En desacuerdo / No me interesa -> 0 puntos
    1: 0   # Totalmente en desacuerdo / Me desagrada -> -1 puntos
}

PREGUNTAS_INTERES = {
    "Ingeniería en Sistemas Computacionales": [
        ("Int_Crear_Apps_Web", "¿Te interesa aprender a desarrollar páginas web y aplicaciones móviles?"),
        ("Int_Armar_Computadoras", "¿Te gusta conocer los componentes internos de una PC y cómo ensamblarlos?"),
        ("Int_Logica_Acertijos", "¿Disfrutas resolver problemas de lógica, acertijos o retos mentales?"),
        ("Int_Seguridad_Internet", "¿Te llama la atención cómo proteger redes, evitar hackeos y la privacidad online?")
    ],
    "Ingeniería Inteligencia Artificial": [
        ("Int_Ensenar_Maquinas", "¿Te intriga cómo los algoritmos pueden aprender de los datos para tomar decisiones solas?"),
        ("Int_Predecir_Tendencias", "¿Te gusta analizar datos para intentar predecir qué pasará en el futuro?"),
        ("Int_Asistentes_Voz", "¿Te interesan tecnologías como Siri, Alexa o chatbots y cómo entienden el lenguaje?"),
        ("Int_Matematica_Estrategica", "¿Te gustan las matemáticas enfocadas en estadística, probabilidad y optimización?")
    ],
    "Ingeniería Mecatrónica": [
        ("Int_Desarmar_Aparatos", "¿Desde niño te ha gustado desarmar juguetes o aparatos dañados para ver cómo funcionan?"),
        ("Int_Robotica_Casera", "¿Te gustaría diseñar y construir tus propios prototipos robóticos o automatizar cosas?"),
        ("Int_Mecanica_Movimiento", "¿Te interesa el diseño de engranes, motores y estructuras mecánicas en movimiento?"),
        ("Int_Modelado_3D", "¿Te llama la atención diseñar piezas o mecanismos usando software de computadora 3D?")
    ],
    "Ingeniería en Alimentos": [
        ("Int_Experimentos_Cocina", "¿Ves la cocina como un laboratorio donde mezclar ingredientes cambia sus propiedades?"),
        ("Int_Alimentos_Saludables", "¿Te interesa el desarrollo de nuevos productos alimenticios nutritivos o funcionales?"),
        ("Int_Conservacion_Empaques", "¿Te da curiosidad cómo se logra que la comida empaquetada dure meses sin echarse a perder?"),
        ("Int_Microorganismos", "¿Te interesa el estudio de bacterias y levaduras aplicados a la creación de productos?")
    ],
    "Ingeniería Ambiental": [
        ("Int_Salvar_Ecosistemas", "¿Te apasiona la protección de la flora, fauna y la conservación de hábitats naturales?"),
        ("Int_Energias_Limpias", "¿Te interesa cómo funcionan y se implementan los paneles solares y alternativas sustentables?"),
        ("Int_Limpiar_Contaminacion", "¿Te gustaría diseñar métodos para limpiar agua o suelos contaminados por industrias?"),
        ("Int_Reciclaje_Basura", "¿Te interesa la gestión de residuos, economía circular y la reducción de la basura?")
    ],
    "Ingeniería Metalúrgica": [
        ("Int_Rocas_Minerales", "¿Te llama la atención la composición química de las rocas y de dónde se extraen los minerales?"),
        ("Int_Fuego_Fundicion", "¿Te interesan los procesos industriales extremos como la fundición y creación de aleaciones?"),
        ("Int_Fuerza_Materiales", "¿Te da curiosidad saber por qué ciertos metales resisten tanta presión o calor y otros se rompen?"),
        ("Int_Reciclar_Metales", "¿Te interesa cómo recuperar y reutilizar metales a gran escala de la chatarra industrial?")
    ]
}

PREGUNTAS_TRONCO = [
    ("Hab_Matematicas", "Se me facilitan las matemáticas, el cálculo algebraico y el razonamiento numérico."),
    ("Hab_Programacion", "Tengo facilidad para la programación, la lógica de código y el pensamiento algorítmico."),
    ("Int_Ciencias_Naturales", "Me entusiasma el estudio de las ciencias naturales como la química, la biología o la física aplicada."),
    ("Int_Hardware_Electronica", "Disfruto experimentar con circuitos físicos, electrónica básica y componentes de hardware.")
]


CONSEJOS_TRONCO_COMUN = {
    "Ingeniería en Sistemas Computacionales": {
        "Hab_Programacion": {
            "baja": "Notamos que la programación aún no es tu fuerte. ¡No te preocupes! Empezarás desde cero, pero te recomendamos ir practicando lógica básica antes de entrar para que no se te complique.",
            "alta": "¡Excelente! Tu facilidad para la programación te dará una ventaja tremenda en el desarrollo de software."
        }
    },
    "Ingeniería Inteligencia Artificial": {
        "Hab_Matematicas": {
            "baja": "Tienes un perfil ideal para IA, pero ten en cuenta que exige un nivel alto de estadística y cálculo. Será fundamental que te regularices en matemáticas para dominar los modelos.",
            "alta": "¡Perfecto! Tu dominio matemático es la base fundamental que necesitas para entender y crear redes neuronales."
        }
    },
    "Ingeniería Mecatrónica": {
         "Int_Hardware_Electronica": {
            "baja": "Tu perfil de diseño y automatización es genial. Solo recuerda que estarás lidiando mucho con circuitos físicos; te sugerimos ir familiarizándote con conceptos básicos de electrónica.",
            "alta": "¡Muy bien! Tu afinidad por la electrónica y el hardware te facilitará enormemente el diseño de sistemas de control."
        }
    },
    "Ingeniería en Alimentos": {
        "Int_Ciencias_Naturales": {
            "baja": "Te interesan mucho los procesos alimenticios, pero recuerda que llevarás mucha química y biología. Es muy importante que refuerces tu interés en las ciencias naturales.",
            "alta": "¡Genial! Tu gusto por las ciencias naturales (química/biología) es exactamente lo que necesitas para triunfar en los laboratorios de alimentos."
        }
    },
    "Ingeniería Ambiental": {
        "Int_Ciencias_Naturales": {
            "baja": "Tienes gran vocación por salvar el planeta, pero debes saber que la carrera tiene una fuerte carga de química y física ambiental. Te sugerimos repasar esos fundamentos.",
            "alta": "¡Excelente perfil! Tu pasión por las ciencias naturales te ayudará a comprender profundamente los ecosistemas y la química de la contaminación."
        }
    },
    "Ingeniería Metalúrgica": {
        "Int_Ciencias_Naturales": {
            "baja": "Tu interés por los procesos industriales es claro, pero la metalurgia requiere bases fuertes en química y física de materiales. Será vital que fortalezcas esa área.",
            "alta": "¡Increíble! Tu interés en la física y la química te permitirá entender a la perfección el comportamiento y la estructura interna de los metales."
        }
    }
}