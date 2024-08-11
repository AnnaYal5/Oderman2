from flask import Flask,render_template
app = Flask(__name__)

pizzas = [
    {'name': "Маргарита", "ingredients": "соус , сир, базилік", "price": "150 грн"},
    {'name': "Папероні", "ingredients": "соус , сир, папероні", "price": "190 грн"},
    {'name': "Гавайська", "ingredients": "соус , сир, ананас, шинка", "price": "200 грн"}
]

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/menu')
def menu():
    return render_template('menu.html',pizzas=pizzas)

if __name__ ==  '__main__':
    app.run(debug=True)
