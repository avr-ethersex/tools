import mysql.connector
import sys
config = {
    'host': '10.100.0.13',
    'user': 'rasp',
    'password': 'pi',
    'database': 'test',
}

def insert_temperature( sensor_id,temp_value ):
        try:
                cnx = mysql.connector.connect(**config)
        except:
                print ("DB error")
        else:
                cursor = cnx.cursor()
                data_insert = {
                        'sensor_id': sensor_id,
                        'temp': temp_value,
                }

                query_insert_temperature = (
                        "INSERT INTO temperature (sensor_id,temp) "
                        "VALUES (%(sensor_id)s,%(temp)s)")

                cursor.execute(query_insert_temperature,data_insert)
                cnx.commit()
                cursor.close()
                cnx.close()
