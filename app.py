import json
from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

# Chargement du fichier JSON contenant les langues
with open('languages.json') as f:
    languages = json.load(f)

@app.route('/', methods=['GET', 'POST'])
def translate():
    if request.method == 'POST':
        text = request.form['text']
        source_lang = request.form['source_lang']
        target_lang = request.form['target_lang']

        try:
            source_lang_name = languages[source_lang]
            target_lang_name = languages[target_lang]
            translation = translator.translate(text, src=source_lang, dest=target_lang)
            translated_text = translation.text
            return render_template('index.html', translation=translated_text, languages=languages, source_lang=source_lang, target_lang=target_lang, source_lang_name=source_lang_name, target_lang_name=target_lang_name)
        except KeyError:
            error_message = "Langue non valide sélectionnée"
            return render_template('index.html', error_message=error_message, languages=languages)
    return render_template('index.html', languages=languages)

if __name__ == '__main__':
    app.run()
