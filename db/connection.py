def db_connect():
    import mysql.connector
    connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='8072',
            database='clinica_nutricional'
        )
    
    if connection:
        return connection