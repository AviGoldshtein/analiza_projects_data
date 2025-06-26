from models.agent import Agent


class Menu:
    @staticmethod
    def show_menu():
        print("1. to insert a new agent to DB\n"
              "2. to show all agents\n"
              "3. to get details for an agent by his id\n"
              "4. to delete an agent by his id\n"
              "5. to change the status for an agent\n"
              "1000. to exit the program\n")

    @staticmethod
    def get_details_new_agent():
        code_name = input("Enter the code name")
        real_name = input("Enter the real name")
        location = input("Enter the location")
        status = input("Enter the status")
        if code_name and real_name and location and status:
            return Agent(code_name, real_name, location, status)
        else:
            print("something is missing")
            return Menu.get_details_new_agent()

    @staticmethod
    def ask_for_id():
        id = input("enter the number id")
        if id.isnumeric():
            return id
        else:
            print("this is not a number")
            return Menu.ask_for_id()

    @staticmethod
    def ask_for_status():
        choice = input("1. living\n"
              "2. ded\n"
              "3. hospital\n"
              "4. unknown\n")
        if choice == "1":
            return "living"
        if choice == "2":
            return "ded"
        if choice == "3":
            return "hospital"
        if choice == "4":
            return "unknown"
        else:
            print("invalid choice")
            return Menu.ask_for_status()
