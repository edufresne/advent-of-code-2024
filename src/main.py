from argparse import ArgumentParser
import importlib

arg_parser = ArgumentParser()
arg_parser.add_argument("--day", "-d", type=int, required=True)
arg_parser.add_argument("--part", "-p", type=int, required=True)

args = arg_parser.parse_args()

importlib.import_module(f"day{args.day}.part{args.part}").run()
