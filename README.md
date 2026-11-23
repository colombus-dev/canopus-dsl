# Canopus DSL - The DSL for ML pipelines pattern matching

## Requirements

* Python 3.10
* uv 0.9.0 (https://docs.astral.sh/uv/)

## Development

### Compile the grammar and generate the corresponding Python parser and lexer

```bash
$ uv run bash scripts/compile.sh
```

Generated files will be located under the [canopus/generated](./canopus/generated/) directory.

Once generated, update the canopus library accordingly (`ConcreteCanopusDSLListener` for instance).

### Run quality gate

Install the pre-commit as follows:

```bash
$ uv run prek install
```

Manually run code-related quality gate:

```bash
$ uv run prek run               # To run pre-commit on staged files
$ uv run bash scripts/check.sh  # or manually check script on all files
```

## Package distribution

To build the `canopus_dsl` package, run the following command:

```bash
$ uv build
```

The build package will be located under the *dist/* directory.

## Examples

Examples of the canopus DSL can be found under the [ANTLR/resources](./ANTLR/resources/) directory and package use in the [main.py](./main.py) file.
