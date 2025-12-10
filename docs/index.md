# Welcome to clisechubman

A CLI to help manage findings from AWS Security Hub

**Usage**:

```console
$ [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `validate-rules`: Validate the rules defined in the given...

## `validate-rules`

Validate the rules defined in the given YAML file.

Parameters
----------
rules : str, optional
    Path to the rules YAML file, by default &quot;rules.yaml&quot;.

Raises
------
typer.Exit
    Exit with code 1 if validation fails.

**Usage**:

```console
$ validate-rules [OPTIONS] [RULES]
```

**Arguments**:

* `[RULES]`: [default: rules.yaml]

**Options**:

* `--help`: Show this message and exit.
