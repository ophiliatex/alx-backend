### README.md

# Pagination Project

This project focuses on implementing various pagination techniques in Python, including simple pagination, hypermedia pagination, and deletion-resilient pagination.

## Learning Objectives

By the end of this project, you should be able to:
- Paginate a dataset using simple page and page_size parameters.
- Implement hypermedia pagination with metadata.
- Create a deletion-resilient pagination system.

## Requirements

- All code will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should follow the `pycodestyle` style guide (version 2.5.*).
- All modules should have documentation.
- All functions should have documentation explaining their purpose.
- All functions and coroutines must be type-annotated.

## Setup

The project uses the `Popular_Baby_Names.csv` dataset. Ensure this file is in the same directory as your Python scripts.

## Tasks

### 0. Simple Helper Function

Create a function `index_range` that takes two integer arguments `page` and `page_size`, and returns a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

```python
def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index."""
    start = (page - 1) * page_size
    end = page * page_size
    return start, end
```

### 1. Simple Pagination

Implement the `Server` class with a `get_page` method that paginates a dataset.

```python
class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
```

### 2. Hypermedia Pagination

Extend the `Server` class to include a `get_hyper` method that returns a dictionary with hypermedia pagination details.

```python
class Server:
    # (previous code omitted for brevity)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Union[int, List[List]]]:
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
```

### 3. Deletion-Resilient Hypermedia Pagination

Implement a `get_hyper_index` method in the `Server` class that provides deletion-resilient pagination.

```python
class Server:
    # (previous code omitted for brevity)

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict[str, Union[int, List[List]]]:
        assert isinstance(index, int) and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index
        collected = 0

        while collected < page_size and current_index < len(indexed_data):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                collected += 1
            current_index += 1

        next_index = current_index if current_index < len(indexed_data) else None

        return {
            "index": index,
            "page_size": page_size,
            "data": data,
            "next_index": next_index,
        }
```

## Usage

To test your implementation, use the provided `main.py` files for each task and run them as scripts.

```sh
$ ./0-main.py
$ ./1-main.py
$ ./2-main.py
$ ./3-main.py
```

Ensure that the `Popular_Baby_Names.csv` file is available in the same directory.

## Repository Structure

```sh
.
├── 0-simple_helper_function.py
├── 0-main.py
├── 1-simple_pagination.py
├── 1-main.py
├── 2-hypermedia_pagination.py
├── 2-main.py
├── 3-hypermedia_del_pagination.py
├── 3-main.py
├── Popular_Baby_Names.csv
└── README.md
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

By following this structure and completing the tasks, you will have a fully functional and robust pagination system. Happy coding!
