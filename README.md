# API em Python da Roleta: JonBet

Este projeto é uma aplicação web em Python que consome a API da roleta do site [JonBet](https://jonbet.bet.br/pt/games/double), salva os resultados em um banco de dados SQLite e atualiza em tempo real a interface web usando Flask e Socket.IO.

---

## Funcionalidades

- Consulta periódica da API da roleta para obter os resultados mais recentes.
- Armazena os resultados em banco SQLite (`results.db`).
- Interface web que mostra os últimos 20 resultados da roleta (número + cor).
- Atualização em tempo real da tabela de resultados via WebSocket.
- Notificação visual (toast) para novos resultados.
- Estilo moderno com tema escuro.

---

## Tecnologias usadas

- Python 3
- Flask
- Flask-SocketIO
- SQLite3
- Requests
- HTML, CSS e JavaScript (Socket.IO client)

---

## Como rodar

1. Clone o repositório:
    ```bash
    git clone https://github.com/asafeCode/roleta-jonbet-python.git
    cd roleta-jonbet-python
    ```

2. Crie e ative um ambiente virtual:
    ```bash
    python3 -m venv venv       # Criação
    source venv/bin/activate   # Ativação Linux/Mac
    venv\bin\activate      # Ativação Windows
    ```

3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

4. Execute a aplicação:
    ```bash
    python api.py
    ```

5. Acesse no navegador:
    ```
    Use o Google Chrome
    http://localhost:5000
    ```
6. Finalizar a Aplicação:
    ```
    Para parar o servidor, vá ao terminal onde está rodando e pressione Ctrl + C
    ```


---

## Arquivos principais

- `api.py` — Aplicação Flask + Socket.IO e lógica para consumir API e salvar resultados.
- `database.py` — Funções para inicializar o banco e salvar/obter resultados.
- `templates/index.html` — Página HTML para exibir a tabela de resultados e receber atualizações.
- `static/style.css` — Estilo CSS da página.

---

## Observações

- A aplicação faz requisições à API da JonBet a cada 5 segundos.
- Os resultados são armazenados localmente em SQLite (`results.db`).
- Caso o `recent_id` já exista, o resultado não será inserido novamente para evitar duplicatas.
- O WebSocket mantém o cliente atualizado em tempo real.

---

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## Contato

Se tiver dúvidas ou sugestões, abra uma *issue* (registro de problema/sugestão no GitHub) ou entre em contato.

---

**Divirta-se acompanhando os resultados da roleta em tempo real! 🎲**