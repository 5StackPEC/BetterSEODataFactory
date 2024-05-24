import json
import subprocess

def run_lighthouse(url):
    cmd = f"lighthouse {url} --output=json --quiet"
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if result.returncode != 0:
        print(f"Error running Lighthouse command for {url}: {result.stderr.decode()}")
        return None
    else:
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for {url}: {e}")
            return None
