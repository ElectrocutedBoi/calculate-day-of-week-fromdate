from enum import Enum
from math import floor
from sys import exit

class DayOfWeek(Enum):
  MONDAY       = 1
  TUESDAY      = 2
  WEDNESDAY    = 3
  THURSDAY     = 4
  FRIDAY       = 5
  SATURDAY     = 6
  SUNDAY       = 0

  def __str__(self):
    d = self
    if d == DayOfWeek.MONDAY:
      return "Monday"
    elif d == DayOfWeek.TUESDAY:
      return "Tuesday"
    elif d == DayOfWeek.WEDNESDAY:
      return "Wednesday"
    elif d == DayOfWeek.THURSDAY:
      return "Thursday"
    elif d == DayOfWeek.FRIDAY:
      return "Friday"
    elif d == DayOfWeek.SATURDAY:
      return "Saturday"
    elif d == DayOfWeek.SUNDAY:
      return "Sunday"
    else:
      raise NotImplementedError

  @staticmethod
  def calculate_day_of_week(m, d, y):
    c = floor(y / 100) 
    y = y - c * 100
    day_of_week = (d + floor(2.6 * (m - 2) - 0.2) - 2 * c + y + floor(y / 4) + floor(c / 4)) % 7
  
    return DayOfWeek(day_of_week)

# --------------------------------------------------
  
def cli():
  while True:
    m = int(input("Input month: "))
    d = int(input("Input day: "))
    y = int(input("Input year: "))
    day_of_week = DayOfWeek.calculate_day_of_week(m, d, y)
    print(f"Day of week: {str(day_of_week)}\n")

def cli_keyboard_interrupt():
  try:
    cli()
  except KeyboardInterrupt:
    exit(0) # Gracefully exit program
  
# This is pretty useful also imported as a library
if __name__ == "__main__":
  cli_keyboard_interrupt()