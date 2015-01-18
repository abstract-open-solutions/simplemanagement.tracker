#-*- coding: utf-8 -*-

from Acquisition import aq_inner
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.watcherlist.utils import su
from zope.i18n import translate

from Products.Poi.browser.notifications import ResolvedIssueMail
from ... import _


class ResolvedStageIssueMail(ResolvedIssueMail):

    index = ViewPageTemplateFile(
        'templates/poi_email_resolved_stage_issue_html.pt')
    plain_index = ViewPageTemplateFile(
        'templates/poi_email_resolved_stage_issue_plain.pt')

    @property
    def subject(self):
        context = aq_inner(self.context)
        tracker = context.getTracker()
        subject = _(
            'poi_email_issue_resolved_prod_subject_template',
            u"[${tracker_title}] Resolved #${issue_id} on stage - ${issue_title}",
            mapping=dict(
                tracker_title=su(tracker.getExternalTitle()),
                issue_id=su(context.getId()),
                issue_title=su(context.Title())))
        # Make the subject unicode and translate it too.
        subject = su(subject)
        subject = translate(subject, 'Poi', context=self.request)
        return subject


class ResolvedProdIssueMail(ResolvedIssueMail):

    index = ViewPageTemplateFile(
        'templates/poi_email_resolved_prod_issue_html.pt')
    plain_index = ViewPageTemplateFile(
        'templates/poi_email_resolved_prod_issue_plain.pt')

    @property
    def subject(self):
        context = aq_inner(self.context)
        tracker = context.getTracker()
        subject = _(
            'poi_email_issue_resolved_prod_subject_template',
            u"[${tracker_title}] Resolved #${issue_id} on prod - ${issue_title}",
            mapping=dict(
                tracker_title=su(tracker.getExternalTitle()),
                issue_id=su(context.getId()),
                issue_title=su(context.Title())))
        # Make the subject unicode and translate it too.
        subject = su(subject)
        subject = translate(subject, 'Poi', context=self.request)
        return subject
