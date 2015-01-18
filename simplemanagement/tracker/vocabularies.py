#-*- coding: utf-8 -*-

from zope.interface import implements
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm
from zope.schema.interfaces import IVocabularyFactory

from plone import api

from collective.simplemanagement.api.content import get_project


class BaseVocabulary(object):
    implements(IVocabularyFactory)

    def __call__(self, context):
        terms = self.get_terms(context)
        return SimpleVocabulary(list(terms))

    def get_dict(self, context):
        return dict(self.get_terms(context))

    def get_terms(self, context):
        raise NotImplementedError()


class Stories(BaseVocabulary):

    def _query(self, project):
        query = {
            'path': {
                'query': '/'.join(project.getPhysicalPath()),
                'depth': -1,
            },
            'sort_on': 'path',
            'sort_order': 'reverse',
            'portal_type': 'Story',
        }
        return query

    def get_terms(self, context):
        catalog = api.portal.get_tool('portal_catalog')
        project = get_project(context)
        for brain in catalog(self._query(project)):
            token = brain.UID
            value = brain.UID
            path = brain.getPath()
            # dirty hack to get a meaningful parent title
            # without waking it up
            prefix = path.split('/')[-2].replace('-', ' ').capitalize()
            title = '{} / {}'.format(prefix, brain.Title)
            yield SimpleTerm(value=value,
                             token=token,
                             title=title)

