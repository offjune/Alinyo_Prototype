from chatbot import Chatbot

if __name__ == "__main__":
    meu_chatbot = Chatbot()

    while True:
        entrada_usuario = input("\n Sua mensagem: ")

        if entrada_usuario.lower() in ["sair", "exit", "quit", "parar", "fechar"]:
            print("\n Até mais! Cuide-se.")
            break

        resposta_ai = meu_chatbot.get_response(entrada_usuario)
        print(f"\n {resposta_ai}")
