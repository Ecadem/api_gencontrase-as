# -*- coding: utf-8 -*-
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

import os
import json

from .models import (
   request_model,
)


from .dependencies import (
    gen_password,
    get_pass_groups,
)

from .settings import (
    char_dict
)

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
def root():
   return """
   <html>
        <head>
            <title>API Ecadem</title>
        </head>
        <body>
            <h1>Funciona equipo ¡funciona!</h1>
        </body>
    </html>
   """


@router.post("/generate_pass", summary="Se encarga de generar una contraseña con un nivel mas de seguridad apartir de una frase", tags=['Generador Contraseñas'] )
def generate_pass(pwd: str):

    results = [ gen_password(pwd, char_dict, 0) for _ in range(1000) ] 
    response = get_pass_groups(results, pwd) 

    return {"data": response}