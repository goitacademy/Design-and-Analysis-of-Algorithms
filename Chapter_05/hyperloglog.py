import random
import mmh3
import math


class HyperLogLog:
    def __init__(self, p=5):
        self.p = p
        self.m = 1 << p
        self.registers = [0] * self.m
        self.alpha = self._get_alpha()
        self.small_range_correction = 5 * self.m / 2  # Поріг для малих значень

    def _get_alpha(self):
        if self.p <= 16:
            return 0.673
        elif self.p == 32:
            return 0.697
        else:
            return 0.7213 / (1 + 1.079 / self.m)

    def add(self, item):
        x = mmh3.hash(str(item), signed=False)
        j = x & (self.m - 1)
        w = x >> self.p
        self.registers[j] = max(self.registers[j], self._rho(w))

    def _rho(self, w):
        return len(bin(w)) - 2 if w > 0 else 32

    def count(self):
        Z = sum(2.0**-r for r in self.registers)
        E = self.alpha * self.m * self.m / Z

        if E <= self.small_range_correction:
            V = self.registers.count(0)
            if V > 0:
                return self.m * math.log(self.m / V)

        return E


if __name__ == "__main__":
    # Приклад використання
    hll = HyperLogLog(p=14)
    all_tags = [
        "python",
        "fastapi",
        "web",
        "api",
        "database",
        "sql",
        "orm",
        "async",
        "programming",
        "coding",
        "development",
        "software",
        "tech",
        "data",
        "backend",
        "frontend",
        "fullstack",
        "learning",
        "tutorial",
        "blog",
    ]
    # Додаємо елементи
    for i in range(100000):
        hll.add(random.choice(all_tags))

    # Оцінюємо кардинальність
    estimated_cardinality = hll.count()
    print(f"Оцінена кардинальність: {estimated_cardinality}")
