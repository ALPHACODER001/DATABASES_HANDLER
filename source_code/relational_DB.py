import Data_Handler
import sqlalchemy

engine = sqlalchemy.create_engine('mysql://root:123@127.0.0.1:3306/trucks_geolocation', pool_recycle=3600, echo=True)

Table_Tracks=Data_Handler.get_table_rows("trucks","table")
Table_geolocation=Data_Handler.get_table_rows("geolocation","table")

Table_Tracks.to_sql(name='tracks',con=engine,if_exists='fail',index=False)
Table_geolocation.to_sql(name='geolocation',con=engine,if_exists='fail',index=False)
