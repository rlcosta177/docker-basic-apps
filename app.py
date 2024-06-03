from flask import Flask, request, jsonify

app = Flask(__name__)

# Translation dictionaries
translations = {
    'english_to_portuguese': {
        'red': 'vermelho',
        'orange': 'laranja',
        'yellow': 'amarelo',
        'green': 'verde',
        'blue': 'azul',
        'indigo': 'índigo',
        'violet': 'violeta'
    },
    'portuguese_to_english': {
        'vermelho': 'red',
        'laranja': 'orange',
        'amarelo': 'yellow',
        'verde': 'green',
        'azul': 'blue',
        'índigo': 'indigo',
        'violeta': 'violet'
    },
    'portuguese_to_french': {
        'vermelho': 'rouge',
        'laranja': 'orange',
        'amarelo': 'jaune',
        'verde': 'vert',
        'azul': 'bleu',
        'índigo': 'indigo',
        'violeta': 'violet'
    },
    'french_to_portuguese': {
        'rouge': 'vermelho',
        'orange': 'laranja',
        'jaune': 'amarelo',
        'vert': 'verde',
        'bleu': 'azul',
        'indigo': 'índigo',
        'violet': 'violeta'
    }
}

@app.route('/translate', methods=['GET'])
def translate():
    color = request.args.get('color')
    target_language = request.args.get('target_language')
    if not color or not target_language:
        return jsonify({'error': 'Please provide both color and target_language parameters'}), 400
    
    key = f'{request.args.get("source_language")}_to_{target_language}'
    
    if key in translations and color in translations[key]:
        return jsonify({'translated_color': translations[key][color]})
    else:
        return jsonify({'error': 'Translation not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
