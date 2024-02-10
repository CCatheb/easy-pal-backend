from sql.sql_client import DatabaseManager

client = DatabaseManager()
output = client.execute_query("INSERT INTO public.api_author (name) VALUES ('Sarah J. Maas') RETURNING id;")

print(output)

output = client.execute_query("SELECT * FROM public.api_author")
print(output)
