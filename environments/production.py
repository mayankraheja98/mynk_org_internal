DATABASES = {
    'nyk_prod': {
        'ENGINE': 'django.db.backends.sql',
        'NAME': 'Org_Master',
        'USER': 'admin',
        'PASSWORD': 'admin@123',
        'HOST': 'endpoint.org.com',
        'PORT': '1337',
    }
}

ACCESS_TOKEN_URL = "REDACTED"

BASIC_URL = "https://REDACTED"
BACKEND_URL = "https://REDACTED"


ENVIRONMENT_TYPE = "production"
NYKAA_MAIL_NOTIFICATION_API = "http://REDACTED"
STORE_MASTER_SYNC_ENDPOINT = "http://REDACTED"

AWS_BUCKET_NAME = "s3-bucket-prod-name"

# Sensitive Organization Environment Information can be leaked on github

# Developers often clone repositories into their personal accounts
# Repositories are made Public instead of Private

# All these things should be kept in mind before commit

# Critical secrets should not be stored in code. Secure vault, like AWS secrets manager should be used ALWAYS

Now go to "/flag9" on CTF site to get your flag!
