#!/bin/sh

uv run antlr4 -Dlanguage=Python3 -o ../src/canopus_dsl/generated ./CanopusDSL.g4
