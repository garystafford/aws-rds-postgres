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
    except (Exception, psycopg2.DatabaseError) as err:
        print(set_connection.__name__, err)
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

                movies = []
                row = curs.fetchone()
                while row is not None:
                    movies.append(row)
                    row = curs.fetchone()

                return movies
    except (psycopg2.OperationalError, psycopg2.DatabaseError) as err:
        print(get_movies.__name__, err)
    finally:
        close_conn()


def close_conn():
    """
    Closes database connection
    """
    if conn is not None:
        conn.close()
        print('Database connection closed')


def main():
    set_connection('docker')
    for movie in get_movies(10):
        print('Movie: {0}, Genre: {1}, Released: {2}'
              .format(movie[0], movie[1], movie[2]))


if __name__ == '__main__':
    main()
