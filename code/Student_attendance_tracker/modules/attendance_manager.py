
from config.settings import (
    SUBJECTS,
    SUBJECT_COLUMNS,
    WARNING_THRESHOLD,
    STAFF_EMAILS
)

from modules.excel_handler import (
    savefile,
    get_student,
    get_leave,
    update_leave
)

from modules.utilityFunctions import (
    mailstu,
    mailstaff
)

# global variables
l1 = []
l2 = ""
l3 = []


def check(no_of_days, row_num, b):

    global l1
    global l2
    global l3

    subject_name = SUBJECTS[b]

    col = SUBJECT_COLUMNS[b]

    for i in range(len(row_num)):

        row = row_num[i] + 1

        total_leave = no_of_days[i]

        update_leave(
            row,
            col,
            total_leave
        )

        roll, name, email = get_student(row)

        print(
            f"{name} -> Updated Leave:"
            f" {total_leave}"
        )

        # warning threshold
        if total_leave == WARNING_THRESHOLD:

            l1.append(email)

        # shortage
        elif total_leave > WARNING_THRESHOLD:

            l3.append(email)

            l2 += str(roll) + ","

    # STUDENT WARNING MAIL
    if len(l1) > 0:

        msg = f"""
Warning!

Your attendance in {subject_name}
has reached the warning threshold.

Please attend classes regularly.
"""

        mailstu(l1, msg)

    # SHORTAGE MAIL
    if len(l3) > 0:

        msg = f"""
Attendance shortage detected in
{subject_name}

Please attend classes regularly.
"""

        mailstu(l3, msg)

        staff_msg = f"""
Students with shortage attendance:

{l2}
"""

        mailstaff(
            STAFF_EMAILS[b],
            staff_msg
        )

    savefile()