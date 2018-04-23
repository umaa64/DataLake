import argparse
import os

import multiprocessing
from configparser import ConfigParser

import functools

import logging

import sys

from flask import (
    Flask,
    render_template,
    request,
    session,
    jsonify,
    abort
)
from flask import redirect
from flask import url_for

from analysis.transformations import *

test = Flask(
    __name__,
    template_folder=os.path.join(PROJECT_DIR, 'web/templates'),
    static_folder=os.path.join(PROJECT_DIR, 'web/static')
)


def parse_command_line_args():
    parser = argparse.ArgumentParser(description='Quick start App')
    parser.add_argument('--config', required=True, help='Configuration')
    return parser.parse_args()

def read_config(config_path):
    parser = ConfigParser()
    parser.read(config_path)
    config = {}
    for section in parser.sections():
        for (config_key, config_value) in parser.items(section):
            config[config_key] = config_value
    return config

logging.basicConfig(stream=sys.stderr, level=logging.INFO)
args = parse_command_line_args()
config = read_config(args.config)
test.secret_key = os.urandom(47)
test.config.update(config)

print("123")
create_and_load_curated_datasets(test.config)
