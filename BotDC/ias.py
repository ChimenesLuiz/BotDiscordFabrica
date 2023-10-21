import json
import requests


def generate_chatGPT(text):
    
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiZGMzODA5NzAtMTRlYy00MzY3LThmNGEtYTZhYzc5NTFjYjA4IiwidHlwZSI6ImFwaV90b2tlbiJ9.fgy2wdjQMpyg2XwJ-YD6XwDZZmBNOtj7nOgE9i4lDMM"}

    url ="https://api.edenai.run/v2/text/chat"
    payload = {
        "providers": "openai",
        "text": text,
        "chatbot_global_action": "Act as an bot of discord named 'Fábrica de Software' that is provied by students(Arthur Simões, Luiz Chimenes e Thays Martines) of the Senac Brazil",
        "previous_history" : [],
        "temperature" : 0.0,
        "max_tokens" : 150
        }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)
    return result['openai']['generated_text']

ex = {
    
    "nome":"nome_do_execicio",
    "descricao":"descricao_do_exercicio",
    "dificuldade":"Facil"
    
}