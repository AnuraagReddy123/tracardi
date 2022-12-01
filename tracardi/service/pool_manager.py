import asyncio


class PoolManager:

    def __init__(self, max_pool, on_pool_purge=None, on_append=None, replace_item_on_append=False):
        self.replace_item_on_append = replace_item_on_append
        self.on_append = on_append
        self.max_pool = max_pool
        self.on_pool_purge = on_pool_purge
        self.items: list = []
        self.counter = 0
        self.ttl = 0
        self.loop = None
        self.last_task = None

    def set_ttl(self, loop, ttl):
        self.ttl = ttl
        self.loop = loop

    async def _invoke(self):
        if self.on_pool_purge:
            result = self.on_pool_purge(self.items)
            if asyncio.iscoroutinefunction(self.on_pool_purge):
                await result

        self.items = []
        self.counter = 0

    async def _append(self, item):
        if self.on_append:
            result = self.on_append(item)
            if asyncio.iscoroutinefunction(self.on_append):
                result = await result
            return result

    def __await__(self):
        async def closure():
            return self

        return closure().__await__()

    async def __aenter__(self):
        return self

    def purge_task(self):
        asyncio.create_task(self.purge())

    async def purge(self):
        if self.last_task:
            self.last_task.cancel()
        if self.items:
            await self._invoke()

    async def __aexit__(self, exc_type, exc_value, exc_traceback):
        await self.purge()

    async def append(self, item):
        if self.on_append:
            result = await self._append(item)
            if self.replace_item_on_append:
                item = result
        self.items.append(item)
        self.counter += 1
        if self.counter == self.max_pool:
            await self.purge()
        elif self.ttl > 0 and self.loop:
            if self.last_task:
                self.last_task.cancel()
            self.last_task = self.loop.call_later(self.ttl, self.purge_task)