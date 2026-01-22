import argparse
import sys
import markdown
from core_converter import convert_markdown_to_html

def main():
    parser = argparse.ArgumentParser(description="Convert Markdown text or file to HTML")

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-t', '--text', help='Direct Markdown text to convert')
    group.add_argument('-f', '--file', help="Path to a Markdown file to convert")

    parser.add_argument('-o', '--output', help="Optional: Path to save the HTML output file")

    args = parser.parse_args()

    markdown_content = ""
    input_source = ""

    if args.text:
        markdown_content = args.text
        input_source = "direct text"
    elif args.file:
        input_source = args.file
        try:
            with open(args.file, 'r', encoding="utf-8") as f:
                markdown_content = f.read()
        except FileNotFoundError:
            print(f"Error: Input file not found: {args.file}", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file {args.file}: {e}", file = sys.stderr)
            sys.exit(1)
    
    # Convert the markdown
    html_output = convert_markdown_to_html(markdown_content)

    # Output the result
    if args.output:
        try:
            with open(args.output, 'w', encoding="utf-8") as f:
                f.write(html_output)
            print(f"Successfully converted {input_source} to HTML: {args.output}")
        except Exception as e:
            print(f"Error writing to output file {args.output}: {e}", file = sys.stderr)
            sys.exit(1)
    else:
        print(html_output)
if __name__ == "__main__":
    main()