# using the implicit interger values of char would be easier, but it doesn't seem like the reference table follows Ascii order
# assessment doesn't mention anything about lower case chars so I'mma assume the encoding is caseless

class Encoder:
    def __init__(self, offset, reference_table):
        self._offset = offset
        self._reference_table = reference_table
        
    @property
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, user_offset):
        self._offset = user_offset.upper()

    @property
    def reference_table(self):
        return self._reference_table

    @reference_table.setter
    def reference_table(self, user_reference_table):
        self._reference_table = user_reference_table


    def encode(self, plainText):
        shift = self._reference_table.index(self._offset.upper())
        reference_table_length = len(self._reference_table)

        encodedText = self._offset

        for c in plainText:
            if c.upper() in self._reference_table:
                new_index = self._reference_table.index(c.upper()) - shift
                if new_index < 0:
                    new_index += reference_table_length
                # # taking advantage of the fact the non alphabetical characters return false for isupper or islower
                # # could have been done with ternary operator, but would make it more unreadeable than it already is
                # if not c.islower():
                #     encodedText += str(self._reference_table[new_index])
                # else:
                #     encodedText += str(self._reference_table[new_index]).lower()
                    
                encodedText += str(self._reference_table[new_index])
            else:
                encodedText += c

        return encodedText


    def decode(self, encodedText):
        shift = self._reference_table.index(encodedText[0])

        plainText = ""

        for c in encodedText[1:]:
            if c.upper() in self._reference_table:
                new_index = self._reference_table.index(c.upper()) + shift
                if new_index > 43:
                    new_index -= 44
                # # taking advantage of the fact the non alphabetical characters return false for isupper or islower
                # # could have been done with ternary operator, but would make it more unreadeable than it already is
                # if not c.islower():
                #     plainText += str(self._reference_table[new_index])
                # else:
                #     plainText += str(self._reference_table[new_index]).lower()
                plainText += str(self._reference_table[new_index])
            else:
                plainText += c

        return plainText


encoder1 = Encoder("F",
            [chr(n) for n in range(65, 91)]
            + list(range(0, 10))
            + [chr(n) for n in range(40, 48)]                       
)

print(encoder1.encode("Hello World"))
print(encoder1.decode("FC/ggj Rjmg."))