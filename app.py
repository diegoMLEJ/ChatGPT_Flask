from flask import Flask, render_template, request
import openai

app = Flask(__name__)
historial = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method=="POST":
        pregunta = request.form.get("pregunta")
        resultado = enviar_pregunta(pregunta)
        historial.append({"rol": "user", "contenido": pregunta})
        historial.append({"rol": "chatbot", "contenido": resultado})
    else:
        chat=""
    return render_template("index.html", historial=historial)

def enviar_pregunta(pregunta):
    openai.api_key="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"
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role":"user",
                "content":pregunta
            }
        ]
    )
    return respuesta["choices"][0]["message"]["content"]

if __name__ == '__main__':
    app.run(debug=True, port=5000)
