import os
import argparse

def parse_commandline():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('paths', metavar='PATH', nargs='+', help='Paths to search')
    parser.add_argument('--threshold', type=int, default=260, help='Character threshold')

    return parser.parse_args()

def script_main():

    # parse the command line
    args = parse_commandline()

    too_long = 0

    # loop through and detect the length of paths and print all offending
    for path in args.paths:
        for root, _, files in os.walk(path, topdown=False):
            for filepath in files:
                abs_path = os.path.abspath(os.path.join(root, filepath))
                path_len = len(abs_path)
                if path_len >= args.threshold:
                    print('{} : {}'.format(path_len, abs_path))
                    too_long += 1

    if too_long == 0:
        print('All file paths are fine')
    else:
        print('{} file paths are too long'.format(too_long))


if __name__ == '__main__':
    script_main()
