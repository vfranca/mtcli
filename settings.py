import os
from dotenv import load_dotenv

load_dotenv()
DATABASE = os.getenv("DATABASE")
