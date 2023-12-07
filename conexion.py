import psycopg2

# Connection parameters
host = "localhost"
database = "femcoprueba"
user = "postgres"
password = "root"

# Establish a connection
conn = psycopg2.connect(host=host, database=database, user=user, password=password)

cur = conn.cursor()


