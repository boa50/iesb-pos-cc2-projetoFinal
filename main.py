from flask import Flask, jsonify, render_template, request, send_file
import io
import ast

from microfone_escuta import microfone_escuta
from audio_fala import audio_fala
from frase_processa import frase_traduz

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/transcreve', methods=['POST'])
def transcreve():
    dados = request.data
    frase = microfone_escuta(audio_blob=dados)

    return jsonify(frase=frase)

@app.route('/traduz/<idioma>', methods=['POST'])
def traduz(idioma):
    dados = request.data
    dict_str = dados.decode("UTF-8")
    dct = ast.literal_eval(dict_str)
    frase = dct['frase']

    if idioma != 'pt-br':
        traducao = frase_traduz(frase, idioma)
    else:
        traducao = frase

    return jsonify(traducao=traducao)

@app.route('/fala/<idioma>', methods=['POST'])
def fala(idioma):
    dados = request.data
    dict_str = dados.decode("UTF-8")
    dct = ast.literal_eval(dict_str)
    traducao = dct['traducao']

    blob = audio_fala(traducao, idioma)
    file_transfer = io.BytesIO(blob)

    return send_file(file_transfer, mimetype='audio/mp3')