import os
import argparse

parser = argparse.ArgumentParser(
    description="""Search files for a specified string. Default is to search all 
    files in the current working directory."""
)
parser.add_argument('string', metavar="s", type=str,
                    help='a string to search for')
parser.add_argument('-ext', '--extensions', metavar="", default='', nargs="*",
                    help='filter files for extensions')
parser.add_argument('-root', '--directory', metavar="", default=os.getcwd(),
                    help='specify the root directory to search')
args = parser.parse_args()


def search(search_for, file_ext, path):
    ext = tuple(file_ext) if file_ext else file_ext

    files_with_search_term = []
    for (root, dirs, files) in os.walk(path, topdown=True):
        for filename in files:
            if filename.endswith(ext):
                try:
                    with open(os.path.join(root, filename), 'r') as rqstd:
                        print("Searching for '{}' in {}...".format(
                            search_for, filename))
                        if search_for in rqstd.read():
                            files_with_search_term.append(
                                os.path.join(root, filename)
                            )
                except UnicodeDecodeError:  # exception thrown for binary files e.g. executibles
                    continue

    print("\nFound the following files with '{}' in the text:".format(search_for))
    for file in files_with_search_term:
        print("**** " + file)
    print()  # adds newline to stdout


def main():
    search(args.string, args.extensions, args.directory)


if __name__ == "__main__":
    main()
