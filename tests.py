import operations
from Lab3 import app
from mock import patch, call
import unittest


class Lab3Test(unittest.TestCase):

    @patch("operations.create")
    def test_add(self, mock_add):
        response = app.test_client().post('/api/add/', data={'key': 'testAdd', 'data': 'test'})
        print "add.call_args:", mock_add.call_args
        assert mock_add.call_args == call('testAdd', 'test')

    @patch("operations.delete")
    def test_delete(self, mock_delete):
        response = app.test_client().post('/api/remove/', data={'key': 'new'})
        print "remove.call_args:", mock_delete.call_args
        assert mock_delete.call_args == call('new')

    @patch("operations.update")
    def test_update(self, mock_update_users):
        response = app.test_client().post('api/edit/', data={'key': 'testAdd', 'data': 'test'})
        print "update.call_args:", mock_update_users.call_args
        assert mock_update_users.call_args == call('testAdd', 'test')

    @patch("operations.read")
    def test_read(self, get_one_user_mock):
        get_one_user_mock.return_value = 'Second'
        response = app.test_client().post('/api/read/', data={'key': 'new'})
        print "one.call_args:", get_one_user_mock.call_args
        assert get_one_user_mock.call_args == call('new')
