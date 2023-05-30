import argparse
from .bot import client

def main():

    parser = argparse.ArgumentParser()
    parser.description = "Run a Discord bot that reminds you to use vxtiwtter."
    parser.epilog = "Create a bot token here: https://discord.com/developers"
    parser.add_argument("--token", required = True, help = "Discord bot token")

    client.run(parser.parse_args().token)

if __name__ == "__main__":
    main()
