import datetime
import os
import argparse
import src.discover as discover

parser = argparse.ArgumentParser(description='Search for files')
parser.add_argument('--key', type=str, help='Search term')
parser.add_argument('--path', type=str, help='Path to search', default=os.path.expanduser('~'))
parser.add_argument('--dev', action='store_true', help='Search recursively')
parser.add_argument('--search', action='store_true', help='Search recursively')

args = parser.parse_args()

run_start = datetime.datetime.now()

if args.search:

    out = discover.hue(args.key, args.path)

    i = 1
    for f in out:
        print(f'{i}:',f,out[f])
        i += 1
    print("Time taken:",datetime.datetime.now()-run_start)

if args.dev:
    listed = discover.threads(key=args.key, search_path=args.path)
    for k,v in listed.items():
        print(f"{k}: {v}")
    print("Time taken:",datetime.datetime.now()-run_start)


