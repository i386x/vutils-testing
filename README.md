[![Coverage Status](https://coveralls.io/repos/github/i386x/vutils-testing/badge.svg?branch=main)](https://coveralls.io/github/i386x/vutils-testing?branch=main)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/i386x/vutils-testing.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/i386x/vutils-testing/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/i386x/vutils-testing.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/i386x/vutils-testing/context:python)

# vutils-testing: Auxiliary library for writing tests

This package provides a set of functions and classes shared across various
repositories within test code.

## Installation

To install the package, type
```sh
$ pip install vutils-testing
```

## Usage

Following code snippets demonstrate how to use the package.

The method `TestCase.assert_called_with` asserts that the mock object has been
called once with the specified arguments and then resets it:
```python
import unittest.mock

from vutils.testing import TestCase

class ExampleTestCase(TestCase):
    def test_assert_called_with(self):
        mock = unittest.mock.Mock()

        mock.foo(1, 2, bar=3)
        self.assert_called_with(mock, 1, 2, bar=3)

        mock.foo(4)
        self.assert_called_with(mock, 4)
```
