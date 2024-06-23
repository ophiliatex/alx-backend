#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None,
                        page_size: int = 10) -> Dict[str, Union[int, List]]:
        """
            Deletion-resilient hypermedia pagination
            :param index: index to get hypermedia for
            :param page_size: int page size
            :return: dict hypermedia indexed by page_size
        """

        dataset = self.indexed_dataset()

        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0
        assert index < len(dataset)

        data = []
        current_index = index
        collected = 0

        while collected < page_size and current_index < len(dataset):
            if current_index in dataset:
                data.append(dataset[current_index])
                collected += 1
            current_index += 1

        next_index = current_index if current_index < len(dataset) else None

        hyper_index = {
            "index": index,
            "page_size": page_size,
            "data": data,
            "next_index": next_index,
        }

        return hyper_index
