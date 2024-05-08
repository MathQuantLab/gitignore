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
        print("A .gitignore file already exists in the current directory.")
        sys.exit(0)

    args = sys.argv[1:]

    with open(FILE_NAME, "w") as file:
        try:
            for result in asyncio.as_completed(
                [utils.fetch(language) for language in args]
            ):
                file.write(await result)
        except RuntimeError as error:
            print(error)
            sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())
