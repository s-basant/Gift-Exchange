class DuplicateMemberException(Exception):
    """Members must be unique"""

    pass


class DuplicatePartnerException(Exception):
    """Partner should be unique"""

    pass


class NoSolutionPossibleException(Exception):
    """There not enough members to find solution"""

    pass
