import os , sys, json, calendar, random, datetime

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


