import pytest
import ya_disk_create_folder


class TestDisk:

    def setup_class(self):
        print('method setup_class')

    def setup(self):
        print("method setup")

    def teardown(self):
        print("method teardown")

    @pytest.mark.parametrize('folder_name, response', [('folder', 201),
                                                       ('folder', 409)])
    def test_create_folder(self, folder_name, response):
        assert ya_disk_create_folder.create_folder(folder_name) == response

    @pytest.mark.parametrize('folder_name, response', [('folder', 200),
                                                       ('my_folder', 404)])
    def test_folder_search(self, folder_name, response):
        assert ya_disk_create_folder.folder_search(folder_name) == response

    def teardown_class(self):
        print('method teardown_class')