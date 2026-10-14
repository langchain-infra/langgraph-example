import time


def retry(fn, attempts=3):
    for attempt in range(attempts):
        try:
            return fn()
        except Exception:
            time.sleep(2 ** attempt)
    return fn()
