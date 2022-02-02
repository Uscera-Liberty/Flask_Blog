import sqlite3

connection = sqlite3.connect('database.db')
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.execute("INSERT INTO posts (title, content,comment) VALUES (?, ? , ?)",
            ('Мейн-кун', 'Одной из самых удивительных и загадочных пород считается мейн-кун – ласковый гигант с серьезным взглядом. Этих созданий называют «комнатными рысями», что неудивительно, т.к. они одни из самых крупных домашних кошек.','ty')
            )

cur.execute("INSERT INTO posts (title, content,comment) VALUES (?, ? , ?)",
            ('Шотландская вислоухая', 'Во всём мире эту породу именуют «скоттиш-фолд», но нам привычней называть этих милых кошек «шотландскими вислоухими». Их «няшная» внешность никого не оставит равнодушным – такое создание сразу хочется взять на руки и затискать.', 'ty')
            )


connection.commit()
connection.close()