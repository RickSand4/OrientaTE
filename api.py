from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Dict, List, Optional
import base_conocimiento
import motor_inferencia

app = FastAPI(title="OrientaTE - Sistema Experto Vocacional UPIIZ")
templates = Jinja2Templates(directory="templates")

# ── modelos ──────────────────────────────────────────────────────────────────

class RespuestasPayload(BaseModel):
    respuestas_interes: Dict[str, int]
    respuestas_tronco: Dict[str, int]

# ── utilidades ────────────────────────────────────────────────────────────────

def serializar_preguntas():
    """Devuelve las preguntas de interés en formato plano para el frontend."""
    bloques = []
    for carrera, variables in base_conocimiento.PREGUNTAS_INTERES.items():
        preguntas = [{"id": id_var, "texto": texto} for id_var, texto in variables]
        bloques.append({"carrera": carrera, "preguntas": preguntas})
    return bloques

def serializar_tronco():
    return [{"id": id_var, "texto": texto}
            for id_var, texto in base_conocimiento.PREGUNTAS_TRONCO]

# ── rutas ─────────────────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request, "index.html")

@app.get("/api/preguntas")
async def get_preguntas():
    return JSONResponse({
        "interes": serializar_preguntas(),
        "tronco": serializar_tronco(),
        "escala": {
            "1": "Totalmente en desacuerdo / Me desagrada",
            "2": "En desacuerdo / No me interesa",
            "3": "Neutral / Indiferente",
            "4": "De acuerdo / Me llama la atención",
            "5": "Totalmente de acuerdo / ¡Me encanta!",
        }
    })

@app.post("/api/diagnostico")
async def diagnostico(payload: RespuestasPayload):
    puntajes = motor_inferencia.calcular_puntajes(payload.respuestas_interes)
    carreras_ideales = motor_inferencia.obtener_carrera_ideal(puntajes)

    consejo = None
    if carreras_ideales:
        consejo = motor_inferencia.generar_retroalimentacion_tronco(
            carreras_ideales, payload.respuestas_tronco
        )

    return JSONResponse({
        "puntajes": puntajes,
        "carreras_ideales": carreras_ideales,
        "consejo": consejo,
    })
