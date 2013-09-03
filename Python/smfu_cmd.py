#!/usr/bin/env python

import argparse
import json
import os

from smfu import Shortener

conf_parser = argparse.ArgumentParser(description="Create a shortened URL using smfu.in",
                add_help=False)

conf_parser.add_argument("-config", "--config-file", help="Specify config file",
            metavar="FILE")

parser = argparse.ArgumentParser(parents=(conf_parser,))
parser.add_argument("url", help="URL to shorten")
parser.add_argument("-s", "--short-url", help="Only show the urlkey",
                    action="store_false")
parser.add_argument("-k", "--key", help="API key")
parser.add_argument("-v", "--verbose", help="increase verbosity", action="store_true")


conf_args, remaining_args = conf_parser.parse_known_args()
args = parser.parse_args(remaining_args)

if conf_args.config_file:
    config = conf_args.config_file
    if not os.path.isfile(config):
        parser.error("Invalid config file -- file does not exist")

    conf_file = json.load(open(config))
    api_key = conf_file.get('key', None)

else:
    api_key = args.key
    if not api_key:
        parser.error("Need to specify a config file or an API key")

url = args.url

short = Shortener(url=url, key=api_key)
ret_json = short.shorten(args.short_url)

if args.verbose:
    print(json.dumps(ret_json, indent=4))

else:
    print("Shortened URL:\t" + ret_json[0]['urlkey'])
    print("URL shortened:\t" + ret_json[0]['url'])
