from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")

def index():
    
    return render_template('index.html')
    
@app.route("/proceso",methods=['POST'])
def proceso():
    #itulo
    titulo=request.form.get("titulo")
    #autor
    autor=request.form.get("autor")
    #resumen
    resumen=request.form.get("resumen")
    #medio
    medio=request.form.get("medio")
    return render_template("salida.html",ti=titulo,au=autor,re=resumen,me=medio)

if __name__ == "__main__":
    app.run(debug=True)