from dal.agent_dal import Dal_agent
from menu import Menu


class Manager:
    def __init__(self):
        self.dal_agent = Dal_agent()

    def run(self):
        running = True
        while running:
            Menu.show_menu()
            choice = input()
            if choice == "1":
                self.dal_agent.insert_agent(Menu.get_details_new_agent())
            elif choice == "2":
                Dal_agent.print_agents_list(self.dal_agent.retrieve_all_agents())
            elif choice == "3":
                agent = self.dal_agent.get_agent_by_id(Menu.ask_for_id())
                print(agent or "there is no person with this id\n")
            elif choice == "4":
                self.dal_agent.delete_agent_by_id(Menu.ask_for_id())
            elif choice == "5":
                self.dal_agent.update_status(Menu.ask_for_id(), Menu.ask_for_status())
            elif choice == "1000":
                print("have a good day")
                running = False
            else:
                print("invalid input")
