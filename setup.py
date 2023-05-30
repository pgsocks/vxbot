from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup (
    name = "vxTwitterDiscordBot",
    version = "1.0.0",
    author = "pgsocks",
    author_email = "pgsocks@pm.me",
    long_description = long_description,
    long_description_type = "text/markdown",
    packages = ["vxbot"],
    description = "Run a Discord bot that reminds you to use vxtiwtter.",
    install_requires = requirements,
    entry_points = {
        "console_scripts": [
            "vxbot=vxbot.__main__:main"
        ]
    }
)
