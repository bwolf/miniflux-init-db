#!/usr/bin/env python3

import os
import psycopg2 as db

from psycopg2.extensions import AsIs
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

host = os.environ['DB_POSTGRES_HOST']
password = os.environ['DB_POSTGRES_PASSWORD']

init_database = os.environ['MINIFLUX_DB_NAME']
init_username = os.environ['MINIFLUX_DB_USERNAME']
init_password = os.environ['MINIFLUX_DB_PASSWORD']

with db.connect("host={} dbname=postgres user=postgres password={}".format(
        host, password)) as con:
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with con:
        with con.cursor() as cur:
            print("Creating role {} .. ".format(init_username), end='')
            try:
                cur.execute("CREATE ROLE %s WITH LOGIN PASSWORD %s",
                            (AsIs(init_username), init_password))
            except db.errors.DuplicateObject as e:
                print("{}".format(e.diag.message_primary), end='')
        print()

        with con.cursor() as cur:
            print("Creating database {} .. ".format(init_database), end='')
            try:
                cur.execute("CREATE DATABASE %s OWNER %s",
                            (AsIs(init_database), AsIs(init_username)))
            except db.errors.DuplicateDatabase as e:
                print("{}".format(e.diag.message_primary), end='')
        print()

with db.connect("host={} dbname={} user=postgres password={}".format(
        host, init_database, password)) as con:
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with con:
        with con.cursor() as cur:
            print("Creating extension hstore .. ", end='')
            try:
                cur.execute("CREATE EXTENSION hstore")
            except db.errors.DuplicateObject as e:
                print("{}".format(e.diag.message_primary))
            print()

# EOF
