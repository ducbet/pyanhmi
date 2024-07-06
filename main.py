from common.Config import Mode, Config
from common.demo_schema_class import User
from common.schema_class import Product, ProductDescription
from common.schema_classes_test import StrClass, StrDataclass
from pyanhmi import LunchBox
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Creator import create

if __name__ == '__main__':
    CookbookRecipe.clear()
    Config.MODE = Mode.STRICT

    db_1_users = {
        # "tmd@gmail.com": {
            "name": "Trieu Duc",
            "email": "tmd@gmail.com",
            "address": "Ba Dinh, Ha Noi",
        # }
    }

    user_1 = User(email=db_1_users["email"],
                  full_name=db_1_users["name"],
                  address=db_1_users["address"],
                  )

    print(user_1)

    db_2_users = {
        # "tmd@gmail.com": {
            "user_name": "Trieu Duc",
            "first_name": "Trieu",
            "last_name": "Duc",
            "user_email": "tmd@gmail.com",
        # }
    }

    user_2 = User(email=db_2_users["user_email"],
                  full_name=db_2_users["user_name"],
                  first_name=db_2_users["first_name"],
                  last_name=db_2_users["last_name"],
                  )

    print(user_2)

    objects_normalizer = LunchBox()
    objects_normalizer.add(user_1)
    objects_normalizer.add(user_2)
    # print(objects_normalizer.export())


    products = {
        0: {
            "id": 0,
            "name": "iphone 12",
            "description": "6.1‑inch...",
            "color": "black",
        }
    }

    orders = {
        5: {
            "mail": "tmd@gmail.com",
            "prd_id": 0,
            "time_stamp": "2024-07-05",
        }
    }




