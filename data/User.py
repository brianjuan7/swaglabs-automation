from utilities import Encryption

USERNAME = "gAAAAABmJ8TVvPP4gtSlkoyBW6lbNsOc5bWRZ15_WV_KpLtbwsLlwiU12G6hVqMjLhu7XSHQJLsjttpcXtGA1Oh1xVtrOMvH4Q=="
PASSWORD = "gAAAAABmJ8V-Wo1MPCkAQZTtANY49m5UZQk6ZK_PbUs4ZZLTgAIilbZaNQAkY6TZBGJzUo1vf5MkZpkzZrHpo_C35-5BwX9Tbg=="
INVALID_USERNAME = "invalid_username"
INVALID_PASSWORD = "invalid_password"
FIRST_NAME = "Brian"
LAST_NAME = "Juan"
POSTAL_CODE = 1111
PAYMENT_INFORMATION = "SauceCard #31337"
SHIPPING_INFORMATION = "Free Pony Express Delivery!"


def get_username():
    return Encryption.decrypt(USERNAME)


def get_password():
    return Encryption.decrypt(PASSWORD)
