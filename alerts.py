def create_alert(message):

    with open("alerts.log","a") as f:

        f.write(message + "\n")

    print("ALERT:", message)