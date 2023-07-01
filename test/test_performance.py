from pyanhmi.Helper import Helper


def test_str_constructor():
    @Helper.timer
    def str_1(data):
        for i in range(loop_total):
            a = str(data)
    @Helper.timer
    def str_2(data):
        for i in range(loop_total):
            a = data

    @Helper.timer
    def str_3(data):
        for i in range(loop_total):
            if isinstance(data, str):
                a = data

    loop_total = 1000000
    print()
    str_1("hqwuihekanhqwuihekanskdahqwuihekanskdahqwuihekanskdahqwuihekanskdahqwuihekanskdaskda")
    str_2("hqwuihekanhqwuihekanskdahqwuihekanskdahqwuihekanskdahqwuihekanskdahqwuihekanskdaskda")
    str_3("hqwuihekanhqwuihekanskdahqwuihekanskdahqwuihekanskdahqwuihekanskdahqwuihekanskdaskda")