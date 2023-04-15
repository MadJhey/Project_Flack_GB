from flask import Blueprint, render_template, request, url_for
from flask_login import login_required, current_user
from sqlalchemy.orm import joinedload
from werkzeug.exceptions import NotFound
from werkzeug.utils import redirect

from blog.extensions import db
from blog.forms.article import CreateArticleForm
from blog.models.tag import Tag
from blog.models.article import Article
from blog.models.author import Author

article = Blueprint('article', __name__, url_prefix='/articles', static_folder='../static')


@article.route('/create/', methods=['GET'])
@login_required
def create_article_form():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    return render_template('articles/create.html', form=form)


@article.route('/create/', methods=['POST'])
@login_required
def create_article():
    form = CreateArticleForm(request.form)
    form.tags.choices = [(tag.id, tag.name) for tag in Tag.query.order_by('name')]
    if form.validate_on_submit():

        if not current_user.author:
            author = Author(user_id=current_user.id)
            db.session.add(author)
            db.session.flush()
        else:
            author = current_user.author

        _article = Article(author_id=author.id, title=form.title.data.strip(), text=form.text.data.strip())

        if form.tags.data:
            selected_tags = Tag.query.filter(Tag.id.in_(form.tags.data))
            for tag in selected_tags:
                _article.tag.append(tag)

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
        selected_art = Article.query.filter_by(id=pk).options(joinedload(Article.tag)).one_or_none()
    except KeyError:
        raise NotFound(f'Article id {pk} is not found')
    return render_template('articles/details.html',
                           art=selected_art
                           )

@article.route('/tag/<int:pk>')
def tag_article_list(pk: int):
    try:
        tag = Tag.query.filter_by(id=pk).one_or_none()
    except KeyError:
        raise NotFound(f'Tag id {pk} is not found')
    articles = tag.article
    return render_template('tags/details.html',
                           articles=articles, tag_name=tag.name,
                           )

