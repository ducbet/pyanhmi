from common.Config import CastingMode, Config
from common.demo_schema_class import UserDb1, UserDb2, ReportUser
from pyanhmi import LunchBox
from pyanhmi.Cookbook.CookbookRecipe import CookbookRecipe
from pyanhmi.Creator import create

if __name__ == '__main__':
    CookbookRecipe.clear()
    Config.MODE = CastingMode.STRICT

    db_1_users = {
            "name": "Trieu Duc",
            "email": "tmd@gmail.com",
            "address": "Ba Dinh, Ha Noi",
    }

    user_1 = create(db_1_users, UserDb1)
    print(user_1)

    db_2_users = {
            "user_email": "tmd@gmail.com",
            "full_name": "Trieu Minh Duc",
            "first_name": "Trieu",
            "last_name": "Duc",
    }
    user_2 = create(db_2_users, UserDb2)
    print(user_2)

    objects_normalizer = LunchBox()
    objects_normalizer.add(user_1)
    objects_normalizer.add(user_2)
    assert objects_normalizer.convert(ReportUser) == ReportUser(mail=user_2.user_email,
                                                                name=user_2.full_name,
                                                                first_name=user_2.first_name,
                                                                last_name=user_2.last_name,
                                                                address=user_1.address)



