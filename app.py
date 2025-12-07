from flask import Flask, request, render_template

app = Flask(__name__)

# ---------------------------------------------
# PÁGINA INICIAL
# ---------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")


# ---------------------------------------------
# ÁREAS
# ---------------------------------------------
@app.route("/area/circulo", methods=["GET", "POST"])
def area_circulo():
    resultado = None
    if request.method == "POST":
        raio = float(request.form["raio"])
        resultado = 3.14 * (raio ** 2)
    return render_template("area_circulo.html", resultado=resultado)

@app.route("/area/triangulo", methods=["GET", "POST"])
def area_triangulo():
    resultado = None
    if request.method == "POST"]:
        base = float(request.form["base"])
        altura = float(request.form["altura"])
        resultado = (base * altura) / 2
    return render_template("area_triangulo.html", resultado=resultado)

@app.route("/area/retangulo", methods=["GET", "POST"])
def area_retangulo():
    resultado = None
    if request.method == "POST"]:
        base = float(request.form["base"])
        altura = float(request.form["altura"])
        resultado = base * altura
    return render_template("area_retangulo.html", resultado=resultado)

@app.route("/area/quadrado", methods=["GET", "POST"])
def area_quadrado():
    resultado = None
    if request.method == "POST"]:
        lado = float(request.form["lado"])
        resultado = lado ** 2
    return render_template("area_quadrado.html", resultado=resultado)

@app.route("/area/losango", methods=["GET", "POST"])
def area_losango():
    resultado = None
    if request.method == "POST"]:
        d1 = float(request.form["d1"])
        d2 = float(request.form["d2"])
        resultado = (d1 * d2) / 2
    return render_template("area_losango.html", resultado=resultado)


# ---------------------------------------------
# VOLUMES
# ---------------------------------------------
@app.route("/volume/esfera", methods=["GET", "POST"])
def volume_esfera():
    resultado = None
    if request.method == "POST"]:
        raio = float(request.form["raio"])
        resultado = (4/3) * 3.14 * (raio ** 3)
    return render_template("volume_esfera.html", resultado=resultado)

@app.route("/volume/cubo", methods=["GET", "POST"])
def volume_cubo():
    resultado = None
    if request.method == "POST"]:
        lado = float(request.form["lado"])
        resultado = lado ** 3
    return render_template("volume_cubo.html", resultado=resultado)

@app.route("/volume/cilindro", methods=["GET", "POST"])
def volume_cilindro():
    resultado = None
    if request.method == "POST"]:
        raio = float(request.form["raio"])
        altura = float(request.form["altura"])
        resultado = 3.14 * (raio ** 2) * altura
    return render_template("volume_cilindro.html", resultado=resultado)

@app.route("/volume/piramide", methods=["GET", "POST"])
def volume_piramide():
    resultado = None
    if request.method == "POST"]:
        area_base = float(request.form["area_base"])
        altura = float(request.form["altura"])
        resultado = (area_base * altura) / 3
    return render_template("volume_piramide.html", resultado=resultado)

@app.route("/volume/prisma", methods=["GET", "POST"])
def volume_prisma():
    resultado = None
    if request.method == "POST"]:
        area_base = float(request.form["area_base"])
        altura = float(request.form["altura"])
        resultado = area_base * altura
    return render_template("volume_prisma.html", resultado=resultado)


# ---------------------------------------------
# EQUAÇÕES E JUROS
# ---------------------------------------------
@app.route("/mat/inequacao", methods=["GET", "POST"])
def inequacao():
    resultado = None
    if request.method == "POST"]:
        a = float(request.form["a"])
        b = float(request.form["b"])
        c = float(request.form["c"])
        resultado = (b*b) - (4*a*c)
    return render_template("inequacao.html", resultado=resultado)

@app.route("/mat/juros_simples", methods=["GET", "POST"])
def juros_simples():
    resultado = None
    if request.method == "POST"]:
        capital = float(request.form["capital"])
        taxa = float(request.form["taxa"]) / 100
        tempo = float(request.form["tempo"])
        resultado = capital * taxa * tempo
    return render_template("juros_simples.html", resultado=resultado)

@app.route("/juros_compostos", methods=["GET", "POST"])
def juros_compostos():
    resultado = None
    if request.method == "POST"]:
        capital = float(request.form["capital"])
        taxa = float(request.form["taxa"])
        tempo = float(request.form["tempo"])
        unidade = request.form["unidade"]

        i = taxa / 100
        montante = capital * (1 + i) ** tempo

        resultado = f"Montante final ({unidade}): {montante:.2f}"
    return render_template("juros_compostos.html", resultado=resultado)


# ---------------------------------------------
# CALCULADORA ARITMÉTICA
# ---------------------------------------------
@app.route("/calc/soma", methods=["GET", "POST"])
def calc_soma():
    resultado = None
    if request.method == "POST"]:
        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        resultado = n1 + n2
    return render_template("calc_soma.html", resultado=resultado)

@app.route("/calc/subtracao", methods=["GET", "POST"])
def calc_sub():
    resultado = None
    if request.method == "POST"]:
        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        resultado = n1 - n2
    return render_template("calc_subtracao.html", resultado=resultado)

@app.route("/calc/multiplicacao", methods=["GET", "POST"])
def calc_mult():
    resultado = None
    if request.method == "POST"]:
        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        resultado = n1 * n2
    return render_template("calc_multiplicacao.html", resultado=resultado)

@app.route("/calc/divisao", methods=["GET", "POST"])
def calc_div():
    resultado = None
    if request.method == "POST"]:
        n1 = float(request.form["n1"])
        n2 = float(request.form["n2"])
        if n2 == 0:
            resultado = "Erro: divisão por zero."
        else:
            resultado = n1 / n2
    return render_template("calc_divisao.html", resultado=resultado)

@app.route("/calc/quadratica", methods=["GET", "POST"])
def calc_quadratica():
    resultado = None
    if request.method == "POST"]:
        a = float(request.form["a"])
        b = float(request.form["b"])
        c = float(request.form["c"])
        delta = b*b - 4*a*c

        if delta < 0:
            resultado = "Não existem raízes reais."
        else:
            x1 = (-b + delta**0.5) / (2*a)
            x2 = (-b - delta**0.5) / (2*a)
            resultado = f"x1 = {x1:.2f}, x2 = {x2:.2f}"
    return render_template("calc_quadratica.html", resultado=resultado)


# ---------------------------------------------
# INICIALIZAÇÃO
# ---------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
