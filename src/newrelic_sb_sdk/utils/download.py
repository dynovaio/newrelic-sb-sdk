__all__ = [
    "logger",
    "DownloadFileArgs",
    "Downloader",
    "download_file",
    "download_files",
]


import logging
import multiprocessing
import urllib
import warnings
from collections import namedtuple
from queue import Queue
from threading import Thread
from typing import List, Union

import requests

logger = logging.getLogger("newrelic_sb_sdk")


DownloadFileArgs = namedtuple(
    "DownloadFileArgs",
    [
        "url",
        "file_name",
    ],
)


class Downloader(Thread):
    job: Union[int, None] = None

    def __init__(self, *, queue: Queue, order: int):
        Thread.__init__(self)
        self.queue = queue
        self.order = order

    def run(self):
        while True:
            job, download_file_args = self.queue.get()

            if job is None:
                break

            self.job = job

            logger.debug(
                "Dowloader %d is downloading with parameters %r",
                self.order,
                download_file_args,
            )

            download_file(**download_file_args._asdict())


def download_file(
    *,
    url: str,
    file_name: str,
) -> None:
    chunk_size = 1024

    response = requests.get(
        url,
        stream=True,
        timeout=60,
    )

    response.raise_for_status()

    file_size = int(response.headers.get("content-length", 0))

    if file_size == 0:
        warnings.warn(
            f"Size of {file_name} file is 0B.",
            UserWarning,
            stacklevel=2,
        )

    if not file_name:
        file_name = urllib.parse.urlparse(url).path.split("/")[-1]

    with open(file_name, "wb") as file:
        for chunk in response.iter_content(chunk_size):
            file.write(chunk)


def download_files(
    *,
    urls: List[str],
    base_file_name: str,
    file_extension: str,
) -> None:
    queue: Queue = Queue()

    empy_job = (
        None,
        DownloadFileArgs(None, None),
    )

    workers = []
    workers_count = multiprocessing.cpu_count()
    zero_padding = max(len(str(len(urls))), 1)

    jobs = [
        (
            order,
            DownloadFileArgs(
                url,
                f"{base_file_name}_{order:0>{zero_padding}d}.{file_extension}",
            ),
        )
        for order, url in enumerate(urls)
    ]

    for job in jobs:
        queue.put(job)

    for _ in range(workers_count):
        queue.put(empy_job)

    for order in range(workers_count):
        worker = Downloader(
            queue=queue,
            order=order,
        )
        worker.start()
        workers.append(worker)

    for worker in workers:
        worker.join()
