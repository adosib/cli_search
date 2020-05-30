# Python Text Search CLI
(https://www.partialdifferential.com/media/post_cards/cli_text_search.jpeg)

## What
This is a basic text search CLI created using the argparse python package. 
At the moment, all this utility does is take a string of text and parses files in a provided directory for the text. The standard 
output is the resulting files in which the text was found.

For more detailed information on set-up and running from 
the command line, please see [my blog post](https://www.partialdifferential.com/post/creating-a-basic-search-cli-with-python/) where I work through the project set-up, installation, and running.

## Installing
Clone the contents of this repo and in the project's root directory run
```bash
$ pip install -e .
```

## Running
Replace the items in angle brackets with the appropriate commands. The -ext and -root arguments are optional.
- ext is a list of space-separated extensions to filter the files being searched (e.g. only search .js and .py files)
- root is a string representing the root directory to crawl for files to parse. Default is the current working directory.
```bash
$ python search.py "<some string here>" -ext <list of space-separated extensions e.g.: .py .js .html> -root "</some/root/directory/path>"
```