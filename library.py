from typing import List  # noqa: F401

import bot
import lib.items.feature
from lib.data import Send
from lib.data.message import Message


def botFeatureList(send: Send) -> bool:
    prepend: str = 'Features: '
    limit: int = bot.config.messageLimit - len(prepend)
    featureAbbrList: List[str] = list(lib.items.feature.features().keys())
    featureAbbrList.sort()
    printList: List[str] = []
    length = 0
    feature: str
    for feature in featureAbbrList:
        if length:
            length += 2
        length += len(feature)
        printList.append(feature)
        if length >= limit:
            send(prepend + ', '.join(printList[:-1]))
            del printList[:-1]
            length = len(feature)
    if printList:
        send(prepend + ', '.join(printList))
    return True


def botFeatureDescription(message: Message, send: Send) -> bool:
    if len(message) < 2:
        return False

    features: lib.items.feature.FeatureDict = lib.items.feature.features()
    if message.lower[1] not in features or features[message.lower[1]] is None:
        send('Unrecognized feature: ' + message.lower[1])
        return True

    send(message.lower[1] + ': ' + features[message.lower[1]])

    return True
