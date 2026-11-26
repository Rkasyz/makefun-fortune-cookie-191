"""Fortune Cookie Funnies for Engineers — make.fun entry.

Writes one fortune cookie message for a software engineer to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

The entry is a single line of 116 characters, inside the competition's
gate of 1 to 120 characters of UTF-8 text. It reads like a real fortune
(short, declarative, future-tense) and its twist comes from the
engineer's world — a Friday deploy, broken production, an unintelligible
commit — with the funniest word, the error code 404, sitting at the end.
"""

import os

ENTRY = (
    "You will ship on Friday, break production by lunch, and fix it "
    "with a commit no one understands. Lucky numbers: 404."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry outside the 1-120 character gate"
    assert ENTRY.strip() == ENTRY, "entry must not have leading/trailing whitespace"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
