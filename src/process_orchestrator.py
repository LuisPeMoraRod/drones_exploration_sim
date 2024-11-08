import subprocess
import json
from configurator.constants import CONFIG_STATUS


class ProcessOrchestrator:
    """
    This class is responsible for orchestrating the processes of the configuration, simulation and web view windows
    """

    def __init__(self):
        # Execute the configuration process
        self.configuration_process()

        # Execute simulation process if configuration is ready
        config_status = self.get_config_status()
        if config_status == CONFIG_STATUS["READY"]:
            # self.execute_web_views()
            self.execute_simulation()

    def configuration_process(self):
        """
        This method starts the configuration process and monitors it.
        """
        # Start the configuration process as a separate process
        process = subprocess.Popen(["python", "src/configurator/main.py"])

        # Wait for the process to complete
        process.wait()

    def execute_web_views(self):
        """
        This method starts the web view processes.
        """
        subprocess.Popen(["python", "src/webview/main.py"])

    def execute_simulation(self):
        """
        This method starts the simulation process.
        """
        subprocess.Popen(["python", "src/simulation/main.py"])

    def get_config_status(self):
        """
        This method returns the status of the configuration process
        """
        try:
            # Read configuration file and return the data
            with open("./config/config.json", "r") as f:
                config_data = json.load(f)
                return config_data["config_status"]
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading configuration file: {e}")
            return None
