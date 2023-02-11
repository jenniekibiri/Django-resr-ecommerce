import pytest
import json
pytestmark =pytest.mark.django_db


class TestCategoryEndpoints:
    endpoint = "/api/category/"

    def test_get_category(self, api_client, category_factory):
        category_factory.create_batch(10)
    
        response = api_client().get(self.endpoint)
        print (json.loads(response.content))
        assert response.status_code == 200
        assert len(json.loads(response.content)) ==10



class TestBrandEndpoints:
    endpoint ="/api/brand/"
    def test_get_brand(self,api_client,brand_factory):
        brand_factory.create_batch(10)
        response = api_client().get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) ==10


class TestProductEndPoints:
    product_endpoint = "/api/product/"
    def test_get_product(self,api_client,product_factory):
        product_factory.create_batch(10)
        response = api_client().get(self.product_endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) ==10
