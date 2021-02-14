"""Utilities."""


def get_interval_unit(interval: int) -> str:
    return "seconds" if interval > 1 else "seconds"
