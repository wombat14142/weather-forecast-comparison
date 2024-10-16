import psycopg2
from psycopg2 import sql


# database
db_url = "postgresql://postgres:TpwJNGnvzwqnUkxnPGLUBxvujQDtmrqi@junction.proxy.rlwy.net:19549/railway"
# this is the public port. internal: db_port = "5432"
db_port = "19549"
# this is the public host. internal: db_host = "postgres.railway.internal"
db_host = "junction.proxy.rlwy.net" 
db_user = "postgres"
db_password= "TpwJNGnvzwqnUkxnPGLUBxvujQDtmrqi"
db_name = "railway"

# Verbindung herstellen
try:
    connection = psycopg2.connect(
        host=db_host,
        port=db_port,
        user=db_user,
        password=db_password,
        database=db_name,
    )
    
    cursor = connection.cursor()
    print("Verbindung zur Datenbank erfolgreich!")

    # Beispielabfrage
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Datenbank-Version:", db_version)

except Exception as error:
    print("Fehler bei der Verbindung zur Datenbank:", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Datenbankverbindung geschlossen.")
