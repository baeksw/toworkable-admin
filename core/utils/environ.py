import os 
from pathlib import Path

from dotenv import load_dotenv

class Environ:
    
    LOG_LEVEL = os.environ.get('LOG_LEVEL')
 