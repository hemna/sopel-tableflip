# -*- coding: utf-8 -*-
import sopel.module


# matching exactly @!
@sopel.module.rule('\@\?$')
def flip_help(bot, trigger):
    flip = "(╯°□°)╯︵ ┻━┻ ".decode("utf-8")
    bot.say("Welcome to Table flipping bot.")
    bot.say(flip)
    bot.say("@!           - Standard table flip.")
    bot.say("@!b <nick>   - Battle another nick table flip.")
    bot.say("@!d <nick>   - Battle win another nick table flip.")
    bot.say("@!f          - Fat table flip.")
    bot.say("@!h          - Hercules table flip.")
    bot.say("@!j          - Jedi table flip.")
    bot.say("@!z          - Bear table flip.")


# matching exactly @!
@sopel.module.rule('\@\!$')
def flip(bot, trigger):
    flip = "(╯°□°)╯︵ ┻━┻ ".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)


# matching @!f
@sopel.module.rule('\@\!f')
def flip_fat(bot, trigger):
    flip = "(ノ ゜Д゜)ノ ︵ ┻━┻".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)


# matching @!z
@sopel.module.rule('\@\!z')
def flip_bear(bot, trigger):
    flip = "ʕノ•ᴥ•ʔノ ︵ ┻━┻".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)


# matching @!h
@sopel.module.rule('\@\!h')
def flip_hercules(bot, trigger):
    flip = "(/ .□.) ︵╰(゜Д゜)╯︵ /(.□. )".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)


# matching @!j
@sopel.module.rule('\@\!j')
def flip_jedi(bot, trigger):
    flip = "(._.) ~ ︵ ┻━┻".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)


# matching @!d
# also appends anything after @!d to end of message
@sopel.module.rule('\@\!d')
def flip_dude(bot, trigger):
    flip = "(╯°Д°）╯︵ /(.□ . )".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    other = str(trigger).replace('@!d', '')
    bot.say(flip1 + other)


# matching @!b
# also appends anything after @!b to end of message
@sopel.module.rule('\@\!b')
def flip_battle(bot, trigger):
    flip = "(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    other = str(trigger).replace('@!b', '')
    bot.say(flip1 + other)
