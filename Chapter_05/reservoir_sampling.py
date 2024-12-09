import random


def reservoir_sampling(stream, k):
    reservoir = []
    for i, item in enumerate(stream):
        if i < k:
            reservoir.append(item)
        else:
            j = random.randint(0, i)
            if j < k:
                reservoir[j] = item
    return reservoir


if __name__ == "__main__":
    # Приклад використання
    stream = range(1000000)  # Великий потік даних
    sample = reservoir_sampling(stream, 10)
    print(sample)
