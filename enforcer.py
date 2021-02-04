#!/usr/bin/env python3
"""Parses commit messages to ensure the follow the Conventional Commits standard
"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter

if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter,
        
    )

    args, unknown = parser.parse_known_args()

    print(unknown)