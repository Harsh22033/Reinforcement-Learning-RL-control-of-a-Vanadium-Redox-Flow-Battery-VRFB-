from thales_remote.connection import ThalesRemoteConnection

connection = ThalesRemoteConnection()

try:
    connection.connectToTerm("127.0.0.1") # IP address of machine
    # .connectToTerm() is to open TCP/IP socket.(Transmission Control Protocol / Internet Protocol)
    print("Connected to thales remote.")

    # disconnect just to check.
    connection.disconnectFromTerm()
    print("Disconnect")

except Exception as e:
    print("failed:", e)
