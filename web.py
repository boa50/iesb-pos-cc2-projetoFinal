from flask import Flask, jsonify, render_template, request, url_for

from microfone_escuta import microfone_escuta
from audio_fala import audio_fala
from frase_processa import frase_traduz

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/processa/<idioma>', methods=['POST'])
def retorna_algo(idioma):
    dados = request.data
    frase = microfone_escuta(audio_blob=dados)

    if idioma != 'pt-br':
        traducao = frase_traduz(frase, idioma)
    else:
        traducao = frase

    audio_fala(traducao, idioma)

    return jsonify(frase=frase, traducao=traducao)