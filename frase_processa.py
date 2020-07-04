from googletrans import Translator

def frase_traduz(frase, idioma_destino='en'):
    translator = Translator()
    result = translator.translate(frase, dest=idioma_destino)

    frase_traduzida = result.text
    print('Frase traduzida: ', frase_traduzida)

    return frase_traduzida