import pytest

class TestUsers:

    def test_register(self):
        assert True

    def test_login(self):
        assert True

    @pytest.mark.order(2)
    def test_search(self):
        assert True

    @pytest.mark.order(1)
    def test_add_cart(self):
        assert True

    def test_add_adrres(self):
        assert True

    def test_add_order(self):
        assert True