# Warning Label for Humans: One Line, Big Laugh

[![make.fun](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![rank](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/oponopon31/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/rank.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)
[![reward](https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/oponopon31/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/reward.svg)](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85)

Entry for the [make.fun](https://make.fun/bounty/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85) competition "Warning Label for Humans: One Line, Big Laugh".

`main.py` (Python 3, pure standard library, deterministic, no network)
writes one original single-line safety warning label for humans to
`entry.txt` — 115 characters, well inside the 160-character gate. The
label is written in genuine printed-label diction, names an everyday
human behaviour everyone recognises, and lands its turn in the last
few words, in a single read. The reasoning behind the choice,
including the candidates it beat, is in the docstring of `main.py`.

Run it with:

```sh
python3 main.py
```

It honours `$MAKEFUN_OUTPUT_DIR` (falling back to `/output`, then the
current directory), validates the line (exactly one line, 1–160
characters, not only whitespace, no control characters), writes
`entry.txt` with exactly one trailing newline, re-reads the file and
asserts the exact bytes, and prints the line, character count, byte
count, and SHA-256 of the output.
