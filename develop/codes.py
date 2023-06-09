from random import choice           # for choosing letters randomly
from string import ascii_lowercase  # for getting all letters

CODE_VERIFIER_LEN = 64

def getCodeVerifier():
    # choose from all lowercase letter
    letters = ascii_lowercase
    result_str = ''.join(choice(letters) for i in range(CODE_VERIFIER_LEN))
    return result_str

if __name__ == "__main__":
    print(getCodeVerifier())
    