#!/usr/bin/env python3
"""
the script contains functions for pagination
"""
import csv
from typing import List
from typing import Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def index_range(self, page: int, page_size: int) -> Tuple[int, int]:
        """
        Helper function to generate a range of pages
        :param page: int The page number
        :param page_size: int The size of the page
        :return: tuple of ints The range of pages
        """

        return (page - 1) * page_size, page * page_size

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Paginate a database of popular baby names.
        :param page: The page number
        :param page_size: The number of pages
        :return: list of list the names on the page
        """

        assert isinstance(page, int)
        assert isinstance(page_size, int)
        assert page > 0
        assert page_size > 0

        index_range = self.index_range(page, page_size)

        try:
            dataset = self.dataset()[index_range[0]:index_range[1]]
        except IndexError:
            return []

        return dataset
