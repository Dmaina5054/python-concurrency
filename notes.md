Coroutines Notes

Declared with the async/await syntax

To run the coroutine, asyncio provides three mechanisms

    1. asyncio.run() -> runs the top-level entry point(main)
    2. Awaiting on a coroutine.
    3. using the asyncio.create_task() which runs coroutines as tasks