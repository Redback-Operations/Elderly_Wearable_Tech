#import the required modules
import datetime  #for timestamp functionality
import random    #to generate random IP addresses
import csv       #for CSV export functionality

#generate a random IP address in the 192.168.1.x range
def generate_ip():
    return f"192.168.1.{random.randint(2, 254)}"

#return current UTC timestamp in ISO 8601 format
def current_timestamp():
    return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

#list of valid usernames
valid_users = ["user_102", "user_877", "user_324", "user_3424", "admin342"]

#list to store user activity logs
activity_logs = []

#dictionary to track the number of chat messages per user (for spam detection)
chat_tracker = {}

#list of allowed file extensions for uploads
safe_extensions = [".png", ".jpg", ".jpeg", ".pdf", ".txt"]

#start the main application loop
while True:
    #prompt the user to log in
    print ("(valid usernames are: user_102, user_877, user_324, user_3424, admin342):")
    username = input("Enter username: ")
    password = input("Enter password (any password will work): ")
    ip = generate_ip()  #generate a simulated IP address for the session

    #handle invalid username attempts
    if username not in valid_users:
        print("Invalid username. Please try again.")
        activity_logs.append({
            "timestamp": current_timestamp(),
            "user_id": username,
            "event": "login_attempt",
            "status": "failed",
            "reason": "Invalid username",
            "ip_address": ip
        })
        continue  #restart login loop

    #admin user functionality: view or export activity logs
    if username == "admin342":
        view_logs = input("Would you like to see the logs? (yes/no)").lower()
        if view_logs == "yes":
            #display all stored logs
            print("\n--- Activity Logs ---")
            for log in activity_logs:
                print(log)
            print("--- End of Logs ---\n")

            #offer option to export logs to CSV
            export = input("Would you like to export logs to a CSV file? (yes/no): ").lower()
            if export == "yes":
                #collect all unique keys used across all log entries
                all_keys = set()
                for entry in activity_logs:
                    all_keys.update(entry.keys())
                all_keys = sorted(all_keys)  #sort for consistent CSV headers

                #create a filename using current timestamp
                csv_filename = f"activity_logs_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
                #write logs to CSV
                with open(csv_filename, mode="w", newline="") as file:
                    writer = csv.DictWriter(file, fieldnames=all_keys)
                    writer.writeheader()
                    for entry in activity_logs:
                        #ensure all keys exist in the row (fill missing with empty string)
                        complete_entry = {key: entry.get(key, "") for key in all_keys}
                        writer.writerow(complete_entry)
                print(f"Logs exported to {csv_filename}")
        continue  #go back to login after admin actions

    #log successful user login
    print(f"Welcome, {username}!")
    activity_logs.append({
        "timestamp": current_timestamp(),
        "user_id": username,
        "event": "login_attempt",
        "status": "success",
        "ip_address": ip
    })

    #begin user session actions
    while True:
        print("\nWhat would you like to do?")
        print("(1) Upload a file or document")
        print("(2) Send a chat message")
        choice = input("Enter 1 or 2: ")

        if choice == "1":
            #handle file upload
            filename = input("What is the filename?: ")
            extension = input(f"What is the extension? (include the dot, allowed: {', '.join(safe_extensions)}): ")
            full_file = filename + extension

            #check file extension safety
            if extension.lower() not in safe_extensions:
                print(f"{full_file} denied due to unsafe file type.")
                activity_logs.append({
                    "timestamp": current_timestamp(),
                    "user_id": username,
                    "event": "file_upload",
                    "filename": full_file,
                    "status": "denied",
                    "reason": "Unsafe file type",
                    "ip_address": ip
                })
            else:
                print(f"{full_file} accepted and uploaded.")
                activity_logs.append({
                    "timestamp": current_timestamp(),
                    "user_id": username,
                    "event": "file_upload",
                    "filename": full_file,
                    "status": "accepted",
                    "ip_address": ip
                })

        elif choice == "2":
            #handle chat messages with spam detection
            if username not in chat_tracker:
                chat_tracker[username] = 0  #initialize count

            print("You may send up to 5 messages. Sending too many will result in a spam flag.")
            for i in range(5):
                msg = input("Enter chat message: ")
                chat_tracker[username] += 1
                activity_logs.append({
                    "timestamp": current_timestamp(),
                    "user_id": username,
                    "event": "chat_message",
                    "message": msg,
                    "status": "received",
                    "ip_address": ip
                })

                #if user exceeds 5 messages, flag them for spamming and log out
                if chat_tracker[username] >= 5:
                    print("Too many messages sent. You are flagged for spamming and will be logged out.")
                    activity_logs.append({
                        "timestamp": current_timestamp(),
                        "user_id": username,
                        "event": "chat_abuse",
                        "status": "spamming_detected",
                        "ip_address": ip
                    })
                    break
            break  #end session after chat

        #ask user if they want to perform another action or log out
        print("Type 'yes' to continue or 'no' to return to login")
        back = input("Would you like to go back to options?: ").lower()
        if back == "no":
            break  #return to login loop
