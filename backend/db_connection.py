import pymysql


mydatabase = pymysql.connect(
  host="localhost",
  port=3306 ,
  user="root",
  password="",
  database="post_office"
)

mycursor = mydatabase.cursor()

def verifyPackageStatus(tracking_number):

    query = 'SELECT status FROM packages WHERE tracking_number=%s'
    #qr = "INSERT INTO packages (tracking_number, status) VALUES ('112233', 'Here');"
    #mycursor.execute(qr)

    mycursor.execute(query, (tracking_number,))
    result = mycursor.fetchone()
    if result:
        print("---------------------------")
        return result[0]  # Assuming 'status' is the first column in the result
    return "not found"
