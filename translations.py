# translations.py
color_translations = {
    'english': {
        'red': 'vermelho',
        'orange': 'laranja',
        'yellow': 'amarelo',
        'green': 'verde',
        'blue': 'azul',
        'indigo': 'índigo',
        'violet': 'violeta'
    },
    'portuguese': {
        'vermelho': 'red',
        'laranja': 'orange',
        'amarelo': 'yellow',
        'verde': 'green',
        'azul': 'blue',
        'índigo': 'indigo',
        'violeta': 'violet',
        'vermelho': 'rouge',
        'laranja': 'orange',
        'amarelo': 'jaune',
        'verde': 'vert',
        'azul': 'bleu',
        'índigo': 'indigo',
        'violeta': 'violet'
    },
    'french': {
        'rouge': 'vermelho',
        'orange': 'laranja',
        'jaune': 'amarelo',
        'vert': 'verde',
        'bleu': 'azul',
        'indigo': 'índigo',
        'violet': 'violeta'
    }
}

# Helper function to handle translations
def translate_color(color, from_lang, to_lang):
    if from_lang == 'english' and to_lang == 'portuguese':
        return color_translations['english'].get(color, 'unknown')
    elif from_lang == 'portuguese' and to_lang == 'english':
        return color_translations['portuguese'].get(color, 'unknown')
    elif from_lang == 'portuguese' and to_lang == 'french':
        eng_color = color_translations['portuguese'].get(color, 'unknown')
        return color_translations['french'].get(eng_color, 'unknown')
    elif from_lang == 'french' and to_lang == 'portuguese':
        port_color = color_translations['french'].get(color, 'unknown')
        return port_color
    else:
        return 'unknown'
