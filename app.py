from flask import Flask, render_template # O último flask é maiusculo por que é uma classe.

app = Flask('Olá') # Variável - Usamos para guardar valores, guardamos dentor de uma variável

@app.route('/') # Criando uma rota( rota = /(Barra))
def ola(): # Função(def) com parametro(ola():)
   return render_template('ola.html')    
    
@app.route('/aluno') #Cria outra rota, é só colocar /aluno na url que aprece quando manda flask run.
def aluno():
   return render_template("Diego, Geissy, Guilherme")
    
    























































