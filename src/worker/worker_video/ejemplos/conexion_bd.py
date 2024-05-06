#script ejemplo que se puede correr dentro del docker de este contendedor
# para ejecutar una consulta sql en la base postgres
from sqlalchemy import create_engine
import os

database_ip = os.environ['DATABASE_IP']

engine = create_engine('postgresql://admin:admin@{database_ip}:5432/idlr_db')
conn = engine.connect()

query = "UPDATE tasks SET status='processed' WHERE id=1"
#query2 = "select * from tasks"
result = conn.execute(query)
#result2 = conn.execute(query2)
print(result.fetchall())
result.close()





