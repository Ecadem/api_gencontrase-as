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
    <!DOCTYPE html>
    <html>
    <head>
        <title>API de ecadem</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
        <style>
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
                font-family: Arial, sans-serif;
            }
            
            html, body {
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
            }
            
            .container {
                max-width: 800px;
                padding: 50px;
            }
            
            img {
                width: 100%;
                max-width: 500px;
                margin-bottom: 50px;
            }
            
            h1 {
                font-size: 36px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            
            p {
                font-size: 24px;
                margin-bottom: 50px;
            }
            
            .btn {
                display: inline-block;
                padding: 12px 20px;
                margin: 0 10px;
                font-size: 18px;
                color: #fff;
                background-color: #007bff;
                border-radius: 4px;
                text-decoration: none;
                cursor: pointer;
                width: 200px;
            }
            
            .btn i {
                margin-right: 10px;
            }
            
            .btn-primary {
                background-color: #007bff;
            }
            
            .btn-secondary {
                background-color: #6c757d;
            }
            
            .btn-primary:hover, .btn-secondary:hover {
                background-color: #0056b3;
            }
            .docs-section {
                margin-top: 40px;
                text-align: center;
                display: none;
            }
            .docs-section h2 {
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 20px;
            }
            .docs-section p {
                font-size: 18px;
                line-height: 1.5;
                margin-bottom: 10px;
            }
            .docs-section code {
                background-color: #f2f2f2;
                border-radius: 4px;
                font-family: monospace;
                padding: 2px 6px;
            }
            .toggle-container {
                justify-content: center;
                align-items: center;
            }
            .toggle-button {
                margin-top: 20px;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                border: 2px solid #000;
                border-radius: 5px;
                background-color: #fff;
                cursor: pointer;
            }
            
            @media (max-width: 600px) {
                h1 {
                    font-size: 24px;
                }
            
                p {
                    font-size: 18px;
                }
            
                .btn {
                    font-size: 16px;
                    margin-bottom: 10px;
                    width: 150px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <img src="https://i.imgur.com/kJ00MaT.png" alt="Logo de ecadem" class="img-fluid">
            <h1 class="mt-5">Bienvenido a la API de ecadem</h1>
            <p>Te invitamos a utilizar nuestra API y visitar nuestra página y repositorio en GitHub</p>
            <div class="mt-5">
                <a href="https://ecadem.co" target="_blank" class="btn btn-primary"><i class="fas fa-globe"></i> Página web</a>
                <a href="https://github.com/Ecadem" target="_blank" class="btn btn-secondary"><i class="fab fa-github"></i> GitHub</a>
            </div>
        
        <div class="toggle-container">
            <button class="toggle-button">Ver docs?</button>
        </div>
        
        <div class="docs-section">
            <h2>Cómo acceder a los docs de una API desarrollada en FastAPI</h2>
            <p>
                FastAPI genera automáticamente una documentación Swagger y OpenAPI para tu API web. 
                Puedes acceder a ella desde tu navegador web en la siguiente URL:
            </p>
            <p>
                <code>http://localhost:8000/docs</code>
            </p>
            <p>
                Reemplaza <code>http://localhost:8000</code> con la URL de tu servidor FastAPI.
            </p>
        </div>
        <script>
            // Obtener la sección de docs y el botón
            const docsSection = document.querySelector('.docs-section');
            const toggleButton = document.querySelector('.toggle-button');
            // Agregar un evento click al botón
            toggleButton.addEventListener('click', () => {
            // Cambiar la visibilidad de la sección de docs
            if (docsSection.style.display === 'none') {
                docsSection.style.display = 'block';
            } else {
                docsSection.style.display = 'none';
            }
            });
        </script>
    </body>
    </html>
   """


@router.post("/generate_pass", summary="Se encarga de generar una contraseña con un nivel mas de seguridad apartir de una frase", tags=['Generador Contraseñas'] )
def generate_pass(pwd: str):

    results = [ gen_password(pwd, char_dict, 0) for _ in range(1000) ] 
    response = get_pass_groups(results, pwd) 

    return {"data": response}
