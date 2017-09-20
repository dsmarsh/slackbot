# -*- coding: utf-8 -*-

import os

DEBUG = False

PLUGINS = [
    'slackbot.plugins',
]

ERRORS_TO = None

API_TOKEN = 'XXX'

ALIASES = '/netq'

BOT_EMOJI = ':robot_face:'

DEFAULT_REPLY = "I will run NetQ commands on the cldemo topology"

for key in os.environ:
    if key[:9] == 'SLACKBOT_':
        name = key[9:]
        globals()[name] = os.environ[key]

try:
    from slackbot_settings import *
except ImportError:
    try:
        from local_settings import *
    except ImportError:
        pass

# convert default_reply to DEFAULT_REPLY
try:
    DEFAULT_REPLY = default_reply
except NameError:
    pass
