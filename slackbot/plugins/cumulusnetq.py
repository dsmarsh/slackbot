#!/usr/bin/env python
#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to
from subprocess import Popen
import subprocess

@listen_to('^netq$')
def netq_help_reply(message):
    netq_output = subprocess.check_output(["netq"])
    message.reply('```{}```'.format(netq_output))

@listen_to('^netq (.*)')
def netq_reply(message, netq_args):
    netq_command = "netq " + netq_args
    print "command sent: \n" + netq_command

    process = Popen(netq_command.split(' '), stdout=subprocess.PIPE)
    netq_output = process.communicate()[0]
    netq_output = re.sub('\\b          \[0m\\b|\[0m|\[9[12]m', '', netq_output)
    print "output from command: \n" + netq_output

    if len(netq_output) > 4000:
      message.channel.upload_content('netq_long_output.txt', netq_output)
    else:
      message.reply('```{}```'.format(netq_output))
