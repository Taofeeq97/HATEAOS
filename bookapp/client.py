from algoliasearch.search_client import SearchClient
from algoliasearch_django import algolia_engine
from .models import BlogArticle


def get_client():
    return algolia_engine.client


def get_index(index_name="bookindex"):
    client = get_client()
    index = client.init_index(index_name)
    return index