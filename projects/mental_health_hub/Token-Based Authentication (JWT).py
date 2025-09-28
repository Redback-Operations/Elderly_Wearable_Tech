from flask import Flask, request, jsonify #web framework to create routes like /login, /register
import bcrypt #hashes the passwords
import jwt #creates and verifies token
import datetime #helps set token expiry times

app = Flask(__name__) #creates the flask app
app.config['SECRET_KEY'] = "super-secret-key"  #



users_db = {} #testing database



def hash_password(password: str) -> bytes:
    """Securely hash a plaintext password using bcrypt."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password: str, hashed: bytes) -> bool:
    """Verify that a given plaintext password matches the stored bcrypt hash."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed)
    


def generate_token(username: str) -> str:
    #create the payload
    payload = {
        'user': username, #store the username
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)  #set expiration time (30 minutes)
    }
    #encode the password into a JWT token, signed with the secret key
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")
    return token

def verify_token(token: str):
    try:
        #decode the token and check the signature and expiry
        payload = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        # If token is invalid or expired, return None
        return None  
    except jwt.InvalidTokenError:
        return None  


#user registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users_db:
        return jsonify({"error": "User already exists"}), 400

    #save the user with a hashed password
    hashed_pw = hash_password(password)
    users_db[username] = hashed_pw

    return jsonify({"message": f"User {username} registered successfully"}), 201

#user login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

#check if user exists
    if username not in users_db:
        return jsonify({"error": "Invalid credentials"}), 401

     #check if password matches the hashed one
    stored_pw = users_db[username]
    if not verify_password(password, stored_pw):
        return jsonify({"error": "Invalid credentials"}), 401

    #if password is correct then generate token
    token = generate_token(username)
    return jsonify({"message": f"Welcome, {username}!", "token": token}), 200

@app.route('/protected', methods=['GET'])
def protected():
      #read the authorization" header (format: Bearer <token>)
    auth_header = request.headers.get("Authorization")
#if no header or wrong format then deny access
    if not auth_header or not auth_header.startswith("Bearer "):
        return jsonify({"error": "Missing or invalid token"}), 401
  #extract the token
    token = auth_header.split(" ")[1]
    payload = verify_token(token)
  #if token is invalid/expired then deny access
    if not payload:
        return jsonify({"error": "Invalid or expired token"}), 401
# if token is valid then user gets access

    username = payload["user"]
    return jsonify({"message": f"Hello {username}, you accessed a protected route!"})

@app.route('/logout', methods=['POST'])
def logout():
     
    #logout is just deleting the token from the client side
    
    return jsonify({"message": "Logout by deleting token on client-side"}), 200


if __name__ == "__main__":
    app.run(debug=True)
