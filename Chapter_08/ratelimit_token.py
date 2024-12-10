import time


class RateLimiter:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity
        self.tokens = capacity
        self.refill_rate = refill_rate
        self.last_refill_time = time.time()

    def is_allowed(self):
        current_time = time.time()
        elapsed = current_time - self.last_refill_time

        # Поповнюємо токени
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill_time = current_time

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False


if __name__ == "__main__":
    # Використання
    limiter = RateLimiter(capacity=10, refill_rate=2)  # 10 токенів, 2 токени за секунду

    for _ in range(15):
        if limiter.is_allowed():
            print("Request allowed")
        else:
            print("Request denied")
