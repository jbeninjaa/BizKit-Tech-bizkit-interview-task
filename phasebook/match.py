import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200


def is_match(fave_numbers_1, fave_numbers_2):
    # == Prev code
    '''
    for number in fave_numbers_2:
        if number not in fave_numbers_1:
            return False

    return True
    '''

    #  == New code

    # Sort both both list
    fave_numbers_1.sort()
    fave_numbers_2.sort()

    # Initialize Variables
    pointer_fn1 = 0 
    pointer_fn2 = 0
    len_fn1 = len(fave_numbers_1) 
    len_fn2 = len(fave_numbers_2)

    # Traverse 
    while(pointer_fn1 < len_fn1 and pointer_fn2 < len_fn2):
        # If we find a match, we increase both pointers to check the next index
        if(fave_numbers_1[pointer_fn1] == fave_numbers_2[pointer_fn2]):
            pointer_fn2 += 1
        pointer_fn1 += 1 # If we don't find a match, increase pointer for fn1 to look for a match.

    # if pointer_fn2 reaches the length of fn2, it means all numbers in fn2 is present in fn1
    return pointer_fn2 == len_fn2
    
