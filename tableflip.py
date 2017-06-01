# -*- coding: utf-8 -*-
import random

import sopel.module


# matching exactly @!
@sopel.module.rule('\@\?$')
def flip_help(bot, trigger):
    flip = "(╯°□°)╯︵ ┻━┻ ".decode("utf-8")
    bot.say("Welcome to Table flipping bot.")
    bot.say(flip)
    bot.say("@!           - Hello.")
    bot.say("@!b <nick>   - Battle another nick table flip.")
    bot.say("@!c          - Covfefe table flip.")
    bot.say("@!d <nick>   - Battle win another nick table flip.")
    bot.say("@!f          - Fat table flip.")
    bot.say("@!g          - The Finger table flip.")
    bot.say("@!h          - Hercules table flip.")
    bot.say("@!j          - Jedi table flip.")
    bot.say("@!m          - Magic table flip.")
    bot.say("@!r          - Rage table flip.")
    bot.say("@!t          - Standard table flip.")
    bot.say("@!z          - Bear table flip.")


# matching exactly @!
@sopel.module.rule('\@\!$')
def flip(bot, trigger):
    hi_list = [
        "( ･ω･)ﾉ",
        "( ^_^)／",
        "(^o^)/",
        "( ´ ▽ ` )ﾉ",
        "(=ﾟωﾟ)ﾉ",
        "( ・_・)ノ",
        "(。･∀･)ﾉ",
        "(*ﾟ͠ ∀ ͠)ﾉ",
        "(♦亝д 亝)ﾉ",
        "( *՞ਊ՞*)ﾉ",
        "(｡Ő▽Ő｡)ﾉﾞ",
        "(ஐ╹◡╹)ノ",
        "(✧∇✧)╯",
        "(^▽^)/ ʸᵉᔆᵎ",
        "(。･д･)ﾉﾞ",
        "(◍˃̶ᗜ˂̶◍)ﾉ”",
        "(*´･д･)ﾉ",
        "|。･ω･|ﾉ",
        "(ه’́⌣’̀ه )／",
        "ヽ(´･ω･`)､",
        "ヘ(°￢°)ノ",
        "＼(-_- )",
        "(¬_¬)ﾉ",
        "(;-_-)ノ",
        "(^-^*)/",
        "＼( ･_･)",
        "ヾ(-_-;)",
        "|ʘ‿ʘ)╯"
    ]

    index = random.randint(0, len(hi_list)-1)

    flip = hi_list[index].decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)


# matching @!b
# also appends anything after @!b to end of message
@sopel.module.rule('\@\!b')
def flip_battle(bot, trigger):
    flip = "(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    other = str(trigger).replace('@!b', '')
    bot.say(flip1 + other)


# matching @!c
@sopel.module.rule('\@\!c')
def flip_covfefe(bot, trigger):
    flip = "༼ノಠل͟ಠ༽ノ ︵ ┻━┻".decode("utf-8")
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


# matching @!f
@sopel.module.rule('\@\!f')
def flip_fat(bot, trigger):
    flip = "(ノ ゜Д゜)ノ ︵ ┻━┻".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)


# matching @!g
@sopel.module.rule('\@\!g')
def flip_finger(bot, trigger):
    flip = "╭∩╮◕ل͜◕)╭∩╮  ︵┻┻".decode("utf-8")
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


# matching @!m
@sopel.module.rule('\@\!m')
def flip_magic(bot, trigger):
    flip = "༼∩ຈل͜ຈ༽つ━☆ﾟ.*･｡ﾟ ︵ ┻━┻".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)


# matching @!r
@sopel.module.rule('\@\!r')
def flip_rage(bot, trigger):
    flip = "(ノಠ益ಠ)ノ彡┻━┻".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)


# matching @!t
@sopel.module.rule('\@\!t')
def flip_table(bot, trigger):
    flip = "(╯°□°)╯︵ ┻━┻ ".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)


# matching @!z
@sopel.module.rule('\@\!z')
def flip_bear(bot, trigger):
    flip = "ʕノ•ᴥ•ʔノ ︵ ┻━┻".decode("utf-8")
    flip1 = ('%s %s' % (trigger.nick, flip))
    bot.say(flip1)
