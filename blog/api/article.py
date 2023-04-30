import requests
from combojsonapi.event.resource import EventsResource
from flask_combo_jsonapi import ResourceList, ResourceDetail

from blog.extensions import db
from blog.models import Article
from blog.schemas import ArticleSchema


class ArticleCountEvent(EventsResource):
    def event_get_count(self, *args, **kwargs):
        return {'count': Article.query.count()}

    def event_get_filter(self, author_id=1,*args, **kwargs):
        return {'count': Article.query.filter(Article.id == author_id).count()}

    def event_post_count(self, *args, **kwargs):
        return {'method': requests.method}


class ArticleList(ResourceList):
    events = ArticleCountEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }


class ArticleDetailEvent(EventsResource):

    def event_get_count_by_author(self, *args, **kwargs):
        return {'count': Article.query.filter(Article.author_id == kwargs['id']).count()}


class ArticleDetail(ResourceDetail):
    events = ArticleDetailEvent
    schema = ArticleSchema
    data_layer = {
        'session': db.session,
        'model': Article,
    }
