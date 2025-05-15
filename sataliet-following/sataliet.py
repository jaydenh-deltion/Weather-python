import requests
import os 
from dotenv import load_dotenv 

load_dotenv()
api_key = os.environ['API_KEY']
folllow = input('pleas enter the satalite you want to track: ')