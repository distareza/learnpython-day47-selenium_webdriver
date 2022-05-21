import configparser
config = configparser.RawConfigParser()
config.read(filenames="../config.properties")

linkedin_user = config.get("linkedin.com", "linkedin_user")
linkedin_pwd = config.get("linkedin.com", "linkedin_pwd")
my_contact_phone_no = config.get("my-personal-info", "phone_no")

my_facebook_account = config.get("facebook.com", "fb_user")
my_facebook_password = config.get("facebook.com", "fb_pwd")

my_twitter_email = config.get("twitter.com", "twitter_email")
my_twitter_account = config.get("twitter.com", "twitter_account")
my_twitter_password = config.get("twitter.com", "twitter_password")

my_instagram_email = config.get("instagram.com", "ig_email")
my_instagram_account = config.get("instagram.com", "ig_account")
my_instagram_password = config.get("instagram.com", "ig_password")
