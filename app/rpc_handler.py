from aiohttp.web import Request


async def handle_rpc(request: Request):
    print('aa')
    return {'a': 'b'}
