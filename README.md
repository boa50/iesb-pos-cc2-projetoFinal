# Tradutor de Frases

A aplicação traz a funcionalidade de tradução de frases para que a pessoa possa se comunicar de maneira mais eficiente com diversas pessoas em idiomas diferentes.

# Procedimentos de instalação

## Instalação dos Pacotes

Os pacotes utilizados durante o projeto foram:
- pyaudio
- googletrans
- ibm-watson
- gTTS
- Flask

É preciso executar os seguintes comandos através do pip:
```
$ pip install ibm-watson
$ pip install gTTS
```

Os pacotes SpeechRecognition, pyaudio e googletrans podem ser instalados através do pip ou pelo conda.

#### Pelo Pip
```
$ pip install pyaudio
$ pip install googletrans
$ pip install Flask
```

#### Pelo Conda
```
$ conda install -c anaconda pyaudio
$ conda install -c conda-forge googletrans
$ conda install -c anaconda flask
```

## Configuração da aplicação

É preciso que um arquivo com o nome *config.ini* seja criado na raiz do projeto com o seguinte formato

```
[SPEECH2TEXT]
API_KEY={sua-api-key}

[TEXT2SPEECH]
API_KEY={sua-api-key}
```

# Execução da aplicação

Para executar a aplicação basta executar os comandos
```
$ export FLASK_APP=main.py
$ flask run
```