# -*- coding: utf-8 -*-

from plone.app.uuid.utils import uuidToObject

from collective.watcherlist.interfaces import IWatcherList

from .extenders import STORY_FIELDNAME


def booking_added(booking, evt):
    """ track ticket story on booking
    """
    if booking.ticket:
        ticket = uuidToObject(booking.ticket)
        field = ticket.getField(STORY_FIELDNAME)
        story = field and field.get(ticket) or None
        booking.add_reference(story.portal_type, story.UID())


def mail_issue_change(object, event):
    """Send an email on some transitions of an issue.

    Specifically: resolved issue on stage and prod
    """
    if event.new_state.id in ('resolved-stage',
                              'resolved-prod'):
        watchers = IWatcherList(object)
        # Only mail the original poster, if available.
        address = object.getContactEmail()
        if address:
            watchers.send("{}-issue-mail".format(event.new_state.id),
                          only_these_addresses=[address])
