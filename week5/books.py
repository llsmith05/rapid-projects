from flask import Flask, request, render_template
from string import upper
from random import random, shuffle
from copy import deepcopy

app = Flask(__name__)

@app.route('/view/')
def hello(name=None):
    return render_template('book.html')

# @app.route('/view/')
@app.route('/view/<book_id>')
def view(book_id=None):

    # print 'in there'



    book_id = int(book_id)

    # print 'casting'
    # print BOOKS_LIST

    title = BOOKS_LIST[book_id][0]

    # print 'retrieving '

    author = BOOKS_LIST[book_id][1]
    price = BOOKS_LIST[book_id][2]
    # print type(price)
    # # description = "some text ..."
    # print 'Title = %s author = %s price = %s' % (title, author)
    # print 'ready to serve'

    # return 'Title = %s author = %s price = %s ' % (title, author, price)
    return render_template('book.html', title=title, author=author,
                           price=price)

@app.route('/search')
def lolsearch():
    return 'NO RESULTS'

@app.route('/search', methods=['GET'])
def search():

    try:
        number = int(request.args.get('n', ''))
        query = request.args.get('query', '')
    except KeyError:
        return 'No results found!'


    list_of_results = []

    for element in BOOKS_LIST:
        # print element
        if query in element[0]:
            # print len(list_of_results)
            list_of_results.append(element)

        if  len(list_of_results) >= number:
            break
    # return '%s' % str(list_of_results)
    return render_template('search.html', list_of_results=list_of_results)

@app.route('/bestof', methods=['GET'])
def bestof():

    try:
        genre = request.args.get('genre', '')
    except KeyError:
        genre = 'No genre specified'

    copy_of_list = deepcopy(BOOKS_LIST)
    shuffle(copy_of_list)

    # return genre name
    # 
    # return 'Genre is: %s Results: %s' % (genre, str(copy_of_list[0:4]))
    return render_template('bestof.html', genre_name=genre,
                           list_of_results=copy_of_list)


BOOKS_STRING = u"""100 BILIMSEL DENEY	ANDREWS
10'A KADAR SAYMAK	TYLER
21.YUZYIL	TUBI
ASTRONOMI	ATKINSON
ATIK MI?  HIC DERT DEGIL !   	MORICHON
ATOM VE MOLEKUL	COX
AY'A INIS	TUBI
AYAK IZLERININ ESRARI	CALHOUN
AY'DA	TUBI
BENDE DISLEKSI VAR	MOORE
BILGISAYAR NE SAYAR    Rakk.Evren.Tarihi IX	IFRAH
BILGISAYARDAKI ADRESINIZ WEB SITESI	KALBAG
BILGISAYARLAR	STEPHENS
BILIM ADAMLARI	REID
BILIM KONUSMALARI	TUBI
BILIMSEL DENEYLER	BINGHAM
BILIMSEL GAFLAR	ARONSON
BIR TIP GOZLEMCISININ NOTLARI	THOMAS
BIR UCTAN DIGER UCA DUNYA COCUKLARI	ROCA
BIR YESILIN PESINDE  	ZIHNIOGLU
BIR ZAMANLAR   	MCNEIL
BITKILER	KINDERSLEY
BUNU ANCAK DR ECCO COZER	SHASHA
CEVREMIZ ve BIZ / Hava	ROCA
CEVREMIZ ve BIZ / Yeryuzu	ROCA
COCUK OLMAK ZOR	MOORE-MALLINOS
DENEYLERLE BILIM 1. KITAP	EDOM
DENEYLERLE BILIM 2. KITAP	EDOM
DENEYLERLE BILIM 3. KITAP	HEDDLE
DENIZDEKI 1001 SEYI BULUN	DAYNES
DENIZLER VE OKYANUSLAR	BROOKS
DIS HEKIMINDE	CIVARDI
DOKTORDA	CIVARDI
DUNYA ve UZAY	MAYES
DUNYAYI SARAN AG WWW    	KALBAG
EKOLOJI	SPURGEON
EKOLOJIK SORUNLAR VE COZUMLERI	CEPEL
ENERJI ve GUC	SPURGEON
E-POSTA	WALLACE
FIRTINALAR VE KASIRGALAR    	GEMMELL
GEZEGENLER KILAVUZU   	MOORE
HAH, BULDUM	GARDNER
HASTANEDE	CIVARDI
HAVA ve IKLIM	WATT
HAVADA KARADA SUDA  	LITTLE
HAYDI OGRENELIM / Atma, Kullan !	ROCA
HAYDI OGRENELIM / Dort Element	ROCA
ZAMAN VE UZAY      	TUBI"""

BOOKS_LIST = [element.split('\t')+[str(random()*100)] for element in BOOKS_STRING.split('\n')]

if __name__ == "__main__":
    app.run()
