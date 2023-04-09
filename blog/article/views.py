from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, current_user
from werkzeug.exceptions import NotFound
from werkzeug.utils import redirect

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models.article import Article
from blog.models.author import Author

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')

@article.route('/create/', methods=['GET'])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    return render_template('articles/create.html', form=form)

@article.route('/create/', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)

    if form.validate_on_submit():

        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
        else:
            author = current_user.author

        _article = Article(author_id=author.id, title=form.title.data.strip(), text=form.text.data.strip())

        db.session.add(_article)
        db.session.commit()
        return redirect(url_for('article.get_article', pk=_article.id))
    return render_template('articles/create.html',
                           form=form,
                           )


@article.route('/', methods=['GET'])
def article_list():
    return render_template('articles/list.html',
                           articles=Article.query.all(),
                           )

@article.route('/<int:pk>')
def get_article(pk: int):
    try:
        selected_art = Article.query.filter_by(id=pk).one_or_none()
    except KeyError:
        raise NotFound(f'Article id {pk} is not found')
    return render_template('articles/details.html',
                           art=selected_art
                           )
