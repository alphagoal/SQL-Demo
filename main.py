from flask import Flask, request
import psycopg2

app = Flask(__name__) #flask object

@app.route("/view_profile/<user_id>")
def hello_world(user_id):
    # establishing the connection
    conn = psycopg2.connect(
        database="crs", user='postgres', password='master12345',
        host='database-1.cfoquoki6zm5.ap-northeast-1.rds.amazonaws.com',
        port='5432'
    )
    # Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # Executing an MYSQL function using the execute() method
    cursor.execute(f"SELECT id,name,phone FROM customer WHERE id ={user_id}")

    # Fetch a single row using fetchone() method.
    data = cursor.fetchone()
    dict_data = dict(zip(['id','name','phone'],data))
    print("***** Connection established to: ", dict_data)

    # Closing the connection
    conn.close()

    return dict_data


@app.route("/login",methods=['POST'])
def login():
    user_id=request.json['user_id']
    pwd= request.json['pwd']
    return {"user_id":user_id,"pwd":pwd}


