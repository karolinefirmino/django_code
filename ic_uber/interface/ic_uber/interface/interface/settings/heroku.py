import environ

from interface.settings.base import *

env = environ.Env()

DEBUG = env.boot("DEGUB", True)

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = [env.list("ALLOWED_HOSTS")]

ALLOWED_HOSTS += [   '*',
	'0.0.0.0',
	'boiling-taiga-97630.herokuapp.com',
  	'127.0.0.1',
  	]

DATABASES = {
	"default": env.db()
}