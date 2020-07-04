import speech_recognition as sr
from gtts import gTTS
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import pygame
from pygame import mixer
import configparser

def audio_fala(texto, language='pt-br', servico='ibm'):
    audio_path = 'audio.mp3'
    
    if servico == 'ibm':
        config = configparser.ConfigParser()
        config.read('config.ini')

        authenticator = IAMAuthenticator(config['TEXT2SPEECH']['API_KEY'])
        text_to_speech = TextToSpeechV1(authenticator=authenticator)
        text_to_speech.set_service_url('https://stream.watsonplatform.net/text-to-speech/api')

        vozes = {
            'pt-br': 'pt-BR_IsabelaVoice',
            'en': 'en-GB_KateVoice',
            'de': 'de-DE_BirgitVoice',
            'ja': 'ja-JP_EmiVoice',
            'it': 'it-IT_FrancescaVoice',
            'es': 'es-ES_LauraVoice'
            }

        voz = vozes[language]

        with open(audio_path, 'wb') as audio_file:
            audio_file.write(text_to_speech.synthesize(texto, voice=voz, accept='audio/mp3').get_result().content)
    else:
        tts = gTTS(texto, lang=language)
        tts.save(audio_path)


    print("Estou falando...")
    
    #Da play ao audio
    mixer.init()
    mixer.music.load(audio_path)
    mixer.music.play()
    while pygame.mixer.music.get_busy(): 
        pygame.time.Clock().tick(10)