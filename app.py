from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
app.secret_key = "hackathon_secret"


# Página principal
@app.route("/")
@app.route("/hackathon/sistema-seguro")
def index():

    session.clear()

    return render_template("index.html")


# Nivel 1
@app.route("/hackathon/sistema-seguro/login")
def login():

    session["nivel1"] = True

    return render_template("inicio.html")


# Activar nivel 2
@app.route("/activar_nivel2")
def activar_nivel2():

    if not session.get("nivel1"):
        return "<h1>⛔ Acceso no autorizado</h1>"

    session["nivel2"] = True

    return redirect("/nivel2")


# Nivel 2
@app.route("/nivel2")
def nivel2():

    if not session.get("nivel2"):
        return "<h1>⛔ Acceso no autorizado</h1>"

    return render_template("nivel2.html")


# Activar nivel 3
@app.route("/activar_nivel3")
def activar_nivel3():

    if not session.get("nivel2"):
        return "<h1>⛔ Acceso no autorizado</h1>"

    session["nivel3"] = True

    return redirect("/nivel3")


# Nivel 3
@app.route("/nivel3")
def nivel3():

    if not session.get("nivel3"):
        return "<h1>⛔ Acceso no autorizado</h1>"

    return render_template("nivel3.html")


# Validación login real
@app.route("/validar", methods=["POST"])
def validar():
    user = request.form.get("user")
    password = request.form.get("pass")

    if user == "desarrollador" and password == "zeroday":
        return render_template("Reto_completado.html")
    else:
        return "<h1>❌ Acceso denegado</h1>"
    
    # Pantalla final
    @app.route("/Reto_completado")
    def final():
        return render_template("Reto_completado.html")


if __name__ == "__main__":
    app.run(debug=True)