from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    # ============
    
    # Stores the list of users that match the search parameters
    result = []

    # Extract parameters 
    params_id = args.get("id")
    params_name = args.get("name")
    params_age = args.get("age")
    params_occupation = args.get("occupation")
    
    # If there are no search parameters, return all users
    if not args:
        return USERS

    """ FIRST IMPLEMENTATION 

    for user in USERS: 
        # If {params_...} is stated and matches a user in USERS, append to result list then continue to the next iteration to avoid duplicates

            # Check for ID, 
        if params_id is not None and params_id == user["id"]:
            result.append(user)
            continue
        
            # Check for name, .lower() since it's case insensitive 
        if params_name is not None and params_name.lower() in user["name"].lower():
            result.append(user)
            continue

            # Check for age in the range of params_age +- 1
        if params_age is not None: 
            age = int(params_age)
            if user["age"] in (age - 1, age, age + 1):
                result.append(user)
                continue

            # Check for occupation, .lower() since it's case insensitive
        if params_occupation is not None and params_occupation.lower() in user["occupation"].lower():
            result.append(user)
            continue
    """

    # BONUS CHALLENGE

    # Check ID 
    if params_id is not None:
        for user in USERS:
            if params_id == user["id"] and user not in result:
                result.append(user)

    # Check name
    if params_name is not None:
        for user in USERS:
            if params_name.lower() in user["name"].lower() and user not in result:
                result.append(user)

    # Check age 
    if params_age is not None:
        for user in USERS:
            age = int(params_age)
            if user["age"] in (age -1, age, age+1) and user not in result:
                result.append(user)

    # Check occupation
    if params_occupation is not None:
        for user in USERS:
            if params_occupation.lower() in user["occupation"].lower() and user not in result:
                result.append(user)
        
    return result

        

