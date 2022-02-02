import os
import random
from typing import Optional

from TemporaryStorage import TemporaryStorageInstance
from jinja2 import Template

from FluentGenerator.utils import render_html, random_string

storage = TemporaryStorageInstance()
generated_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'generated')
if not os.path.exists(generated_path):
    os.makedirs(generated_path)


class FluentImage:
    def __init__(self, background: str, colors: int, width: int, height: int):
        if colors < 1:
            colors = 1

        self.width = width
        self.height = height

        self.background = background

        self.gradients = [dict(x=random.randint(0, 100),
                               y=random.randint(0, 100),
                               hue=random.randint(0, 360),
                               saturation=random.randint(20, 80),
                               lightness=random.randint(20, 80),
                               transparent=random.randint(40, 80)) for _ in range(colors)]

    def __gen_html__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'template.html'), 'r') as f:
            return Template(f.read()).render(background=self.background, gradients=self.gradients)

    def generate(self, external_storage: Optional[bool] = False):
        path = render_html(html=self.__gen_html__(),
                           width=self.width, height=self.height,
                           path=generated_path, name='{}.png'.format(random_string(16)))

        if not external_storage:
            return path
        else:
            uploaded = storage.upload(path)

            if uploaded and uploaded.url:
                os.remove(path)
                return uploaded.url
            else:
                return path
