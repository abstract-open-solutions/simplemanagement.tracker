#-*- coding: utf-8 -*-
from DateTime import DateTime
from zope.component import adapts
from zope.interface import implements

from Products.Archetypes import atapi
from Products.Poi.interfaces import IIssue

from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import IOrderableSchemaExtender
from archetypes.schemaextender.interfaces import ISchemaModifier
from archetypes.schemaextender.interfaces import IBrowserLayerAwareExtender

from archetypes.referencebrowserwidget import ReferenceBrowserWidget

from .interfaces import ILayer
from . import _


STORY_FIELDNAME = "sm_story"
DEADLINE_FIELDNAME = "sm_deadline"
ESTIMATE_FIELDNAME = "sm_estimate"


class _ExtensionReferenceField(ExtensionField, atapi.ReferenceField):
    pass


class _ExtensionFixedPointField(ExtensionField, atapi.FixedPointField):
    pass


class _ExtensionDatetimeField(ExtensionField, atapi.DateTimeField):
    pass


class StoryExtender(object):
    adapts(IIssue)
    implements(IOrderableSchemaExtender,
               IBrowserLayerAwareExtender,
               ISchemaModifier)

    layer = ILayer

    fields = [
        _ExtensionReferenceField(
            STORY_FIELDNAME,
            allowable_content_types='text/plain',
            vocabulary_factory='sm.tracker.project_stories',
            allowed_types=('Story', ),
            relationship='issue_story',
            widget=ReferenceBrowserWidget(
                label=_(u"Story"),
                allow_browse=0,
                allow_search=1,
                allow_sorting=1,
                force_close_on_insert=1,
                show_indexes=0,
                show_results_without_query=1,
                default_search_index='SearchableText',
                base_query='issue_stories_base_query_getter',
            )

        ),
        _ExtensionDatetimeField(
            DEADLINE_FIELDNAME,
            required=False,
            default_method=DateTime,
            widget=atapi.CalendarWidget(
                description='',
                label=_(u'Deadline')
            )
        ),
        _ExtensionFixedPointField(
            ESTIMATE_FIELDNAME,
            required=False,
            default='0.0',
            widget=atapi.DecimalWidget(
                description='',
                label=_(u'Estimate')
            )
        ),
    ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        return self.fields

    def getOrder(self, original):
        """
        'original' is a dictionary where the keys are the names of
        schemata and the values are lists of field names, in order.
        """
        return original

    def fiddle(object, schema):
        return schema
