[![PyPI version](https://badge.fury.io/py/sopel-modules.tableflip.svg)](https://badge.fury.io/py/sopel-modules.tableflip)
[![Build Status](https://travis-ci.org/hemna/sopel-tableflip.svg?branch=master)](https://travis-ci.org/hemna/sopel-tableflip)
[![Coverage Status](https://coveralls.io/repos/github/hemna/sopel-tableflip/badge.svg?branch=master)](https://coveralls.io/github/hemna/sopel-tableflip?branch=master)

# sopel-tableflip
sopel-tableflip is a simple tableflip bot for Sopel.

This bot will flip a table when requested.
(╯°□°)╯︵ ┻━┻ ︵ ╯(°□° ╯)

## Usage
```
# Get all the tableflip commands
│11:35:29 hemna_ | @?                                                                                                               │
│11:35:30 _pewp_ | Welcome to Table flipping bot.                                                                                   │
│11:35:31 _pewp_ | (╯°□°)╯︵ ┻━┻                                                                                                    │
│11:35:31 _pewp_ | @!           - Hello.                                                                                            │
│11:35:32 _pewp_ | @!b <nick>   - Battle another nick table flip.                                                                   │
│11:35:33 _pewp_ | @!c          - Covfefe table flip.                                                                               │
│11:35:34 _pewp_ | @!d <nick>   - Battle win another nick table flip.                                                               │
│11:35:35 _pewp_ | @!f          - Fat table flip.                                                                                   │
│11:35:36 _pewp_ | @!g          - The Finger table flip.                                                                            │
│11:35:36 _pewp_ | @!h          - Hercules table flip.                                                                              │
│11:35:37 _pewp_ | @!j          - Jedi table flip.                                                                                  │
│11:35:38 _pewp_ | @!m          - Magic table flip.                                                                                 │
│11:35:39 _pewp_ | @!r          - Rage table flip.                                                                                  │
│11:35:40 _pewp_ | @!t          - Standard table flip.                                                                              │
│11:35:40 _pewp_ | @!z          - Bear table flip.

# Send a tableflip to a channel
/m <botname> .tf h <channel>
/m _pewp_ .tf h #pewp
│11:47:58 _pewp_ | hemna_ ヘ(°￢°)ノ
/m _pewp_ .tf c #pewp
│11:48:15 _pewp_ | hemna_ ༼ノಠل͟ಠ༽ノ ︵ ┻━┻

``

## Requirements
```
requests
sopel
```
