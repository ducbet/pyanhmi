class Config:
    cached_rules_flag = "IS_RULE_CACHED"
    normalize_rules_field_name = "NORMALIZE_RULES"
    normalize_rules_field_name_2 = "__NORMALIZE_RULES"
    localize_rules_field_name = "LOCALIZE_RULES"

    ObjAtt_priority = 100
    OrderedDict_priority = 60
    DictAtt_priority = 50
    ListAtt_priority = 50
    SetAtt_priority = 50
    TupleAtt_priority = 50
    UnionAtt_priority = 50
    PRIMITIVE_TYPE_PRIORITY = 10
    AnyAtt_priority = 0

    DISCRIMINATE_PRIMITIVE_TYPES = False

