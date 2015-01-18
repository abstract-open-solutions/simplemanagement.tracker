#-*- coding: utf-8 -*-

from Products.Five.browser import BrowserView

from collective.simplemanagement.api.content import get_project


class IssueStoriesQueryGetter(BrowserView):

    def __call__(self):
        project = get_project(self.context)
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
