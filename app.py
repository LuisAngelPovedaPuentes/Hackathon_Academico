from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal
@app.route("/")
@app.route("/hackathon/sistema-seguro")
def index():
    return render_template("index.html")


# Nivel 1 completado
@app.route("/hackathon/sistema-seguro/login")
def login():
    return render_template("inicio.html")


# Nivel 2
@app.route("/nivel2")
def nivel2():
    return render_template("nivel2.html")


# Nivel 3
@app.route("/nivel3")
def nivel3():
    return render_template("nivel3.html")


# Validación login real
@app.route("/validar", methods=["POST"])
def validar():
    user = request.form.get("user")
    password = request.form.get("pass")

    if user == "desarrollador" and password == "zeroday":
        return "<h1>✅ FELICITACIONES LOGRASTE TERMINAR TODO EL RETO</h1>"
    else:
        return "<h1>❌ Acceso denegado</h1>"


if __name__ == "__main__":
    app.run(debug=True)