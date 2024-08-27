import sys
import os

# Adiciona o diretório raiz ao caminho de módulos do Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from myvoiceassistant.voice_recognition import listen_and_recognize
from myvoiceassistant.command_handler import CommandHandler

# Crie uma instância do manipulador de comandos
handler = CommandHandler()

# Loop principal para ouvir e processar comandos
while True:
    # Ouça e reconheça o comando de voz
    command = listen_and_recognize()
    
    # Se um comando for reconhecido, processe-o
    if command:
        if not handler.handle_command(command):
            print("Comando não reconhecido.")
