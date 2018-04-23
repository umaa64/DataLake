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


@app.route('/create_curated_datasets', methods=['POST'])
@handle_quickstart_exception("Error occured while creating curated datasets")
@login_required
@mark_step_as_done(step=2)
def create_curated_datasets():
    create_and_load_curated_datasets(app.config)




if __name__ == "__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    args = parse_command_line_args()
    config = read_config(args.config)
    app.secret_key = os.urandom(47)
    app.config.update(config)
    create_curated_datasets()
    app.run(host='0.0.0.0', port=int(config['port']), threaded=True)
