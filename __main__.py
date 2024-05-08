import asyncio
import sys
from pathlib import Path

import utils

FILE_NAME = ".gitignore"


async def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m gitignore <language> ...")
        sys.exit(0)

    if Path(FILE_NAME).exists():
        if "-f" in sys.argv:
            Path(FILE_NAME).unlink()
        else:
            print("A .gitignore file already exists in the current directory.")
            sys.exit(0)

    args = sys.argv[1:]

    with open(FILE_NAME, "w") as file:
        print(f"Fetching .gitignore files for {', '.join(args)}...")
        try:
            for result in asyncio.as_completed(
                [
                    utils.fetch(language)
                    for language in args
                    if not language.startswith("-")
                ]
            ):
                file.write(await result)
                file.write("\n")
        except RuntimeError as error:
            print(error)
            sys.exit(1)
        print(f".gitignore file created successfully.")


if __name__ == "__main__":
    asyncio.run(main())
