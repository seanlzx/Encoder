# using the implicit interger values of char would be easier, but it doesn't seem like the reference table follows Ascii order
# assessment doesn't mention anything about lower case chars so I'mma assume the encoding is caseless
offset = "F"
reference_table = (
    [chr(n) for n in range(65, 91)]
    + list(range(0, 10))
    + [chr(n) for n in range(40, 48)]
)

print(len(reference_table))


def get_offset():
    pass


def set_offset():
    pass


def get_reference_table():
    return reference_table


def set_reference_table(user_reference_table):
    reference_table = user_reference_table


def encode(plaintext):
    shift = reference_table.index(offset.upper())
    reference_table_length = len(reference_table)

    encodedText = ""

    for c in plaintext:
        if c.upper() in reference_table:
            new_index = reference_table.index(c.upper()) - shift
            if new_index < 0:
                new_index += reference_table_length
            # taking advantage of the fact the non alphabetical characters return false for isupper or islower
            # could have been done with ternary operator, but would make it more unreadeable than it already is
            if not c.islower():
                encodedText += str(reference_table[new_index])
            else:
                encodedText += str(reference_table[new_index]).lower()
        else:
            encodedText += c

    return encodedText


def decode(encodedText):
    pass


print(encode("Hello World"))
