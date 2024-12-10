import time


class LeakyBucket:
    def __init__(self, capacity, leak_rate):
        self.capacity = capacity
        self.leak_rate = leak_rate
        self.current_level = 0
        self.last_check_time = time.monotonic()

    def leak(self):
        now = time.monotonic()
        elapsed = now - self.last_check_time
        leaked_amount = elapsed * self.leak_rate
        self.current_level = max(0, self.current_level - leaked_amount)
        self.last_check_time = now

    def add(self, amount):
        self.leak()
        if self.current_level + amount <= self.capacity:
            self.current_level += amount
            return True
        return False


if __name__ == "__main__":
    leaky_bucket = LeakyBucket(capacity=10, leak_rate=2)

    for i in range(15):
        if leaky_bucket.add(3):
            print(f"Запит {i + 1}: дозволено")
        else:
            print(f"Запит {i + 1}: відхилено через переповнення")
        time.sleep(0.5)
