from secret import API_KEY
import requests
import json

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_model = "gpt-3.5-turbo"

body_msg = {
    "model": "gpt-3.5-turbo",
    "messages": [
      {
        "role": "user",
        "content": "Ola chat gpt, como vc esta?"
      }
    ]
  }
body_msg = json.dumps(body_msg)

requisicao = requests.post(link, headers = headers, data = body_msg)

print(requisicao)
print(requisicao.text)
