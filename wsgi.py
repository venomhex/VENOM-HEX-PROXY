import os
import subprocess

def app(environ, start_response):
    port = os.environ.get("PORT", "8080")
    # ব্যাকগ্রাউন্ডে প্রক্সি ইঞ্জিন চালু করা
    cmd = f"mitmdump -p {port} --set block_global=false"
    subprocess.Popen(cmd, shell=True)
    
    data = b"Proxy Server is Running Successfully!"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return [data]
