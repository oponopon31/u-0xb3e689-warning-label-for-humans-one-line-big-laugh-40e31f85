#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes ONE original warning-label line (plus exactly one trailing
newline) to entry.txt in $MAKEFUN_OUTPUT_DIR, else /output, else the
current directory. Pure standard library, deterministic, no network.

Candidates (all warning-label format, everyday human behaviour, turn
in the last few words) and pairwise reasoning against the judge's
criteria -- (1) IS a single-line safety warning label for every human
and is funny, (2) laugh lands in one read, turn in the LAST FEW WORDS,
(3) feels true about people in general, (4) sounds like a real printed
label, (5) inside 160 chars, uses the whole line, no filler, no second
idea, no repeated joke:

A. "WARNING: Human contains no user manual, no off switch, and will
   absolutely touch the thing you just told them not to touch."
   Universal behaviour, but the turn is smeared: "will absolutely
   touch" arrives mid-line and the ending ("not to touch") just
   repeats it. Wordy for one idea.

B. "CAUTION: Human may ignore all instructions, warnings, and common
   sense, then act surprised when the predictable thing happens."
   True, but the ending is abstract -- "the predictable thing
   happens" is not a concrete image, so the laugh fizzles instead of
   landing. The turn ("act surprised") sits in the middle.

C. "WARNING: Do not operate human while tired, hungry, or confident;
   side effects include arguing with strangers about things they
   have not read."
   Funny and true, but TWO ideas (operating conditions + arguing
   about unread things) and the list up front eats the line. Fails
   criterion (5): one idea only.

D. "WARNING: Human will read this label, nod wisely, and then do
   exactly the thing it warns against."
   Turn lands at the end and it is true, but the joke is about the
   label itself rather than about humans in general -- meta cleverness
   instead of recognition. Also the shortest line; it leaves the
   160-char line under-used.

E. "CAUTION: Human comes with no warranty, no refunds, and a lifelong
   tendency to press the button marked DO NOT PRESS."
   CHOSEN. Pairwise: E beats A -- same forbidden-touch behaviour but
   tighter, and the turn ("DO NOT PRESS") is the last three words,
   a concrete printed-label image instead of a paraphrase. E beats B
   -- concrete visual ending vs abstract ending. E beats C -- one
   idea, one turn, no list. E beats D -- the behaviour (pressing the
   forbidden button) is a universal human act, not a joke about the
   label; and "no warranty, no refunds" is genuine printed-label
   diction, so it sounds like a real label (criterion 4) while D
   sounds like a joke wearing a label's clothes.

The chosen line is 115 characters: label format, one behaviour
everyone recognises, turn in the last three words, no filler.
"""

import hashlib
import os
import sys

LINE = (
    "CAUTION: Human comes with no warranty, no refunds, and a "
    "lifelong tendency to press the button marked DO NOT PRESS."
)

MAX_CHARS = 160


def output_dir() -> str:
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env:
        return env
    if os.path.isdir("/output"):
        return "/output"
    return os.getcwd()


def validate(line: str) -> None:
    if not line:
        raise ValueError("line is empty")
    if line.strip() == "":
        raise ValueError("line is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be exactly one line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} chars, over the {MAX_CHARS} limit"
        )
    for ch in line:
        if ord(ch) < 0x20 or ord(ch) == 0x7F:
            raise ValueError(f"control character U+{ord(ch):04X} in line")


def main() -> int:
    validate(LINE)
    data = (LINE + "\n").encode("utf-8")
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)

    # Re-read and assert the exact bytes: the line plus one newline.
    with open(path, "rb") as f:
        actual = f.read()
    assert actual == data, (
        f"entry.txt mismatch: wrote {data!r}, read back {actual!r}"
    )
    assert actual.count(b"\n") == 1 and actual.endswith(b"\n"), (
        "entry.txt must contain exactly one line plus one trailing newline"
    )
    decoded = actual.decode("utf-8")
    assert decoded == LINE + "\n", "decoded entry.txt differs from LINE"
    assert decoded.rstrip("\n") == decoded.rstrip(), (
        "entry.txt has trailing whitespace before the newline"
    )
    validate(decoded.rstrip("\n"))

    print(LINE)
    print(f"chars: {len(LINE)}")
    print(f"bytes: {len(data)}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    print(f"path: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
