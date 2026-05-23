import asyncio
from functools import partial


class AsyncFileReader:
    '''Asynchronous file reader for task files'''

    def __init__(self, file_path: str):
        '''Initialize with the path to the file to read'''
        self._file_path = file_path
        self._file = None
        self._loop = None

    def __aiter__(self):
        '''Return the iterator object itself'''
        return self

    async def __aenter__(self):
        '''Open the file for reading'''
        self._loop = asyncio.get_running_loop()
        self._file = await self._loop.run_in_executor(
            None,
            partial(
                open,
                self._file_path,
                'r',
                encoding="utf-8"
            )
        )

        return self

    async def __aexit__(self, exc_type, exc, tb):
        '''Close the file when everything is done'''
        if self._file is not None:
            await self._loop.run_in_executor(
                None,
                self._file.close
            )

    async def __anext__(self) -> str:
        '''Read the next line of the currently opened file'''
        line = await self._loop.run_in_executor(
            None,
            self._file.readline
        )

        if not line:
            raise StopAsyncIteration

        return line
