import os , sys, json, calendar, random
from datetime import datetime

######
# os #
######

# Cpu core counts
print(os.cpu_count())
# Get current working directory/folder
print(os.getcwd())
print(os.process_cpu_count())
# current working folder
print(os.curdir)
# changing directory
print(os.chdir(f"M:\\React"), os.getcwd())
# Get all environment values in windows
# print(os.environ)

#######
# sys #
#######

# Comman line arguments to run a python file
# Example ['py builtin_modules.py', 'hello']
print(sys.argv)
# Python version configured in your machine
print(sys.base_prefix)
# All builtin module names installed as part of python installed
# print(sys.builtin_module_names)
# Which Platform it uses
print(sys.platform)
# Installed python version in your machine
print(sys.winver)
# Executable python file
print(sys.executable)
# Get argument list from command line in detail with path and aruguments
print(sys.orig_argv)

########
# json #
########

sampleJson = {
    "data" : [
        {
            "name" : "Mahenjeeb",
            "age" : 27,
            "cars" : ["Mercedez", "BMW"]
        },
        {
            "name" : "Peti",
            "age" : 54,
            "cars" : ["Tata", "Rolls Royce"]
        },
        {
            "name" : "Tinga Bapa",
            "age" : 56,
            "cars" : ["That", "Bugatti"]
        },
    ],
    "version" : 1
}
# dumps() Format JSON data and change object type to JSON
formattedJSON = json.dumps(sampleJson, indent=4)
print(formattedJSON)
# loads() Change JSON to Python compitale object
JSONtoObject = json.loads(formattedJSON)
print(JSONtoObject)

############
# calender #
############
cal_month = calendar.monthcalendar(2016, 9)
print(cal_month)

############
# datetime #
############

now = datetime.now()
print(now)
# print(datetime.time())
print(datetime.max, datetime.min)
# String Format Time
strfTime = now.strftime("%Y-%m-%d, %H:%M:%S")
print(strfTime)
# String Parse Time
strPTime = datetime.strptime('2026-09-10', '%Y-%m-%d')
print(strPTime)
print(f"{now.hour}:{now.minute}")
print(datetime.isocalendar(now))
print(datetime.today())
print(datetime.weekday(now))

##########
# random #
##########

print(random.choices(['Rock', 'Paper', 'Scissor']))
# shuffleNumbers = random.shuffle([10,7,12,7,0,3,4,5])
# print(shuffleNumbers)
print(random.getrandbits(10))
print(random.randint(1,10))