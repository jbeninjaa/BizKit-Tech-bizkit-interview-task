from flask import Blueprint, request, json

bp = Blueprint("schedule", __name__, url_prefix = "/schedule")

from .data.search_data import USERS

USER_SCHEDULES = []

@bp.route("")
def hello():
    return "hello world"

 
@bp.route("<int:user_id>", methods=["POST"])
def schedule(user_id):
    # parse request body
    schedule_json = request.json

    # extract request data
    start_sched = schedule_json[0]["start"]
    end_sched = schedule_json[0]["end"]


    schedules = []
    schedule = start_sched + " - " + end_sched

    # check if user already exists 
    user_exists = any(user["user_id"] == str(user_id) for user in USER_SCHEDULES)

    if user_exists:
        # find the user_id and append the schedule if not yet present
        for user in USER_SCHEDULES:
            if user["user_id"] == str(user_id) and schedule not in user["schedule"]:
                user["schedule"].append(schedule)
            return USER_SCHEDULES
        
    else:
        # create a schedule for the user
        schedules.append(schedule)
        user_schedule = {
            "user_id": str(user_id),
            "schedule": schedules
        }
        USER_SCHEDULES.append(user_schedule)
        return USER_SCHEDULES

