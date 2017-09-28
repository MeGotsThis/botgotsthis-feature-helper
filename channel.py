from lib.data import ChatCommandArgs
from lib.helper.chat import permission, send

from . import library


@permission('broadcaster')
async def commandFeatureList(args: ChatCommandArgs) -> bool:
    return library.botFeatureList(send(args.chat))


@permission('broadcaster')
async def commandFeatureDescription(args: ChatCommandArgs) -> bool:
    return library.botFeatureDescription(args.message, send(args.chat))
