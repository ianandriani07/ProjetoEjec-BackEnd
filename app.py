from flask import Flask, render_template

app = Flask(__name__)

@app.route("/projetos")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/Prazo")
def Prazsdfo():
    return render_template('landingpage.html')
    
if __name__ == '__main__':
    app.run()