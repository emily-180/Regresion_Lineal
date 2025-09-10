from flask import Flask, render_template, redirect, url_for, request
import regressionLinear
app = Flask(__name__)

@app.route("/")  
def home():
   
    return redirect(url_for("index"))

@app.route("/index")
def index():
    myname = "Flask"
    return render_template("index.html", myname=myname)

@app.route("/lr", methods=["GET"])
def lr_form():
    return render_template("lr.html", grafico=None, result=None)

@app.route("/lr", methods=["POST"])
def lr_result():
    cantidad = float(request.form["cantidad"])
    costo = float(request.form["costo"])
    calculateResult = regressionLinear.calcularPrecio(cantidad, costo)
    grafico = regressionLinear.generarGrafico(cantidad, costo, calculateResult)

    return render_template("lr.html", result=calculateResult, grafico=grafico)


@app.route("/conceptos")
def conceptos():
    return render_template("conceptos.html")

if __name__ == "__main__":
    app.run(debug=True)