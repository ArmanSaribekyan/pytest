import Bookkp
import pytest


class TestClass:

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print("method setup")

    def teardown(self):
        print("method teardown")

    @pytest.mark.parametrize('number, result', [('2207 876234', True),
                                                 ('11-2', True),
                                                 ('10006', True),
                                                 ('007', False)])
    def test_shelf_number(self, number, result):
        assert Bookkp.shelf_number(number) == result

    @pytest.mark.parametrize('number, result', [('2207 876234', True),
                                                 ('11-2', True),
                                                 ('10006', True),
                                                 ('007', False)])
    def test_pers_docum(self, number, result):
        assert Bookkp.pers_docum(number) == result

    @pytest.mark.parametrize('type, number, name, '
                             'directories, result', [('passport', '1234', '1 Name', '3', True),
                                                     ('invoice', '2341', '2 Name', '2', True),
                                                     ('insurance', '3412', '3 Name', '1', True),
                                                     ('passport', '4123', '4 Name', '4', False)])
    def test_add_doc(self, type, number, name, directories, result):
        assert Bookkp.add_doc(type, number, name, directories) == result

    def test_list_doc(self):
        assert Bookkp.list_doc()

    def teardown_class(self):
        print('method teardown_class')


