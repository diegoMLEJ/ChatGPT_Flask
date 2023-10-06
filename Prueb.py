import  openai


openai.api_key="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"
respuesta = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {
                "role":"user",
                "content":"Hola, quien eres"
        }
    ],
    stream = True
)
for token in respuesta:
    print (token["choices"][0]["delta"]["content"], end="")