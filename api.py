from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import requests
import time 
from database import init_db, save_results, obter_resultados, get_last_result

app = Flask(__name__)
socketio = SocketIO(app)

def atualizar():
    while True:
        try:
            cookies = {
                '_gid': 'GA1.3.215100907.1747256248',
                'AMP_MKTG': 'JTdCJTIycmVmZXJyZXIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRnd3dy5nb29nbGUuY29tJTJGJTIyJTJDJTIycmVmZXJyaW5nX2RvbWFpbiUyMiUzQSUyMnd3dy5nb29nbGUuY29tJTIyJTdE',
                '_gcl_au': '1.1.466020439.1747256249',
                'accept_policy_regulation': '1',
                '_gat': '1',
                'AMP': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjI3YjlmNTUwZS0xNjViLTRkNGUtOGFiZS1lNjBhMDk3YzFkNDklMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNzQ3MjU2MjQ4NjkyJTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTc0NzI1NjI0ODc5MyUyQyUyMmxhc3RFdmVudElkJTIyJTNBMCU3RA==',
                '_ga': 'GA1.1.523240144.1747256248',
                '_ga_Y3FELE8HMH': 'GS2.1.s1747256248$o1$g1$t1747256986$j0$l0$h0',
            }

            headers = {
                'accept': 'application/json, text/plain, */*',
                'authorization': 'Bearer null',
                'referer': 'https://jonbet.bet.br/pt/games/double?modal=pay_table&game_mode=double_room_1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/136.0.0.0 Safari/537.36',
                'x-client-version': '526f4047d',
            }

            response = requests.get(
                'https://jonbet.bet.br/api/singleplayer-originals/originals/roulette_games/recent/1',
                cookies=cookies,
                headers=headers,
                timeout=10
            )

            if response.status_code == 200:
                api_response = response.json()

                if api_response:
                    result = api_response[0]
                    recent_number = result['roll']
                    color_code = result['color']
                    recent_id = result['id']
                    created_at = result['created_at']

                    colors = {
                        0: "branca",
                        1: "verde",
                        2: "preta"
                    }

                    recent_color = colors.get(color_code, "desconhecida")

                    last_result = get_last_result()
                    if last_result is None or recent_number != last_result[0]:
                        save_results(recent_id, recent_number, recent_color, created_at)
                        socketio.emit('novo_resultado', {
                            'number': recent_number,
                            'color': recent_color
                        })
        except Exception as e:
            print("Erro ao atualizar:", e)

        time.sleep(5)  # Espera 5 segundos antes da próxima verificação

@app.route('/')
def index():
    results = obter_resultados()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    init_db()
    socketio.start_background_task(atualizar)
    socketio.run(app, debug=True)

