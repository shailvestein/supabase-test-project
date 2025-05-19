from dotenv import load_dotenv
from supabase import create_client, Client
import os

load_dotenv()

# SUPABASE_URL = os.getenv('SUPABASE_URL')
# SUPABASE_ANNON_KEY = os.getenv('SUPABASE_ANNON_KEY') 
SUPABASE_URL = "https://hlndxtvvcpxvwmacfjhp.supabase.co"
SUPABASE_ANNON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImhsbmR4dHZ2Y3B4dndtYWNmamhwIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDc1ODEzMTEsImV4cCI6MjA2MzE1NzMxMX0.TIzsLaQNP7fvZjynSY839QB36EN8kz8LDmbKM1JtYsE"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_ANNON_KEY)

# print(supabase)
try:
  response = supabase.table('users').select('*').limit(1).execute()
  print(f"Connection successfull!\nResponse: {response}")
except Exception as e:
  print(f'Connection failed.\nerror {e} occurred!')

# print(response)
