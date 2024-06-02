from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

def get_crypto_price(coin_symbol):
     url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
     response = requests.get(url)
     if response.status_code == 200:
        data = response.json()
        btc_price = data["price"]
        return btc_price
     else:
        return None
    

def get_ephirium_price(coin_symbol):
     url = ""
     response = requests.get(url)
     if response.status_code == 200:
        data = response.json()
        ephirium_price = data["price"]
        return ephirium_price
     else:
        return None

@app.route ('/')
def home():
    return render_template('index.html')

    return render_template('epherium.html')
@app.route('/bitcoin')
def index():
    return render_template('bitcoin.html')

@app.route('/get_price')
def get_price():
    crypto_price = get_crypto_price('BTC')
    if crypto_price is not None:
        return jsonify({'crypto_price': crypto_price})
    else:
        return jsonify({'error': 'Failed to get Bitcoin price'})

if __name__ == '__main__':
    app.run(debug=True)
