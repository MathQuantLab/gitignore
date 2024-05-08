import asyncio
import utils
import sys

from pathlib import Path

FILE_NAME = ".gitignore"

async def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python -m gitignore <language> ...")
        sys.exit(0)
    
    if Path(FILE_NAME).exists():
        print("A .gitignore file already exists in the current directory.")
        sys.exit(0)
    
    args = sys.argv[1:]
    
    
    
if __name__ == "__main__":
    asyncio.run(main())