import os
import openai
import threading

from dotenv import dotenv_values

config = dotenv_values(".env")
# openai.api_key = config["API_KEY"]
openai.api_key = os.getenv("OPENAI_API_KEY")

# define the model and the prompt
model_engine = "text-davinci-002"


def get_response(prompt, callback):
    get_response.is_busy = True
    try:
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        execute_prompt.response = completions.choices[0].text
        response = execute_prompt.response

        data = {'prompt': prompt, 'response': response}

        callback(data)  # Call the callback function with the response
    except:
        pass
    get_response.is_busy = False


def execute_prompt(prompt, callback):
    if not get_response.is_busy:
        threading.Thread(target=get_response, args=(prompt, callback,)).start()


get_response.is_busy = False
