import aiohttp

BASE_URL = "https://www.toptal.com/developers/gitignore/api/"


async def fetch(language: str) -> str:
    """Fetch the .gitignore file for the given language.

    Args:
        language (str): The language for which to fetch the .gitignore file.

    Raises:
        RuntimeError: If the request to fetch the .gitignore file fails.

    Returns:
        str: The contents of the .gitignore file.
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE_URL + language) as response:
            if response.status != 200:
                raise RuntimeError(
                    f"Failed to fetch .gitignore file for {language} with status {response.status}",
                    await response.text(),
                )
            return await response.text()
