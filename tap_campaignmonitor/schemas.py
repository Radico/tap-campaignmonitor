#!/usr/bin/env python3
import os
import singer
from singer import utils


class IDS(object):
    CAMPAIGNS = 'campaigns'
    SUPPRESSIONLIST = 'suppressionlist'
    RECIPIENTS = 'recipients'
    BOUNCES = 'bounces'
    OPENS = 'opens'
    CLICKS = 'clicks'
    UNSUBSCRIBES = 'unsubscribes'
    SPAM = 'spam'


stream_ids = [getattr(IDS, x) for x in dir(IDS)
              if not x.startswith('__')]

PK_FIELDS = {
    IDS.CAMPAIGNS: ['campaign_id'],
    IDS.SUPPRESSIONLIST: ['EmailAddress'],
    IDS.RECIPIENTS: ['EmailAddress'],
    IDS.BOUNCES: ['EmailAddress'],
    IDS.OPENS: ['EmailAddress'],
    IDS.CLICKS: ['EmailAddress'],
    IDS.UNSUBSCRIBES: ['EmailAddress'],
    IDS.SPAM: ['EmailAddress'],
}


def get_abs_path(path):
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), path)


def load_schema(tap_stream_id):
    path = "schemas/{}.json".format(tap_stream_id)
    return utils.load_json(get_abs_path(path))


def load_and_write_schema(tap_stream_id):
    schema = load_schema(tap_stream_id)
    singer.write_schema(tap_stream_id, schema, PK_FIELDS[tap_stream_id])
