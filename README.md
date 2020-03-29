# shorten_url
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

Python Library to help you short and expand urls using https://rel.ink/

## Installation

In order install this package, simply run:

```bash
pip install shorten_url
```

## Usage

To use shorten_url, you first need to import the package:

```python
import shorten_url
```

### Shorten the URL:

```python
shorten_url.short("https://www.linkedin.com/in/salil-gautam/")    # Returns the shortened URL.
```

### Expand the URL:

```python
shorten_url.expand("https://rel.ink/goqDVn")    # Returns the expanded URL.
```



