import os

# This is an example of a potential security vulnerability
SECRET_KEY = "hardcoded_secret_key"

def insecure_function(user_input):
    # This is an example of potential SQL injection
    query = f"SELECT * FROM users WHERE username = '{user_input}'"
    # Execute query (this is just an example, don't actually do this!)
    return query #sadadssaadfasdZxZXZ
