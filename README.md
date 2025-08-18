# Alinyo - Assistente de Bem-Estar com IA

![Interface do Chat Alinyo](https://raw.githubusercontent.com/offjune/alinyo_prototype/main/screenshot.jpg) 

Alinyo é uma aplicação web full-stack que funciona como um assistente de bem-estar e coach de rotina. Utilizando o poder dos LLMs (Large Language Models), o Alinyo conversa com o utilizador para entender as suas necessidades e criar rotinas personalizadas que equilibram a saúde física e mental.

Este projeto foi construído como um estudo prático de desenvolvimento web com Python e Django, integração com APIs de IA e criação de uma experiência de utilizador interativa e persistente.

---

## ✨ Funcionalidades

* **Chat Interativo:** Interface de chat em tempo real para conversar com o assistente de IA.
* **Memória Persistente:** O histórico da conversa é salvo e recarregado a cada visita, garantindo a continuidade.
* **Gestão de Sessão:** Cada utilizador tem uma sessão única e privada, gerida através do `localStorage` do navegador.
* **Respostas Formatadas:** O bot utiliza Markdown para formatar as suas respostas, tornando a leitura mais clara e organizada.
* **Backend Robusto:** Construído com Django, servindo tanto a página web quanto uma API RESTful para a lógica do chat.

---

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python, Django
* **Inteligência Artificial:** Google Gemini API
* **Frontend:** HTML, CSS, Bootstrap, JavaScript
* **Base de Dados:** SQLite (para desenvolvimento)
* **Formatação:** Python Markdown

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para ter o projeto a rodar na sua máquina.

### Pré-requisitos

* Python 3.10+
* Pip (gestor de pacotes do Python)

### Passos de Instalação

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/offjune/alinyo_prototype.git](https://github.com/offjune/alinyo_prototype.git)
    cd alinyo_prototype
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Windows
    python -m venv .venv
    .\.venv\Scripts\activate

    # Linux / macOS
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Nota: Se não tiver um `requirements.txt`, crie um com `pip freeze > requirements.txt`)*

4.  **Configure as variáveis de ambiente:**
    * Crie um ficheiro chamado `.env` na raiz do projeto (na mesma pasta do `manage.py`).
    * Dentro do ficheiro `.env`, adicione a sua chave da API do Google:
        ```
        GOOGLE_API_KEY=SUA_CHAVE_SECRETA_AQUI
        ```

5.  **Aplique as migrações da base de dados:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Inicie o servidor de desenvolvimento:**
    ```bash
    python manage.py runserver
    ```

7.  Abra o seu navegador e aceda a `http://127.0.0.1:8000/`. A aplicação deverá estar a funcionar!

---

## 👤 Autor

**June Silva**

* **LinkedIn:** [linkedin.com/in/june-silva](https://www.linkedin.com/in/june-silva/)
* **GitHub:** [github.com/offjune](https://github.com/offjune)

Feito com ❤️ e muito código. Este projeto é um reflexo da minha jornada de aprendizado e dedicação.
