import sys
import clipboard
import json
import encrypt_decrypt as ed

SAVED_DATA = "clipboard.json"


def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


def load_data(filepath):
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}


# ed.EncDecr(data).encrypt()

if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Enter a key: ")
        # data[key] = clipboard.paste()

        # encrypting the data:
        copied_data = clipboard.paste()
        cl = ed.EncDecr(copied_data)
        encr_message = cl.encrypt()
        data[key] = encr_message.decode('utf8')

        save_data(SAVED_DATA, data)
        print("Data saved!")
    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            # clipboard.copy(data[key])

            # decrypting the data:
            cl = ed.EncDecr(data[key])
            decr_message = cl.decrypt()
            clipboard.copy(decr_message)
            print("Data copied to clipboard.")
        else:
            print("Key does not exist.")
    elif command == "list":
        print(data)
    else:
        print("Unknown command")
else:
    print("Please pass one command!")



