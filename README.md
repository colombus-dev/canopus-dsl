# Canopus DSL - The DSL for ML pipelines pattern matching

## Requirements

* Python 3.10
* uv 0.9.0 (https://docs.astral.sh/uv/)

## Development

### Compile the grammar and generate the corresponding Python parser and lexer

> cd ANTLR
> ./compile.sh

Generated files will be located under the [canopus/generated](./canopus/generated/) directory.

Once generated, update the canopus library accordingly (`ConcreteCanopusDSLListener` for instance).

## Examples

Examples of the canopus DSL can be found under the [ANTLR/resources](./ANTLR/resources/) directory.
