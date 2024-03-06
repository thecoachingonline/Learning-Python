from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--output', required=True, help='The Destionation file for the output of this program')

args = parser.parse_args()

print(args.output)