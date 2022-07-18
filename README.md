# aicsimageio-ometiffreader

[![Build Status](https://github.com/evamaxfield/aicsimageio-ometiffreader/workflows/Build/badge.svg)](https://github.com/evamaxfield/aicsimageio-ometiffreader/actions)
[![Documentation](https://github.com/evamaxfield/aicsimageio-ometiffreader/workflows/Documentation/badge.svg)](https://evamaxfield.github.io/aicsimageio-ometiffreader)

A basic OmeTiffReader plugin for aicsimageio.

---

## Installation

**Stable Release:** `pip install aicsimageio-ometiffreader`<br>
**Development Head:** `pip install git+https://github.com/evamaxfield/aicsimageio-ometiffreader.git`

## Quickstart

```python
from aicsimageio_ometiffreader import example

print(example.str_len("hello"))  # prints 5
```

## Documentation

For full package documentation please visit [evamaxfield.github.io/aicsimageio-ometiffreader](https://evamaxfield.github.io/aicsimageio-ometiffreader).

## Development

See [CONTRIBUTING.md](CONTRIBUTING.md) for information related to developing the code.

For development commands we use [just](https://github.com/casey/just).

```bash
just
```
```
Available recipes:
    build                    # run tox / run tests and lint
    clean                    # clean all build, python, and lint files
    default                  # list all available commands
    generate-docs            # generate Sphinx HTML documentation
    lint                     # lint, format, and check all files
    serve-docs               # generate Sphinx HTML documentation and serve to browser
    update-from-cookiecutter # update this repo using latest cookiecutter-py-package
```

**BSD License**
