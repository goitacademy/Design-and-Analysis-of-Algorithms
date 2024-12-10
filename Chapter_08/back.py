import asyncio
from asyncio import Queue

async def producer(queue, n):
    for i in range(n):
        await queue.put(i)
        print(f"Produced {i}")
        # Імітація швидкого виробництва даних
        await asyncio.sleep(0.1)
    await queue.put(None)  # Сигнал завершення

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f"Consumed {item}")
        # Імітація повільної обробки даних
        await asyncio.sleep(0.5)
    print("Consumer done")

async def main():
    queue = Queue(maxsize=5)  # Обмеження розміру черги
    await asyncio.gather(
        producer(queue, 20),
        consumer(queue)
    )

asyncio.run(main())
