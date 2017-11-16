#!/usr/bin/env python
# vim:fileencoding=utf-8
# Author: Shinya Suzuki
# Created: 2017-11-16

from application import app, db
from application.models import init
import click


@app.cli.command(help="Initialize database")
def initdb():
    init()
    click.echo("Database is initialized.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
