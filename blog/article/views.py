from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

ARTICLES = {
    1: {'title': "It",
        'text': '123321',
        'author': 1},
    2: {'title': "Blood",
        'text': '3214556',
        'author': 2},
    3: {'title': "Flood",
        'text': '214556',
        'author': 1}
}


@article.route('/')
def article_list():
    return render_template('articles/list.html',
                           articles=ARTICLES
                           )


@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        art = ARTICLES[pk]
    except KeyError:
        raise NotFound(f'Article id {pk} is not found')
        # return redirect('/users/')
    return render_template('articles/details.html',
                           art=art
                           )
