from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['GET'])
def translate():
    color = request.args.get('color')
    from_lang = request.args.get('from_lang')
    to_lang = request.args.get('to_lang')

    # Translate color logic here...

    return render_template('index.html', color=color, from_lang=from_lang, to_lang=to_lang)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
