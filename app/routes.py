from flask import render_template
from app import app
from app.utils.data import fakultas, program_studi
@app.route('/')

def home():
    return render_template('index.html', fakultas=fakultas, program_studi=program_studi)

