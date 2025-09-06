"""def can_apply(perfect_grades, age):
    if not perfect_grades:
        return "poor grades"
    if age <= 5:
        return "too young"
    if age <= 10:
        return "elementary"
    if age <= 14:
        return "middle"
    elif age <= 18:
        return "high school"
    return "too old"

print(can_apply(False, 5))
print(can_apply(True, 14))

# if not perfect_grades: и if age <= 14:
"""

# def  f(a):
#     def g():
#         nonlocal a
#         print(a, end = ' ')
#         a += 1
#     return g
#
# g = f(10)
# g()
# g()  # 10 11

# import re
# string = "as32..4..Fh.d6kJ3.94asd"
# pattern = r".\.\D\d\w{2}"
# print(re.findall(pattern, string))      # ['h.d6kJ']


class Logger:
    DEBUG = 5
    INFO = 4
    WARN = 3
    ERROR = 2
    FATAL = 1
    _level = DEBUG

    def __init__(self):
        Logger._level = Logger.DEBUG

    @classmethod
    def is_level(cls, level):
        return cls._level >= level

    @classmethod
    def debug(cls, message):
        if cls.is_level(Logger.DEBUG):
            print(f"DEBUG: {message}")

    @classmethod
    def info(cls, message):
        if cls.is_level(Logger.INFO):
            print(f"INFO: {message}")

    @classmethod
    def warn(cls, message):
        if cls.is_level(Logger.WARN):
            print(f"WARN: {message}")

    @classmethod
    def error(cls, message):
        if cls.is_level(Logger.ERROR):
            print(f"ERROR: {message}")

    @classmethod
    def fatal(cls, message):
        if cls.is_level(Logger.FATAL):
            print(f"FATAL: {message}")


def log_all():
    Logger.debug("This is a Debug message.")
    Logger.info("This is a Info message.")
    Logger.warn("This is a Warn message.")
    Logger.error("This is a Error message.")
    Logger.fatal("This is a Fatal message.")


Logger._level = Logger.ERROR
log_all()



