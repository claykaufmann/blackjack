from flask import Flask
import json

app = Flask(__name__)


@app.route('/')
def app():  # put application's code here
    deck = Deck()


    return "hi"

@app.route('/shuffle')
def shuffle():
    deck.random()


@app.route('/deal_card')
def deal_card():

    json = json

    card = json.card



if __name__ == '__main__':
    app.run()
