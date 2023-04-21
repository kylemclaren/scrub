#!/usr/bin/env python3

import sys
import argparse
from scrubadubdub import Scrub
from halo import Halo


def main():
    parser = argparse.ArgumentParser(
        description="Scrub PII from text using scrubadubdub."
    )

    parser.add_argument(
        "-i", "--input", type=str, help="Path to the input file containing text."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        help="Path to the output file where the scrubbed text will be saved.",
    )

    args = parser.parse_args()

    # Read input text from file
    with open(args.input, "r") as input_file:
        input_text = input_file.read()

    # Set up spinner
    spinner = Halo(text="Scrubbing PII", spinner="dots")
    spinner.start()

    # Scrub PII from the input text
    try:
        scrubber = Scrub()
        scrubbed_text = scrubber.scrub(input_text)
    except Exception as e:
        spinner.fail("Scrubbing failed")
        print("Error:", str(e))
        sys.exit(1)
    else:
        spinner.succeed("Scrubbing completed")

    # Save the scrubbed text to output file
    with open(args.output, "w") as output_file:
        output_file.write(scrubbed_text)


if __name__ == "__main__":
    main()
