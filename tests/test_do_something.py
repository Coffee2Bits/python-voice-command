from unittest import TestCase
from unittest.mock import patch

from example.do_something import run


class TestDoSomething(TestCase):

    @patch('builtins.print')
    def test_run(self, mock_print):
        run()
        mock_print.assert_called_with("I'm alive!")
