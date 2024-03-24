import sys
import os
import markdown
"""This project converts a markdown file
into an HTML file"""


def markdowntohtml(inputmd, outputfile):
    try:
        # Check if Markdown file exists
        if not os.path.exists(inputmd):
            print(f"Missing {inputmd}", file=sys.stderr)
            sys.exit(1)

        # Read Markdown content
        with open(inputmd, 'r', encoding='utf-8') as f:
            inputcontent = f.read()

        # Convert Markdown to HTML
        htmlcontent = markdown.markdown(inputcontent)

        # Write HTML content to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(htmlcontent)

        sys.exit(0)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(input_file, output_file)