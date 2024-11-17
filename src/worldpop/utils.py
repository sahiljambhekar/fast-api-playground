from time import perf_counter


def measure_time(func):
    async def wrapper(*args, **kwargs):
        start = perf_counter()
        result = await func(*args, **kwargs)
        time_taken = (perf_counter() - start) * 1000
        if isinstance(result, dict):
            result["time_taken"] = f"{time_taken:.2f}ms"
        return result

    return wrapper
