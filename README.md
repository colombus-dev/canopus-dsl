# Canopus DSL - The DSL for ML pipelines pattern matching

## Requirements

* Python 3.10
* uv 0.9.0 (https://docs.astral.sh/uv/)

## Development

### Compile the grammar and generate the corresponding Python parser and lexer

```bash
$ uv run bash scripts/compile.sh
```

Generated files will be located under [src/canopus_dsl/generated](./src/canopus_dsl/generated/)
(Python) and [js/canopus-dsl/generated](./js/canopus-dsl/generated/) (JavaScript).

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
raises: invalid input yields a listener with a populated `.errors` list and no
program (`program is None`) — only a clean parse exposes a model.

## DSL syntax

A program lists its imports first, then its pattern definitions:

```canopus
import Q3, Q4

pattern Q1 = [step="Visualization"]+
pattern Q2 = start -> Q1 -> * -> Q3 -> end
```

Rules:

- **Patterns** — `pattern <Name> = <expr>`. Names start with an uppercase
  letter (`Q1`, `Q8_R`).
- **Imports** — `import <Name> (, <Name>)*`. Imports must precede all pattern
  definitions; an import after a pattern is a parse error.
- **References** — a pattern body may only name a pattern defined earlier in
  the file or an import; forward and self references are errors. Reference
  cycles are therefore impossible.
- **Sequence** — steps chained with `->`, optionally anchored by `start` and
  `end`. An anchored pipeline needs at least one step between `start` and
  `end`: `start -> end` is a parse error.
- **Wildcard** — `*` matches any single step. It never takes a multiplicity:
  `*+` and `**` are parse errors.
- **Element** — `[<label> <op> <value>]` with `=` or `!=`; conditions are
  comma-separated, e.g. `[algoName != "read_csv", step="Data Loading"]`.
- **Multiplicity** — `*` (zero or more) or `+` (one or more) after a primary,
  e.g. `[step="X"]+` or `Q5*`.
- **Group** — `( <expr> (| <expr>)* )`: alternatives, each a full sequence.
  Single-element groups are legal (`(Q1)`); empty groups are not (`()` is a
  parse error); quantified primaries work inside groups, e.g. `(Q1* | [step="X"]+)`.
- **Comments** — `#` starts a comment running to the end of the line.

## Examples

Examples of the canopus DSL can be found under the [tests/resources](./tests/resources/) directory and package use in the [main.py](./main.py) file.
