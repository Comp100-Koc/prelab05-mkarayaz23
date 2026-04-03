def adjacent_duplicates_exist(s, i=0):
    if i >= len(s) - 1:
        return False
    if s[i] == s[i + 1]:
        return True
    return adjacent_duplicates_exist(s, i + 1)


def remove_once(s, i=0):
    if i >= len(s):
        return ""
    if i < len(s) - 1 and s[i] == s[i + 1]:
        return remove_once(s, i + 2)

    return s[i] + remove_once(s, i + 1)


def remove_adjacent_duplicates(s):
    if not adjacent_duplicates_exist(s):
        return s

    new_s = remove_once(s)
    return remove_adjacent_duplicates(new_s)