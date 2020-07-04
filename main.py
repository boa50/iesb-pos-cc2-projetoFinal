########## Procedimentos de instalação ############
##### Pacotes #####
### Pip
# pip install SpeechRecognition
# pip install pyaudio
# pip install googletrans

### Anaconda
# conda install -c conda-forge speechrecognition
# conda install -c anaconda pyaudio
# conda install -c conda-forge googletrans

### Comum
# pip install ibm-watson
# pip install gTTS
# pip install pygame
####################


##### Arquivos #####
# Criar um arquivo config.ini na raiz do projeto com o conteúdo:
# [SPEECH2TEXT]
# API_KEY={sua-api-key}
#
# [TEXT2SPEECH]
# API_KEY={sua-api-key}
####################
###################################################

################### Referências ###################
# https://letscode-academy.com/blog/speech-recognition-com-python/
# https://www.pragnakalp.com/speech-recognition-speech-to-text-python-using-google-api-wit-ai-ibm-cmusphinx/
# https://pypi.org/project/SpeechRecognition/1.3.0/
###################################################

from microfone_escuta import microfone_escuta
from audio_fala import audio_fala
from frase_processa import frase_inverte, frase_traduz
import unicodedata

idiomas = {
    'portugues': 'pt-br',
    'ingles': 'en',
    'japones': 'ja',
    'espanhol': 'es',
    'alemao': 'de',
    'italiano': 'it'
}

print()
print('-'*50)
print('TRADUTOR DE FRASES')
print('-'*50)

idioma_input = input('Digite o idioma para o qual quer traduzir\n\
Idiomas disponíveis: português, inglês, japonês, espanhol, alemão, italiano\n\n')

idioma_input = ''.join(ch for ch in unicodedata.normalize('NFKD', idioma_input) 
    if not unicodedata.combining(ch))
idioma_input = idioma_input.lower()

# frase = microfone_escuta()
frase = 'Hoje, vou ao parque.'

idioma = idiomas[idioma_input]

# frase = frase_inverte(frase)
if idioma != idiomas['portugues']:
    frase = frase_traduz(frase, idioma)

audio_fala(frase, idioma)