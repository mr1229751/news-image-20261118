"""Copy the entry image bundled beside this file into the output directory.

The output directory is taken from the MAKEFUN_OUTPUT_DIR environment
variable and defaults to "/output". The destination file is always named
"entry.png".
"""

import os
import shutil


def main() -> None:
    source = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    destination = os.path.join(output_dir, "entry.png")
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()
