#!/usr/bin/env python3
"""Run: python3 serve.py  ->  open http://localhost:8000"""
import http.server, socketserver
class H(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a): pass
with socketserver.TCPServer(("",8000),H) as s:
    print("Veylora CyberGuard AI running at http://localhost:8000  (Ctrl+C to stop)")
    s.serve_forever()
