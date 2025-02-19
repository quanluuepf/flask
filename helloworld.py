from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/barcola')
def barcola():
    return render_template('barcola.html')

@app.route('/beraldo')
def beraldo():
    return render_template('beraldo.html')

@app.route('/dembele')
def dembele():
    return render_template('dembele.html')

@app.route('/donnarumma')
def donnarumma():
    return render_template('donnarumma.html')

@app.route('/doue')
def doue():
    return render_template('doue.html')

@app.route('/hakimi')
def hakimi():
    return render_template('hakimi.html')

@app.route('/hernandez')
def hernandez():
    return render_template('hernandez.html')

@app.route('/kimpembe')
def kimpembe():
    return render_template('kimpembe.html')

@app.route('/kvaratskhelia')
def kvaratskhelia():
    return render_template('kvaratskhelia.html')

@app.route('/lee')
def lee():
    return render_template('lee.html')

@app.route('/marquinhos')
def marquinhos():
    return render_template('marquinhos.html')

@app.route('/mayulu')
def mayulu():
    return render_template('mayulu.html')

@app.route('/mendes')
def mendes():
    return render_template('mendes.html')

@app.route('/neves')
def neves():
    return render_template('neves.html')

@app.route('/pacho')
def pacho():
    return render_template('pacho.html')

@app.route('/ramos')
def ramos():
    return render_template('ramos.html')

@app.route('/ruiz')
def ruiz():
    return render_template('ruiz.html')

@app.route('/safonov')
def safonov():
    return render_template('safonov.html')

@app.route('/tenas')
def tenas():
    return render_template('tenas.html')

@app.route('/vitinha')
def vitinha():
    return render_template('vitinha.html')

@app.route('/zague')
def zague():
    return render_template('zague.html')

@app.route('/zaire-emery')
def zaire_emery():
    return render_template('zaire-emery.html')
    

if __name__ == '__main__':
    app.run()