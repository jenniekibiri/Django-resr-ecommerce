import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_method(self, category_factory):
        data = category_factory()
        assert data.__str__() == data.name

class TestBrandModel:
    def test_str_method(sel, brand_factory):
        data = brand_factory()
        assert data.__str__( )== data.name

class TestProductModel:
    def test_str_method(sel, product_factory, brand_factory, category_factory):
        data = product_factory(
            name="test_product1",
            description="test_description",
            is_digital=False,
            brand=brand_factory( 
                name="test_brand",
            ),
            category=category_factory(
                name="test_category",
            ),

        )
        assert data.__str__()=="test_product1"
        assert data.brand.__str__()=="test_brand"
        assert data.category.__str__()=="test_category"
        assert data.description=="test_description"
      