import os
import subprocess

# Render এর পোর্ট সেটআপ
port = os.environ.get("PORT", "10000")

# mitmdump সরাসরি ব্যাকগ্রাউন্ডে রান করা হচ্ছে
subprocess.Popen(["mitmdump", "-p", port, "--set", "block_global=false"])

# Render কে শান্ত রাখার জন্য একটি ডামি অ্যাপ
def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return [b"Proxy is running..."]
