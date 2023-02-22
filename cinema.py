from datetime import datetime
from enum import Enum


class CustomerEnum(str, Enum):
    STUDENT = "STUDENT"
    FAMILY = "FAMILY"
    RETIREE = "RETIREE"


def get_prices_for_customer_type(*args):
    return []


def get_baseline_prices(*args):
    return []


def merge_prices_with_priority(*args):
    return []


def get_prices_for_customer(
    customer_type: CustomerEnum,
    day: datetime,
) -> list[list[str]]:
    specific_prices = get_prices_for_customer_type(
        customer_type,
        day.date(),
    )
    default_prices = get_baseline_prices(day.date())
    merged_prices = merge_prices_with_priority(
        specific_prices,
        default_prices,
    )
    return merged_prices
