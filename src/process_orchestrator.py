import subprocess


class ProcessOrchestrator:
    """
    This class is responsible for orchestrating the processes of the configuration, simulation and web view windows
    """

    def __init__(self):
        # Execute the configuration process
        self.configuration_process()
        self.execute_web_views()
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
        # Start the web view process as a separate process
        subprocess.Popen(["python", "src/webview/main.py"])

    def execute_simulation(self):
        """
        This method starts the simulation process.
        """
        # Start the simulation process as a separate process
        subprocess.Popen(["python", "src/simulation/main.py"])
