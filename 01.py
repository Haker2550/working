import webbrowser
# This script opens a web browser to a specified URL based on user input
    # Open a web browser to the specified URL
print("HI!")
def start():
        print("Use number")
        print("1 - Google")
        print("2 - Ping")
        usr1 = str(input("number: "))
        if usr1.lower() == "1":
                url = "https://www.google.com"
                webbrowser.open_new_tab(url)
                print("opening google")
        elif usr1.lower() == "2":
                url = "https://ping.ru"
                webbrowser.open_new_tab(url)
                print("opening ping")
        else:
                print("Invalid input")