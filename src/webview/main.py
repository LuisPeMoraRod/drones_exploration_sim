import json
import webview


def get_servers_address():
    try:
        with open("./config/config.json", "r") as f:
            return json.load(f).get("servers_address")
    except FileNotFoundError:
        return None


def open_webviews(urls: list):
    for i in range(len(urls)):
        webview.create_window(f"Agent {i+1}", urls[i])
    webview.start()


if __name__ == "__main__":
    urls = get_servers_address()
    if urls:
        open_webviews(urls)
    else:
        print("No servers addresses found in configuration file")
