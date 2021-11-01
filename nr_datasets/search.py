from flask import current_app
from invenio_indexer.api import RecordIndexer
from oarepo_communities.search import CommunitySearch


class DatasetRecordsSearch(CommunitySearch):
    LIST_SOURCE_FIELDS = [
        'InvenioID', 'oarepo:validity.valid', 'oarepo:draft',
        'titles', 'abstract', 'creators', 'dateCreated', 'dateAvailable', 'resourceType', 'accessRights', 'rights',
        'contributors', 'keywords', 'subjectCategories', 'relatedItems', 'oarepo:recordStatus', 'language',
        'oarepo:primaryCommunity', 'oarepo:secondaryCommunities', '$schema', '_files'
    ]
    HIGHLIGHT_FIELDS = {
        'titles.title.cs': None,
        'titles.title._': None,
        'titles.title.en': None
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # https://www.elastic.co/guide/en/elasticsearch/reference/current/search-aggregations.html#return-agg-type
        typed_keys = current_app.config.get("NR_ES_TYPED_KEYS", False)
        self._params = {'typed_keys': typed_keys}

class CommitingRecordIndexer(RecordIndexer):
    def __init__(self, _refresh= None, *args, **kwargs):
        self._refresh = True
        super().__init__(*args, **kwargs)
