# -*- coding: utf-8 -*-
from fastapi import APIRouter
from fastapi.responses import HTMLResponse

import os
import json
import pandas as pd

from .models import (
   request_model,
)


# from .dependencies import ()
# from .settings import ()

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