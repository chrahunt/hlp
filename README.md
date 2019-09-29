# hlp

Get Python help from the command-line.

![terminalcast](https://user-images.githubusercontent.com/2312275/65839287-762dbb80-e2d9-11e9-9d37-fe93d33fba3d.gif)

# Setup

```
pip install hlp
```

To enable autocompletion, put the following in your shell's init script:

```
eval "$(hlp --autocomplete-init=bash)"
```

# Usage

```
hlp part [parts ...]
```

Where `part` and `parts` combined form a Python package, module, or class
name. When executed, `hlp` runs the
[`help()`](https://docs.python.org/library/functions.html#help) built-in
function on the combined parts.

For example:

```
hlp http
hlp http.server
hlp http server
hlp http server SimpleHTTPRequestHandler
```

`hlp` autocompletes package, module, and class names.

`hlp` provides help for the Python environment it is executed under. To get
help for a different environment, install help into it. Only one user-level
install is supported. If more are required, it may be better to just use
`path/to/python -m pydoc`.

# Features

* Module and class name autocompletion (in bash)
* A few less characters than `python -m pydoc`

# Development

## Tests/Linters

Install [nox](https://nox.thea.codes/en/stable/) and run it in the root of the
repository.

## Release

1. Identify commit to promote artifacts for, it must have a successful build
   with artifacts pushed to S3.
2. Locally tag commit with annotated tag.
3. Push tag to repo.
4. Create PR to bump version.
