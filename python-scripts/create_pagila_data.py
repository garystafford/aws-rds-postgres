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
        global conn
        conn = psycopg2.connect(**params)
        print('Connection to database created')
    except (Exception, psycopg2.DatabaseError) as error:
        print(set_connection.__name__, error)
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
                return db_version
    except (psycopg2.OperationalError, psycopg2.DatabaseError) as error:
        print(db_info.__name__, error)
        close_conn()
        exit(1)


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
                print('Pagila SQL scripts completed')
    except (psycopg2.OperationalError, psycopg2.DatabaseError, FileNotFoundError) as error:
        print(create_pagila_db.__name__, error)
        close_conn()
        exit(1)


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
                return table_count
    except (psycopg2.OperationalError, psycopg2.DatabaseError) as error:
        print(get_table_count.__name__, error)
        close_conn()
        exit(1)


def close_conn():
    """
    Closes database connection
    """
    if conn is not None:
        conn.close()
        print('Database connection closed.')


def main():
    set_connection('docker')
    print(db_info())
    print(create_pagila_db())
    get_table_count()
    close_conn()


if __name__ == '__main__':
    main()
