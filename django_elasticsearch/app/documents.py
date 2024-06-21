from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry

from .models import Blog 

@registry.register_document
class BlogDocument(Document):
    class Index:
        name = "books"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Blog
        fields = ["blog_title", "user_id", "blog_text"]