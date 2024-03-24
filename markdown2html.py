import sys
import os
import markdown
"""This project converts a markdown file
into an HTML file"""


if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    inputmd = sys.argv[1]
    outputfile = sys.argv[2]


def markdowntohtml(inputmd, outputfile):
    try:
        # Check if Markdown file exists
        if not os.path.exists(inputmd):
            print(f"Missing {inputmd}", file=sys.stderr)
            sys.exit(1)

        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

