# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

# Define Convesions
def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

# Print Menu Options
print('What would you like to convert to (enter the number):')
print('1: KPH')
print('2: m/s')
print('3: ft/s')
selection = int(input())

# Define Get mph to improve useablility 
def get_mph():    
    mph = input("Input speed in mph: ")
    mph = float(mph)
    return mph

# Run Menu Conditionals 
# Call get mph and convert and print
if selection == 1:
    mph = get_mph()
    print("Speed in kph is", mph_to_kph(mph))
elif selection == 2:
    mph = get_mph()
    print("Speed in m/s is", mph_to_ms(mph))
elif selection == 3:
    mph = get_mph()
    print("Speed in ft/s is", mph_to_fts(mph))
else:
    print('Not a valid menu selection')
