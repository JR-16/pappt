
class Config:
    SECRET_KEY = 'B!1w8NAt1T^%kvhUI*S^'


# class conexiondb(Config):
#     DEBUG = True
#     MYSQL_HOST = 'localhost'
#     MYSQL_USER = 'root'
#     MYSQL_PASSWORD = ''x
#     MYSQL_DB = 'flask'

class conexiondb(Config):
    DEBUG = True
    MYSQL_HOST = 'bkv4kmrcaouedd0x5qwq-mysql.services.clever-cloud.com'
    MYSQL_USER = 'ufn8t8ef8pyic07e'
    MYSQL_PASSWORD = 'mCwv8J85za0k80Jzy4UK'
    MYSQL_DB = 'bkv4kmrcaouedd0x5qwq'



config = {
    'conexiondb': conexiondb
}
