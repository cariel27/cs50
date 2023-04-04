import re

'''
. any character except newline
* 0 or more repetitions
+ 1 or more repetitions
? 0 or 1 repetitions
{m} m repetitions
{m,n} m-n repetitions
[] set of characters
[^] complementing the set

^ Matches the start of the string
$ Matches the end of the string or just before the newline at the end of the string

\d decimal digit
\D not a decimal digit
\s whitespace characters
\S not a whitespace character
\w word character ... as well as number and underscore
\W not a word character

A|B either A or B
(...) a group: e.g. (edu|gov|ar)
(?:...) 
'''


# https://youtu.be/hy3sd9MOAcc?t=3740
# cristianarielibanez@cs50.ed.harvard.edu
def is_email_valid(email: str):
    return True if re.search(pattern=r"^(\w+\.?\-?)+@(\w+\.)*(\w+\-?)*\w+\.edu$", string=email,
                             flags=re.IGNORECASE) else False
    # return True if re.fullmatch(pattern=r"(\w+\.?\-?)+@(\w+\.)*(\w+\-?)*\w+\.edu", string=email,
    #                             flags=re.IGNORECASE) else False
    # return True if re.match(pattern=r"(\w+\.?\-?)+@(\w+\.)*(\w+\-?)*\w+\.edu$", string=email,
    #                         flags=re.IGNORECASE) else False
    # return True if re.search(pattern=r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", string=email) else False
    # return True if re.search(pattern=r"^[^@]+@[^@]+\.edu$", string=email) else False
    # return True if re.search(pattern=r"^.+@.+\.edu$", string=email) else False

# xx.xx.xx
# (\w+\.?)+
