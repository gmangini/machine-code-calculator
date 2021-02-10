#!/bin/bash
set -e
set -x

pylint -E src/
mypy --pretty --disallow-untyped-defs src/
yapf --recursive --parallel --in-place src/
