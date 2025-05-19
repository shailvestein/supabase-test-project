from dotenv import load_dotenv
from supabase import create_client, Client
import os

load_dotenv()

SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_ANNON_KEY = os.getenv('SUPABASE_ANNON_KEY') 

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANNON_KEY)

# print(supabase)
try:
  response = supabase.table('users').select('*').limit(1).execute()
  print(f"Connection successfull!\nResponse: {response}")
except Exception as e:
  print(f'Connection failed.\nerror {e} occurred!')

# print(response)