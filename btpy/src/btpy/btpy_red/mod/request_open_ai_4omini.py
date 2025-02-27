

import openai

def request_open_ai_4omini(PROMPT, API_KEY, 
        MAX_TOKENS = 100):
    openai.api_key = API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        max_tokens = 100,
        temperature = 1.0,
        messages=[
        {"role": "system", 
         "content": PROMPT}
        ]
    )
    return response['choices'][0]\
        ['message']['content']