#!/bin/sh

uv run antlr4 -Dlanguage=Python3 -o ../src/canopus_dsl/generated ./CanopusDSL.g4

uv run antlr4 -Dlanguage=JavaScript -o ../js/canopus-dsl/generated ./CanopusDSL.g4
