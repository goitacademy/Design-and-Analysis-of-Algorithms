import time


class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.refill_rate = refill_rate
        self.tokens = capacity  # Початково відро повністю заповнене
        self.last_refill_time = time.monotonic()  # Час останнього оновлення

    def refill(self):
        now = time.monotonic()  # Поточний час
        elapsed = now - self.last_refill_time  # Скільки часу минуло з останнього поповнення
        new_tokens = elapsed * self.refill_rate  # Кількість нових токенів
        # Оновлюємо кількість токенів, не перевищуючи місткість
        self.tokens = min(self.capacity, self.tokens + new_tokens)
        self.last_refill_time = now  # Оновлення часу поповнення

    def consume(self, num_tokens):
        self.refill()  # Оновлення токенів перед спробою спожити
        if self.tokens >= num_tokens:
            self.tokens -= num_tokens  # Зменшення кількості токенів
            return True
        return False  # Недостатньо токенів для виконання операції


if __name__ == "__main__":
    bucket = TokenBucket(capacity=10, refill_rate=2)  # 10 токенів, 2 токени/с

    for i in range(20):
        if bucket.consume(3):  # Спроба спожити 3 токени
            print(f"Запит {i + 1}: дозволено")
        else:
            print(f"Запит {i + 1}: відхилено")
        time.sleep(0.5)  # Затримка між запитами
