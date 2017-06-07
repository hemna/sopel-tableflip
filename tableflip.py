# -*- coding: utf-8 -*-
import random

import sopel.module
from sopel import formatting


# matching exactly @!
@sopel.module.rule('\@\?$')
def flip_help(bot, trigger):
    #flip = "(╯°□°)╯︵ ┻━┻ ".decode("utf-8")
    flip = formatting.color("(╯°□°)╯︵ ┻━┻ ", formatting.colors.RED)
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


def _prep_colors(nick, flip):
    return (formatting.color(nick, formatting.colors.BLUE),
            formatting.color(flip, formatting.colors.RED))


def _build_msg(trigger, flip, replace_str=None):
    nick, flip = _prep_colors(trigger.nick, flip)
    msg = "%s %s" % (nick, flip)
    if replace_str and trigger:
        other = str(trigger).replace(replace_str, '')
        return msg + other
    else:
        return msg


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

    #flip = hi_list[index].decode("utf-8")
    flip = hi_list[index]
    msg = _build_msg(trigger, flip)
    bot.say(msg)


# matching @!b
# also appends anything after @!b to end of message
@sopel.module.rule('\@\!b')
def flip_battle(bot, trigger):
    #flip = "(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)".decode("utf-8")
    flip = "(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)"
    msg = _build_msg(trigger, flip, replace_str="@!b")
    bot.say(msg)


# matching @!c
@sopel.module.rule('\@\!c')
def flip_covfefe(bot, trigger):
    #flip = "༼ノಠل͟ಠ༽ノ ︵ ┻━┻".decode("utf-8")
    flip = "༼ノಠل͟ಠ༽ノ ︵ ┻━┻"
    msg = _build_msg(trigger, flip)
    bot.say(msg)


# matching @!d
# also appends anything after @!d to end of message
@sopel.module.rule('\@\!d')
def flip_dude(bot, trigger):
    #flip = "(╯°Д°）╯︵ /(.□ . )".decode("utf-8")
    flip = "(╯°Д°）╯︵ /(.□ . )"
    msg = _build_msg(trigger, flip, replace_str='@!d')
    bot.say(msg)


# matching @!f
@sopel.module.rule('\@\!f')
def flip_fat(bot, trigger):
    #flip = "(ノ ゜Д゜)ノ ︵ ┻━┻".decode("utf-8")
    flip = "(ノ ゜Д゜)ノ ︵ ┻━┻"
    msg = _build_msg(trigger, flip)
    bot.say(msg)


# matching @!g
@sopel.module.rule('\@\!g')
def flip_finger(bot, trigger):
    #flip = "╭∩╮◕ل͜◕)╭∩╮  ︵┻┻".decode("utf-8")
    flip = "╭∩╮◕ل͜◕)╭∩╮  ︵┻┻"
    msg = _build_msg(trigger, flip)
    bot.say(msg)


# matching @!h
@sopel.module.rule('\@\!h')
def flip_hercules(bot, trigger):
    #flip = "(/ .□.) ︵╰(゜Д゜)╯︵ /(.□. )".decode("utf-8")
    flip = "(/ .□.) ︵╰(゜Д゜)╯︵ /(.□. )"
    msg = _build_msg(trigger, flip)
    bot.say(msg)


# matching @!j
@sopel.module.rule('\@\!j')
def flip_jedi(bot, trigger):
    #flip = "(._.) ~ ︵ ┻━┻".decode("utf-8")
    flip = "(._.) ~ ︵ ┻━┻"
    msg = _build_msg(trigger, flip)
    bot.say(msg)


# matching @!m
@sopel.module.rule('\@\!m')
def flip_magic(bot, trigger):
    #flip = "༼∩ຈل͜ຈ༽つ━☆ﾟ.*･｡ﾟ ︵ ┻━┻".decode("utf-8")
    flip = "༼∩ຈل͜ຈ༽つ━☆ﾟ.*･｡ﾟ ︵ ┻━┻"
    msg = _build_msg(trigger, flip)
    bot.say(msg)


# matching @!r
@sopel.module.rule('\@\!r')
def flip_rage(bot, trigger):
    #flip = "(ノಠ益ಠ)ノ彡┻━┻".decode("utf-8")
    flip = "(ノಠ益ಠ)ノ彡┻━┻"
    msg = _build_msg(trigger, flip)
    bot.say(msg)


# matching @!t
@sopel.module.rule('\@\!t')
def flip_table(bot, trigger):
    #flip = "(╯°□°)╯︵ ┻━┻ ".decode("utf-8")
    flip = "(╯°□°)╯︵ ┻━┻ "
    msg = _build_msg(trigger, flip)
    bot.say(msg)


# matching @!z
@sopel.module.rule('\@\!z')
def flip_bear(bot, trigger):
    #flip = "ʕノ•ᴥ•ʔノ ︵ ┻━┻".decode("utf-8")
    flip = "ʕノ•ᴥ•ʔノ ︵ ┻━┻"
    msg = _build_msg(trigger, flip)
    bot.say(msg)
