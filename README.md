# Tradutor de Frases

A aplicação traz a funcionalidade de tradução de frases para que a pessoa possa se comunicar de maneira mais eficiente com diversas pessoas em idiomas diferentes.

# Procedimentos de instalação

## Instalação dos Pacotes

Os pacotes utilizados durante o projeto foram:
- SpeechRecognition
- pyaudio
- googletrans
- ibm-watson
- gTTS
- pygame

É preciso executar os seguintes comandos através do pip:
```
$ pip install ibm-watson
$ pip install gTTS
$ pip install pygame
```

Os pacotes SpeechRecognition, pyaudio e googletrans podem ser instalados através do pip ou pelo conda.

#### Pelo Pip
```
$ pip install SpeechRecognition
$ pip install pyaudio
$ pip install googletrans
```

#### Pelo Conda
```
$ conda install -c conda-forge speechrecognition
$ conda install -c anaconda pyaudio
$ conda install -c conda-forge googletrans
```

## Configuração da aplicação

É preciso que um arquivo com o nome *config.ini* seja criado na raiz do projeto com o seguinte formato

```
[SPEECH2TEXT]
API_KEY={sua-api-key}

[TEXT2SPEECH]
API_KEY={sua-api-key}
```

## Alteração do servico de reconhecimento

Por padrão a aplicação usa o serviço da IBM para reconhecimento e sintetização de voz, é possível realizar a troca apenas passando um outro nome no parâmetro serviço para as funções de reconhecimento e de sintetização descritas no **main.py**.

No caso da troca será utilizado o serviço da Google para tais funcionalidades.

# Execução da aplicação

Para executar a aplicação basta executar o comando
```
python main.py
```