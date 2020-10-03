class SequenceError(Exception):
    pass

class UnsupportedTypeError(SequenceError):
    def __init__(self, message):
        self.message = message

class UnsupportedSplitTypeError(SequenceError):
    def __init__(self, message):
        self.message = message