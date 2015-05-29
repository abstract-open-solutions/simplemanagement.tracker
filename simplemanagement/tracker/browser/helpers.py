#-*- coding: utf-8 -*-

from Products.Five.browser import BrowserView

# from plone.memoize.view import memoize_contextless

# from .. import api
from ..extenders import STORY_FIELDNAME
from ..extenders import DEADLINE_FIELDNAME
from ..extenders import ESTIMATE_FIELDNAME


class Helpers(BrowserView):

    def story(self):
        """ get the story from issue
        """
        field = self.context.getField(STORY_FIELDNAME)
        story = field.get(self.context)
        return story

    def deadline(self):
        """ get the story from issue
        """
        field = self.context.getField(DEADLINE_FIELDNAME)
        deadline = field.get(self.context)
        return deadline

    def estimate(self):
        """ get the story from issue
        """
        field = self.context.getField(ESTIMATE_FIELDNAME)
        estimate = field.get(self.context)
        return estimate
