import unittest2

import create_pagila_data as cpd
import query_postgres as qps


class CreatePagilaDataTests(unittest2.TestCase):
    def setUp(self):
        cpd.set_connection('master')

    def tearDown(self):
        cpd.close_conn()

    def test_set_connection(self):
        self.assertIsNotNone(cpd.conn)

    def test_db_info(self):
        expected_output = 'PostgreSQL 13.2'
        self.assertIn(expected_output, str(cpd.db_info()))

    def test_get_table_count(self):
        # assumes cpd.create_pagila_db() already run successfully
        expected_output = 28
        self.assertEqual(expected_output, cpd.get_table_count())


class QueryPostgresTests(unittest2.TestCase):
    def setUp(self):
        qps.set_connection('master')

    def test_get_movies(self):
        expected_output = 10
        movies = qps.get_movies(10)
        self.assertEqual(expected_output, len(movies))


if __name__ == '__main__':
    unittest2.main()
