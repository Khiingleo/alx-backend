#!/usr/bin/env python3
"""defines a function index_range """


def index_range(page: int, page_size: int) -> tuple:
    """
    given a page number and page size, calculate the start and end
    indeces for pagination
    """
    start = (page - 1) * page_size
    end = start + page_size

    return (start, end)
