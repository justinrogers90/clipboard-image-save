"""Clipboard Image Save — Save a bitmap from the Windows clipboard to PNG in a folder you choose."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='clipboard_image_save',
        description='Save a bitmap from the Windows clipboard to PNG in a folder you choose.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Clipboard Image Save')
    print('Print Screen, then a file, no Paint in the middle.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
