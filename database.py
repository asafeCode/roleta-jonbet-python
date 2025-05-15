import sqlite3

def init_db():
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS results (
            recent_id TEXT PRIMARY KEY,
            number INTEGER,
            color TEXT,
            created_at TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_results(recent_id, number, color, created_at):
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO results (recent_id, number, color, created_at) VALUES (?, ?, ?, ?)', (recent_id, number, color, created_at))
        conn.commit() 

    except sqlite3.IntegrityError:
        print(f"Erro: O `recent_id` {recent_id} já existe.")
        pass

    finally:
        conn.close()


def obter_resultados():
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT number, color FROM results 
                   ORDER BY created_at DESC 
                   LIMIT 20
                   ''')
    dados = cursor.fetchall()
    conn.close()
    return dados

def get_last_result():
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    cursor.execute('''
                   SELECT number, color FROM results 
                   ORDER BY created_at DESC 
                   LIMIT 1
                   ''')
    last_result = cursor.fetchone()
    conn.close()
    return last_result
