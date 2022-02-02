<div align="center">
  <h1>FluentGenerator</h1>
  <p>
    <img src="https://img.shields.io/pypi/dm/FluentGenerator">
    <img src="https://img.shields.io/pypi/v/FluentGenerator?label=version">
    <img src="https://img.shields.io/pypi/l/FluentGenerator">
    <img src="https://img.shields.io/github/repo-size/ulbwazhine/FluentGenerator">
  </p>
  <p>Create a random fluent image based on multiple colors.</p>
</div>

## Navigation
* [Example](https://github.com/ulbwazhine/FluentGenerator#example)
* [Install](https://github.com/ulbwazhine/FluentGenerator#install)
  * [Update](https://github.com/ulbwazhine/FluentGenerator#update)
* [Usage](https://github.com/ulbwazhine/FluentGenerator#usage)
  * [In Python console](https://github.com/ulbwazhine/FluentGenerator#in-python-console)
  * [FluentGenerator](https://github.com/ulbwazhine/FluentGenerator#FluentGenerator-parameters)
  * [FluentGenerator.generate parameters](https://github.com/ulbwazhine/FluentGenerator#fluentgeneratorgenerate-parameters)
* [Links](https://github.com/ulbwazhine/FluentGenerator#links)

## Example

<div align="center">
  <img width="375px" src="https://raw.githubusercontent.com/ulbwazhine/FluentGenerator/main/FluentGenerator/example.png" alt="FluentGenerator Example">
  <p>FluentGenerator Example</p>
</div>

## Install
```console
$ python3 -m pip install FluentGenerator
```

### Update
```console
$ python3 -m pip install FluentGenerator --upgrade
```

## Usage

#### In Python console:

```python
from FluentGenerator import FluentImage

fluent = FluentImage(background="#white",
                     colors=10,
                     width=1000,
                     height=1000)

fluent.generate()
```

```console
>>> /path/to/fluent/image
```

#### `FluentImage` parameters:
   * `background`: *str* — Background color.
   * `colors`: *int* — Number of random colors.
   * `width`: *int* — Image width.
   * `height`: *int* — Height width.
   
#### `FluentImage.generate` parameters:
   * `external_storage`: *Optional[bool]* — Optional parameter, true if you need to upload image on [TemporaryStorage](https://github.com/ulbwazhine/TemporaryStorage) (0x0.st etc)

## Links
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/author.svg" height="30"/>](https://ulbwa.github.io)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/github.svg" height="30"/>](https://github.com/ulbwazhine/FluentGenerator)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/pypi.svg" height="30"/>](https://pypi.org/project/FluentGenerator)
[<img src="https://raw.githubusercontent.com/ulbwa/ulbwa/main/static/badges/donate.svg" height="30"/>](https://ulbwa.github.io/go?to=donate)