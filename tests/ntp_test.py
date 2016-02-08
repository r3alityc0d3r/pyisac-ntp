import pytest
import mock
from ntp import Ntp

class Ntp_test:

    @patch.object(Ntp, 'ntp')
    def test_one(self, mock):
        self.assertTrue(mock.called)
