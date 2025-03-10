from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    # Tu môžeš pridať analýzu trhu, predikcie a správy
    market_data = {
        'BTC': random.choice(['Rast', 'Pokles']),
        'ETH': random.choice(['Rast', 'Pokles']),
        'Tesla': random.choice(['Rast', 'Pokles']),
        'Microsoft': random.choice(['Rast', 'Pokles'])
    }
    return render_template('index.html', market_data=market_data)

if __name__ == '__main__':
    app.run(debug=True)
