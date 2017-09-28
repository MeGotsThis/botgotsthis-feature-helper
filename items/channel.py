from typing import Iterable, Mapping, Optional

from lib.data import ChatCommand

from .. import channel


def filterMessage() -> Iterable[ChatCommand]:
    return []


def commands() -> Mapping[str, Optional[ChatCommand]]:
    if not hasattr(commands, 'commands'):
        setattr(commands, 'commands', {
            '!feature-list': channel.commandFeatureList,
            '!featurelist': channel.commandFeatureList,
            '!feature-desc': channel.commandFeatureDescription,
            '!featuredesc': channel.commandFeatureDescription,
            '!feature-description': channel.commandFeatureDescription,
            '!featuredescription': channel.commandFeatureDescription,
            }
        )
    return getattr(commands, 'commands')


def commandsStartWith() -> Mapping[str, Optional[ChatCommand]]:
    return {}


def processNoCommand() -> Iterable[ChatCommand]:
    return []
