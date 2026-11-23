"""
PromptShield Local Server Launcher.
Starts a lightweight local HTTP server and opens the React Security Dashboard.
"""
import http.server
import socketserver
import webbrowser
from pathlib import Path
import os
import sys

# Project Root is the parent of the 'code' folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent
PORT = 8501

class DashboardHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(PROJECT_ROOT), **kwargs)

    def do_GET(self):
        # Automatically redirect root '/' to '/dashboard.html'
        if self.path == "/" or self.path == "":
            self.path = "/dashboard.html"
        return super().do_GET()

    def log_message(self, format, *args):
        # Clean terminal logging
        sys.stderr.write(f"[PromptShield Server] {args[0]} - {args[1]}\n")

def run_server():
    os.chdir(PROJECT_ROOT)
    url = f"http://localhost:{PORT}/dashboard.html"
    print(f"\n" + "="*70)
    print(f"  PROMPTSHIELD CYBERSECURITY DASHBOARD (REACT)")
    print(f"="*70)
    print(f"  Local Dashboard URL: {url}")
    print(f"  Serving directory  : {PROJECT_ROOT}")
    print(f"  Press Ctrl+C to stop the dashboard server.")
    print(f"="*70 + "\n")

    try:
        webbrowser.open(url)
    except Exception:
        pass

    with socketserver.TCPServer(("", PORT), DashboardHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Dashboard server stopped.")

if __name__ == "__main__":
    run_server()
