#!/bin/sh

uv run antlr4 -Dlanguage=Python3 -o ../canopus/generated ./CanopusDSL.g4
