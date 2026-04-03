
def fill_zeros(a, b):
      if len(a) < len(b):
        a = ('0' * (len(b) - len(a))) + a
      elif len(b) < len(a):
        b = ('0' * (len(a) - len(b))) + b
      return a, b


def add_binary(a, b):
    if a.startswith('0b'):
        a = a[2:]
    if b.startswith('0b'):
        b = b[2:]

    a, b = fill_zeros(a, b)

    i = len(a) - 1
    carry = 0
    result = ''

    while i >= 0:
        bit_a = int(a[i])
        bit_b = int(b[i])
        total = bit_a + bit_b + carry

        if total == 0:
            result = '0' + result
            carry = 0
        elif total == 1:
            result = '1' + result
            carry = 0
        elif total == 2:
            result = '0' + result
            carry = 1
        else:
            result = '1' + result
            carry = 1

        i -= 1

    if carry == 1:
        result = '1' + result

    while len(result) > 1 and result[0] == '0':
        result = result[1:]

    return '0b' + result