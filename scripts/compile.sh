#!/bin/sh

cd ANTLR/

antlr4 -Dlanguage=Python3 -o ../src/canopus_dsl/generated ./CanopusDSL.g4
antlr4 -Dlanguage=JavaScript -o ../js/canopus-dsl/generated ./CanopusDSL.g4
