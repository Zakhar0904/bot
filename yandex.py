import requests
import config 


def gpt(text):
    prompt = {
        "modelUri": f"gpt://{config.yandex1}/yandexgpt",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                #"text": "ты бот-рэпер, в ответ на любые запросы ты отвечаешь тем что читаешь текст как рэпер, ты гангстер, который читает рэп в стилек тупака"
                #'text': 'ты бот-переводичк текст на англиский, что тебя спросят - просто весь текст переведи на англиский'
                #'text': 'ты бот-разработчки, который умеет писать программы'
            
                #  'text': 'ты бот который на все отвечает в рифму'
                #'text': 'ты крутой покрасщик автомобилей'
                #'text': 'ты бот шутник котрый на все отвечает шутками'
                 'text': 'ты бот котрый учит людей экологии и решению проблемы с загрязнения окружающей среды. О чем мы тебя не спросили своди этот вопрос к экологии'
            },

            {
                "role": "user",
                "text": text
            }
        ]
    }
    
    
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {config.yandex2}"
    }
    
    response = requests.post(url, headers=headers, json=prompt)
    result = response.json().get('result')
    return result['alternatives'][0]['message']['text']


