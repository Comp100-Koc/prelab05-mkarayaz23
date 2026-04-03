def expand_from_center(s, left, right):
    n = len(s)

    while left >= 0 and right < n and s[left] == s[right]:
        left -= 1
        right += 1

    return (left + 1, right - 1)


def longest_palindromic_substring(s):
    n = len(s)
    i = 0
    best_start = 0
    best_end = -1

    while i < n:
        odd_start, odd_end = expand_from_center(s, i, i)
        if (odd_end - odd_start) > (best_end - best_start):
            best_start = odd_start
            best_end = odd_end

        even_start, even_end = expand_from_center(s, i, i + 1)
        if (even_end - even_start) > (best_end - best_start):
            best_start = even_start
            best_end = even_end

        i += 1

    if best_end - best_start + 1 < 2:
        return ""

    return s[best_start:best_end + 1]