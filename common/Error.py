class InvalidDatatype(Exception):
    def __init__(self, data, expects=None, msg=""):
        message = "Invalid Datatype"
        message += f". {msg}" if msg else ""

        if isinstance(expects, list):
            message += ". Expect Type: " + " or ".join([str(expect) for expect in expects])
        else:
            message += f". Expect Type: {expects}" if expects else ""

        message += f". Actual Type: {type(data)}"
        message += f". Data: {repr(data)}"
        super().__init__(message)
        self.message = message

    def __eq__(self, other):
        return self.message == other.message


class InvalidData(Exception):
    def __init__(self, data, msg=""):
        message = "Invalid Data"
        message += f". {msg}" if msg else ""
        message += f". Data: {repr(data)}"
        super().__init__(message)
        self.message = message

    def __eq__(self, other):
        return self.message == other.message


class ValidatorMissing(Exception):
    def __init__(self, cls, validator, msg=""):
        message = "Validator Missing"
        message += f". {msg}" if msg else ""
        message += f"{validator} is not exist in {cls}"
        super().__init__(message)
        self.message = message

    def __eq__(self, other):
        return self.message == other.message
