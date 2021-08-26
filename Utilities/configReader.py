from configparser import ConfigParser

# config = ConfigParser()
# config.read("config.ini")
# print(config.get("locator","username"))
# print(config.get("basic info","testsiteurl"))


def readConfig(section,key):
    config = ConfigParser()
    config.read("..\\ConfigurationData\\conf.ini")
    return config.get(section,key)

print(readConfig("locators","name_XPATH"))