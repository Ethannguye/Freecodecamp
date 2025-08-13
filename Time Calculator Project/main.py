# This entrypoint file is used for development and testing.
# Start by reading README.md for project instructions.

from time_calculator import add_time
from unittest import main

# ----- Manual test -----
# You can change the values below to try your own test cases.
print(add_time("11:06 PM", "2:02"))
print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))

# ----- Automatic unit tests -----
# This will run all tests inside test_module.py
main(module='test_module', exit=False)
