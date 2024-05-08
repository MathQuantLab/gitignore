import setuptools

LONG_DESCRIPTION = open("README.md").read()
REQUIRED_PACKAGES = open("requirements.txt").read().splitlines()

setuptools.setup(
    name="dotgitignore",
    version="1.0",
    author="Aiglon Doré & Rainbow",
    author_email="contact@mathquantlab.com",
    packages=setuptools.find_packages(),
    description="A command-line utility to fetch .gitignore files for multiple languages.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="gitignore git ignore",
    install_requires=REQUIRED_PACKAGES,
)
