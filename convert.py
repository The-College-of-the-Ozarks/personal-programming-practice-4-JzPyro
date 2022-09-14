# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

mph = input("Input speed in mph: ")
mph = float(mph)

print("Speed in kph is", mph_to_kph(mph))

print("Speed in m/s is", mph_to_ms(mph))

print("Speed in ft/s is", mph_to_fts(mph))
