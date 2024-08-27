from datetime import datetime, timedelta
import subprocess
import webbrowser
import time

class CommandHandler:
    def __init__(self):
        self.commands = {
            "olá": self.greet,
            "horas": self.tell_time,
            "sair": self.exit_program,
            "iniciar spotify": self.start_spotify,
            "iniciar google": self.start_google,
            "definir alarme": self.set_alarm
        }
    
    def handle_command(self, command):
        for keyword, action in self.commands.items():
            if keyword in command:
                action(command)
                return True
        return False

    def greet(self, command=None):
        print("Olá! Como posso ajudar?")
    
    def tell_time(self, command=None):
        now = datetime.now().strftime("%H:%M")
        print(f"Agora são {now}.")
    
    def start_spotify(self, command=None):
        print("Iniciando Spotify...")
        subprocess.Popen(["spotify"])

    def start_google(self, command=None):
        print("Abrindo o Google...")
        webbrowser.open("https://www.google.com")

    def set_alarm(self, command):
        try:
            # Extrai a hora do comando de voz
            time_str = command.split("definir alarme para ")[-1]
            alarm_time = datetime.strptime(time_str, "%H:%M").time()
            now = datetime.now()

            # Calcula o tempo restante até o alarme
            alarm_datetime = datetime.combine(now.date(), alarm_time)
            if alarm_datetime < now:
                alarm_datetime += timedelta(days=1)
            
            delta = (alarm_datetime - now).total_seconds()
            print(f"Alarme definido para {time_str}.")
            time.sleep(delta)
            print("Alarme tocando! Hora de acordar!")
        except ValueError:
            print("Formato de hora inválido. Tente novamente.")

    def exit_program(self, command=None):
        print("Encerrando o programa.")
        exit()
