################### Referências ###################
# https://letscode-academy.com/blog/speech-recognition-com-python/
# https://www.pragnakalp.com/speech-recognition-speech-to-text-python-using-google-api-wit-ai-ibm-cmusphinx/
# https://pypi.org/project/SpeechRecognition/1.3.0/
###################################################

from microfone_escuta import microfone_escuta
from audio_fala import audio_fala
from frase_processa import frase_traduz
import unicodedata

idiomas = {
    'portugues': 'pt-br',
    'ingles': 'en',
    'japones': 'ja',
    'espanhol': 'es',
    'alemao': 'de',
    'italiano': 'it'
}

def idioma_altera():
    idioma_input = input('Digite o idioma para o qual quer traduzir\n\
Idiomas disponíveis: português, inglês, japonês, espanhol, alemão, italiano\n\n')

    idioma_input_processed = ''.join(ch for ch in unicodedata.normalize('NFKD', idioma_input) 
        if not unicodedata.combining(ch))
    idioma_input_processed = idioma_input.lower()

    return [idioma_input, idioma_input_processed]

def frase_fala(idioma_input_processed):
    ### Há um parâmetro indicando o servico a ser utilizado, por padrão usa-se o da IBM
    frase = microfone_escuta()

    idioma = idiomas[idioma_input_processed]

    if idioma != idiomas['portugues']:
        frase = frase_traduz(frase, idioma)

    ### Há um parâmetro indicando o servico a ser utilizado, por padrão usa-se o da IBM
    audio_fala(frase, idioma)



print()
print('-'*50)
print('TRADUTOR DE FRASES')
print('-'*50)

idiomas_retorno = idioma_altera()
idioma_input = idiomas_retorno[0]
idioma_input_processed = idiomas_retorno[1]

frase_fala(idioma_input_processed)

opcao = ''

while opcao != 's':
    print('\n\n\nIdioma escolhido:', idioma_input)
    print('O que você quer fazer agora?')
    opcao = input('Digite 1 para falar outra frase, 2 para trocar o idioma, e "s" para sair): ')

    if opcao == '1':
        frase_fala(idioma_input_processed)
    elif opcao == '2':
        idiomas_retorno = idioma_altera()
        idioma_input = idiomas_retorno[0]
        idioma_input_processed = idiomas_retorno[1]