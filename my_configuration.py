import configparser
config = configparser.RawConfigParser()
config.read(filenames="../config.properties")

linkedin_user = config.get("linkedin.com", "linkedin_user")
linkedin_pwd = config.get("linkedin.com", "linkedin_pwd")
my_contact_phone_no = "+1234567890"

