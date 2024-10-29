import time


def get_mean(x):
    mean = 0
    for i in x:
        mean += i
    mean = mean / len(x)
    return mean


x = [i for i in range(1, 1_000_000)]

start = time.time()
get_mean(x)
end = time.time()
print(f"Time taken for mean calculation: {10**6*(end - start)} microseconds")
