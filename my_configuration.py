import configparser
config = configparser.RawConfigParser()
config.read(filenames="../config.properties")

linkedin_user = config.get("linkedin.com", "linkedin_user")
linkedin_pwd = config.get("linkedin.com", "linkedin_pwd")
my_contact_phone_no = config.get("my-personal-info", "phone_no")

my_facebook_account = config.get("facebook.com", "fb_user")
my_facebook_password = config.get("facebook.com", "fb_pwd")
