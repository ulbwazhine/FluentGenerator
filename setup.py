from setuptools import setup, find_packages


setup(
    name='FluentGenerator',
    version='2022.02.02.1',
    packages=find_packages(),
    url='https://github.com/ulbwazhine/FluentGenerator',
    license='MIT',
    author='Ulbwazhine',
    author_email='ulbwa@icloud.com',
    description='Create a random fluent image based on multiple colors.',
    install_requires=[line.strip() for line in open("requirements.txt").readlines()],
    long_description=open('readme.md', 'r').read(),
    long_description_content_type='text/markdown',
    include_package_data=True
)
