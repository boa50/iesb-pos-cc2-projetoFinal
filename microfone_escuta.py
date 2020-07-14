from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import configparser

def microfone_escuta(servico='ibm', audio_blob=''):
    audio = audio_blob

    try:
        if servico == 'ibm':
            config = configparser.ConfigParser()
            config.read('config.ini')

            authenticator = IAMAuthenticator(config['SPEECH2TEXT']['API_KEY'])
            speech_to_text = SpeechToTextV1(authenticator=authenticator)
            speech_to_text.set_service_url('https://stream.watsonplatform.net/speech-to-text/api')

            speech_recognition_results = speech_to_text.recognize(
                                                                audio=audio, 
                                                                model='pt-BR_BroadbandModel', 
                                                                content_type='audio/webm').get_result()
            
            frase = speech_recognition_results['results'][0]['alternatives'][0]['transcript']
        else:
            frase = microfone.recognize_google(audio,language='pt-BR')
        
        print("Você disse: " + frase)

        return frase
        
    except:
        print("Não Entendi")
        return 'Não entendi o que você disse'