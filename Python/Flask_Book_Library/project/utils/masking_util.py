import string


def mask_str(str_to_mask) -> string:
    str_len = len(str_to_mask)
    return str_len * '*'
