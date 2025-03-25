"""
    re.search() looks for the first match anywhere in the string,
    rather than ensuring that the entire string follows the pattern.
    This means that if only a part of the string matches \w+,
    it considers it valid, even if other parts are incorrect.

"""

import re

# email_input=input()
# email_input="info@maktabkhoone.org"
# email_input="!asd234@maktabkhoone.oarg"

# result=re.search(r'\w+@.+\..+',email_input)
# result=re.match(r'\w+@.+\..+',email_input)
# if result== None:
#     print("email input is not correct!!")
# else:
#     print("OK")



email_input = input().strip()
pattern = r'^[A-Za-z0-9]+@[A-Za-z]+\.[A-Za-z]+$'

if re.match(pattern, email_input):
    print("OK")
else:
    print("WRONG")