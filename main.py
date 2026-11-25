"""Famous Last Words: The Funniest Epitaph — make.fun bounty
u-riidzhsn-famous-last-words-the-funniest-epitaph-ff177406 ($2).

Writes one original funny one-line epitaph to /output/entry.txt
(falling back to output/entry.txt when /output is not writable)
and prints it with end="" so stdout is byte-identical to the file.

Pure Python 3.13 standard library, deterministic, no network.
"""

import os

# Revised: tightened "spent my whole life clicking" to "spent my life
# hitting" — shorter, punchier verb, better carved-in-stone rhythm.
# The twist stays: every reminder snoozed except the last one.
ENTRY = "I spent my life hitting 'remind me later.' Death was the one update that couldn't be postponed."


def main() -> None:
    for directory in ("/output", "output"):
        try:
            os.makedirs(directory, exist_ok=True)
            path = os.path.join(directory, "entry.txt")
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(ENTRY)
            break
        except OSError:
            continue
    print(ENTRY, end="")


if __name__ == "__main__":
    main()
