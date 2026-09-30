"""
script to
generate xcompose sequences for each of the braille pattern characters
in the Braille Patterns block (U+2800..U+28FF).
"""
import unicodedata

def generate_pairings() -> list[tuple[list[str], str]]:
    """
    return a list of all the pairings of
    key sequences to braille patterns
    """

    # according to 
    # https://en.wikipedia.org/wiki/Braille_Patterns
    # the braille dots are numbered 1 through 8,
    # but for convenience of this script, i will number
    # them 1 through 7
    #
    # 0 3
    # 1 4
    # 2 5
    # 6 7 (irregular last row, added later after first three)
    #
    # and the formula to derive their unicode codepoints,
    # given which dots are raised, is just to take each dot
    # as a bit that's on or off, with palce value of the dot
    # index. then we add the whole number to the start of the
    # Braille Patterns block
    # 
    # there are 256 possible combinations

    # these keys correspond to each braille dot in the compose sequences
    #       01234567
    KEYS = "1qa2wszx"

    # i want my xcompose sequences to require me to enter the dots
    # in this order (left to right, top to bottom).
    ENTRY_ORDER = [0, 3, 1, 4, 2, 5, 6, 7]

    # loop through every braille character and generate its sequence
    sequences: list[tuple[list[str], str]] = []
    for offset in range(0x100):
        # get the unicode character itself
        pattern_char = chr(0x2800 + offset)

        seq = []
        for i in ENTRY_ORDER:
            if offset & (1 << i):
                seq += KEYS[i]
        sequences.append((seq, pattern_char))


    return sequences


def generate_xcompose(pairings: list[tuple[list[str], str]]) -> str:
    lines = []
    for pair in pairings:
        seq, char = pair
        seq = ["Multi_key", "B"] + seq + ["space"]
        line = ""
        line += " ".join([f"<{k}>" for k in seq])
        line += f"\t: \"{char}\""

        name = unicodedata.name(char, "")
        if name:
            line += "\t# " + name

        lines.append(line)

    return "\n".join(lines)


if __name__ == "__main__":
    pairings = generate_pairings()
    print(generate_xcompose(pairings))

