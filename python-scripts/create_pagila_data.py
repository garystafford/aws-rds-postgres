#!/usr/bin/env python3

import psycopg2

from db_config import config

conn = None  # global variable


def set_connection(section):
    """
    Gets connection to PostgreSQL database instance
    :param section: section of database configuration file to use
    :return: db connection
    """

    try:
        params = config(filename='database.ini', section=section)
        print('Connecting to the PostgreSQL database...')
        global conn
        conn = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.close()
        exit(1)


def db_info():
    """
    Gets database information
    """

    try:
        global conn
        with conn:
            with conn.cursor() as curs:
                curs.execute('SELECT version()')
                db_version = curs.fetchone()
                print('PostgreSQL database version:', db_version)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.close()


def create_pagila_db():
    """
    Creates Pagila database by running DDL and DML scripts
    """

    try:
        global conn
        with conn:
            with conn.cursor() as curs:
                curs.execute(open("../sql-scripts/pagila-schema.sql", "r").read())  # DDL
                curs.execute(open("../sql-scripts/pagila-insert-data.sql", "r").read())  # DML
                conn.commit()
                print('Pagila scripts complete.')
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.close()


def get_table_count():
    """
    Queries database for table count as a test
    """

    try:
        global conn
        with conn:
            with conn.cursor() as curs:
                curs.execute("""
                    SELECT COUNT(*)
                    FROM information_schema.tables
                    WHERE table_schema = 'public';
                """)

                table_count = curs.fetchone()[0]  # returns tuple (28,)
                print("Number of database tables: ", table_count)
                assert table_count == 28, "Incorrect table count!"
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.close()


def close_conn():
    """
    Closes database connection
    """
    if conn is not None:
        conn.close()
        print('Database connection closed.')


def main():
    set_connection('master')
    db_info()
    create_pagila_db()
    get_table_count()
    close_conn()


if __name__ == '__main__':
    main()
