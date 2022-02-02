import asyncio
import functools
import os
import random
import shutil
import string

from html2image import Html2Image

shot = Html2Image()


def run_sync(func, *args, **kwargs):
    return asyncio.get_event_loop() \
        .run_in_executor(None,
                         functools.partial(func,
                                           *args,
                                           **kwargs))


def random_string(n: int):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))


def render_html(html: str, width: int, height: int, path: str, name: str) -> str:
    shot.screenshot(
        html_str=html,
        size=(width, height), save_as=name)
    shutil.move(name, os.path.join(path, name))

    return os.path.join(path, name)
