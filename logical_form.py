class LogicalFormWH:
    def __init__(self, r=[], p=[]):
        self.r, self.p = r, p

    def __str__(self):
        return "WH b: (&{}) {}".format("".join(self.r), "".join(self.p))

    def __del__(self):
        print("")
