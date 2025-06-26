import mysql.connector
from models.agent import Agent

class Dal_agent:
    def open_connection(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="eagleEyeDB_python"
            )

            if mydb.is_connected():
                print("Connected to MySQL server")
                return mydb
            else:
                print("Connection failed")
                return None
        except mysql.connector.Error as err:
            print(f"Connection Error: {err}")
            return None

    def insert_agent(self, agent):
        mydb = self.open_connection()
        if not mydb:
            print("Insert failed: no database connection.")
            return

        try:
            cursor = mydb.cursor()
            sql = "INSERT INTO agents (codeName, realName, location, status) VALUES (%s, %s, %s, %s)"
            values = (agent.code_name, agent.real_name, agent.location, agent.status)
            cursor.execute(sql, values)
            mydb.commit()
            print(cursor.rowcount, "record inserted.")
        except mysql.connector.Error as err:
            print(f"Insert Error: {err}")
        finally:
            if cursor:
                cursor.close()
            if mydb:
                mydb.close()

    def retrieve_all_agents(self):
        mydb = self.open_connection()
        if not mydb:
            print("Retrieve failed: no database connection.")
            return []

        cursor = None
        agents = []
        try:
            cursor = mydb.cursor(dictionary=True)
            sql = "SELECT id, codeName, realName, location, status, missionsCompleted FROM agents"
            cursor.execute(sql)
            all_agents_from_db = cursor.fetchall()

            for agentDB in all_agents_from_db:
                agent = Agent(agentDB["codeName"], agentDB["realName"], agentDB["location"], agentDB["status"], agentDB["missionsCompleted"], agentDB["id"])
                agents.append(agent)

            return agents
        except mysql.connector.Error as err:
            print(f"Retrieve Error: {err}")
            return []
        finally:
            if cursor:
                cursor.close()
            if mydb:
                mydb.close()

    def get_agent_by_id(self, id):
        mydb = self.open_connection()
        if not mydb:
            print("Get_agent_by_id failed: no database connection.")
            return

        try:
            cursor = mydb.cursor(dictionary=True)
            sql = "SELECT * FROM agents WHERE id = %s"
            values = [id]
            cursor.execute(sql, values)
            agent = cursor.fetchone()
            if agent:
                return Agent(agent["codeName"], agent["realName"], agent["location"], agent["status"], agent["missionsCompleted"], agent["id"])
            else:
                return None
        except mysql.connector.Error as err:
            print(f"Get_agent_by_id Error: {err}")
        finally:
            if cursor:
                cursor.close()
            if mydb:
                mydb.close()

    def delete_agent_by_id(self, id):
        mydb = self.open_connection()
        if not mydb:
            print("delete_agent_by_id failed: no database connection.")
            return False

        cursor = None
        try:
            cursor = mydb.cursor()
            sql = "DELETE FROM agents WHERE id = %s"
            values = [id]
            cursor.execute(sql, values)
            mydb.commit()

            if cursor.rowcount == 0:
                print("No agent found with that ID.")
                return False
            else:
                print(f"Agent with ID {id} deleted.")
                return True
        except mysql.connector.Error as err:
            print(f"delete_agent_by_id Error: {err}")
            return False
        finally:
            if cursor:
                cursor.close()
            if mydb:
                mydb.close()

    def update_status(self, id, status):
        mydb = self.open_connection()
        if not mydb:
            print("update_status failed: no database connection.")
            return False

        cursor = None
        try:
            cursor = mydb.cursor()
            sql = "UPDATE agents SET status = %s WHERE id = %s"
            values = (status, id)
            cursor.execute(sql, values)
            mydb.commit()

            if cursor.rowcount == 0:
                print("No agent found with that ID.")
                return False
            else:
                print(f"Agent with ID {id} updated.")
                return True
        except mysql.connector.Error as err:
            print(f"update_status Error: {err}")
            return False
        finally:
            if cursor:
                cursor.close()
            if mydb:
                mydb.close()
    @staticmethod
    def print_agents_list(agents):
        for agent in agents:
            print(agent)