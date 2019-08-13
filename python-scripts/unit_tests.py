import unittest
import create_pagila_data as cpd


class MyTestCase(unittest.TestCase):
    def setUp(self):
        cpd.set_connection('docker')

    def tearDown(self):
        cpd.close_conn()

    def test_set_connection(self):
        # expected_output = 'Connection to database created'
        # self.assertIn(expected_output, str(cpd.set_connection('docker')))
        self.assertIsNotNone(cpd.conn)

    def test_db_info(self):
        expected_output = 'PostgreSQL 11.4'
        self.assertIn(expected_output, str(cpd.db_info()))

    # def test_create_pagila_db(self):
    #     expected_output = 'Pagila SQL scripts completed'
    #     # self.assertIn(expected_output, str(cpd.create_pagila_db()))
    #     # expected_output = 'create_pagila_db type "mpaa_rating" already exists'
    #     # self.assertNotEqual(expected_output, str(cpd.create_pagila_db()))

    def test_get_table_count(self):
        expected_output = 28
        self.assertEqual(expected_output, cpd.get_table_count())


if __name__ == '__main__':
    unittest.main()
