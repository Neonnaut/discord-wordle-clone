import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")

CHECK = ':white_check_mark'
ERR = 'x'
WARN = ':warning:'