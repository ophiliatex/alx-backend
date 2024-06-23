#!/usr/bin/env python3
"""
A helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Helper function to generate a range of pages
    :param page: int The page number
    :param page_size: int The size of the page
    :return: tuple of ints The range of pages
    """

    return (page - 1) * page_size, page * page_size
