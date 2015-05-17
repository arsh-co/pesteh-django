# -*- coding: utf-8 -*-


def generate_user_token():
    import string
    import random

    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    random_id = ''.join(random.choice(chars) for _ in range(50))
    return u"PESTEH-ut-P{}".format(random_id)
