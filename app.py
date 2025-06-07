from flask import Flask, render_template_string, request, redirect, session, url_for
from sqlalchemy import create_engine, text
import os
from datetime import datetime, date
from decimal import Decimal, InvalidOperation

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_muito_segura_e_unica_aqui_troque_imediatamente'
app.debug = True

@app.route('/')
def em_breve():
    return render_template_string('''
    <html>
        <head>
            <title>Em Breve</title>
            <style>
                body {
                    background-color: #b2d8b2;
                    color: white;
                    font-weight: bold;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                    font-size: 2em;
                    font-family: Arial, sans-serif;
                }
            </style>
        </head>
        <body>
            EM BREVE ...
        </body>
    </html>
    ''')

if __name__ == '__main__':
    if os.environ.get("WERKZEUG_RUN_MAIN") == "true" or not app.debug:
        import logging

        pass

    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=app.debug)