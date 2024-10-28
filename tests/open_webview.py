import webview


# This script is responsible for launching the webview
def open_webview():
    webview.create_window("Webview", "http://192.168.1.126")
    webview.start()


if __name__ == "__main__":
    open_webview()
