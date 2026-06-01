
from config.settings import SUBJECT_COLUMNS

from modules.attendance_manager import check

from modules.excel_handler import get_leave

print("\n===== STUDENT ATTENDANCE TRACKER =====\n")

print("Subjects")
print("1 -> Java")
print("2 -> ML")
print("3 -> Python")

b = int(
    input("\nEnter Subject Code: ")
)

absent = input(
    "\nEnter absent roll numbers separated by comma: "
)

row_num = list(
    map(
        int,
        absent.split(",")
    )
)

col = SUBJECT_COLUMNS[b]

no_of_days = []

# calculate updated leaves
for roll in row_num:

    row = roll + 1

    current = get_leave(row, col)

    updated = current + 1

    no_of_days.append(updated)

# call function
check(
    no_of_days,
    row_num,
    b
)