from typing import List

from common.schema_class import Product


class MysqlClient:
    def __init__(self):
        pass

    def get_all_products(self) -> List[Product]:
        product = {"id": 1, "name": "Table"}
        return [Product(**product)]