#!/usr/bin/env python3
"""
2. Hypermedia pagination
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple for start index and an end index for pagination
    """
    start = (page - 1) * page_size
    end = page * page_size

    return (start, end)


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

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        A method named get_page that takes two integer
        arguments page with default value 1 and
        page_size with default value 10.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0
        dataset = self.dataset()
        try:
            start, end = index_range(page, page_size)
            return dataset[start:end]
        except IndexError:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary with pagination information and data.
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.get_page(page, page_size)
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page > 1 else None,

        dict = {'page_size': len(data),
                'page': page,
                'data': data,
                'next_page': next_page,
                'prev_page': prev_page,
                'total_pages': total_pages
                }
        return dict
