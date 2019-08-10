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


def get_movies(return_count=100):
    """
    Queries for all films, by genre and year
    """

    try:
        global conn
        with conn:
            with conn.cursor() as curs:
                curs.execute("""
                    SELECT title AS title, name AS genre, release_year AS released
                    FROM film f
                    JOIN film_category fc
                        ON f.film_id = fc.film_id
                    JOIN category c
                        ON fc.category_id = c.category_id
                    ORDER BY title
                    LIMIT %s;
                """, (return_count,))

                row = curs.fetchone()
                while row is not None:
                    print(row)
                    row = curs.fetchone()

                print("The number of cities displayed: ", curs.rowcount)
                assert curs.rowcount == return_count, "Incorrect number of cities returned!"
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
    get_movies(10)
    close_conn()


if __name__ == '__main__':
    main()
