import speech_recognition as sr

def listen_and_recognize():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Não entendi o que você disse")
        except sr.RequestError:
            print("Erro ao tentar acessar o serviço de reconhecimento")
        return ""

