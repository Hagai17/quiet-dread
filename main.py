"""Write one code review comment to /output/entry.txt.

The comment is a single line of at most 140 characters that approves a pull
request while carrying quiet existential dread.
"""

import os

LINE = (
    "Approved. I checked the edge cases. The biggest one is that we are all "
    "temporary, and it is handled. Merge."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
