from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/delivery')
def delivery():
    return render_template('delivery.html')

@app.route('/gallery')
def gallery():
    images = [
        {
            'src': 'https://raw.githubusercontent.com/awaikoi/OPI-lab03/main/images/shop/Bocchi-the-rock.webp',
            'title': 'Bocchi the Rock',
            'description': 'Коли хотів стати рок-зіркою, але життя внесло свої корективи.'
        },
        {
            'src': 'https://raw.githubusercontent.com/awaikoi/OPI-lab03/main/images/shop/bwaaa.webp',
            'title': 'Bwaaa',
            'description': 'Коли сказали, що сьогодні знову понеділок.'
        },
        {
            'src': 'https://raw.githubusercontent.com/awaikoi/OPI-lab03/main/images/shop/catCobain.webp',
            'title': 'Cat Cobain',
            'description': 'Останній представник гранжу. Його музика торкається душі, а шерсть — нікого не залишає байдужим.'
        },
        {
            'src': 'https://raw.githubusercontent.com/awaikoi/OPI-lab03/main/images/shop/ichu.webp',
            'title': 'Yea, I can’t hear u',
            'description': 'Коли тебе кличуть щось робити, але ти вже морально вийшов із чату.'
        },
        {
            'src': 'https://raw.githubusercontent.com/awaikoi/OPI-lab03/main/images/shop/monster.webp',
            'title': 'Monster',
            'description': 'Коли енергії немає, але дедлайн нікуди не зник.'
        },
        {
            'src': 'https://raw.githubusercontent.com/awaikoi/OPI-lab03/main/images/shop/ryo.webp',
            'title': 'Ryo Yamada',
            'description': 'Коли твій бюджет — нуль, але фінансові рішення все одно залишаються сумнівними.'
        }
    ]

    return render_template('gallery.html', images=images)


if __name__ == '__main__':
    # debug=True: автоматичний перезапуск після змін у коді та детальні повідомлення про помилки.
    # Використовується лише під час розробки.
    app.run(debug=True)
