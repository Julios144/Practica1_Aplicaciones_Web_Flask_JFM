from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")

def index():
    
    return render_template('index.html')
    
@app.route("/proceso",methods=['POST'])
def proceso():
    #producto
    producto=request.form.get("producto")
    #categoria
    categoria =request.form.getlist("categoria")
    #existencia
    existencia=request.form.get("existencia")
    #precio
    precio=request.form.get("precio")
    
    return render_template("salida.html",pro=producto,cate=categoria,exis=existencia,pre=precio)

if __name__ == "__main__":
    app.run(debug=True)