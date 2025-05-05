from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

if __name__ == '__main__':
    # Habilita o modo de debug para reiniciar automaticamente e exibir erros detalhados
    app.run(debug=True)
