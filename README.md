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

## Usage

```bash
$ python main.py <file.canopus>
```

Exit codes:

| Code | Meaning |
|---|---|
| `0` | Clean model (warnings allowed) |
| `1` | Parse errors or error-severity issues |
| `2` | Usage error |

Diagnostics go to stderr: parse errors as `line L:C: <message>`, model issues
as `severity: code: message`. The model goes to stdout. `parse_string` never
raises: invalid input yields a listener with a populated `.errors` list.

## Examples

Examples of the canopus DSL can be found under the [tests/resources](./tests/resources/) directory and package use in the [main.py](./main.py) file.
