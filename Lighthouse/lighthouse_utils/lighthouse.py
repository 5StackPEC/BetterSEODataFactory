import json
import subprocess


def run_lighthouse(url):
    cmd = f"npx lighthouse {url} --output=json"
    result = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    error_message_preffix = f"Error running Lighthouse command for {url}:"
    if result.returncode != 0:
        if result.returncode == None:
            print(f"{error_message_preffix} no error code was generated")
        else:
            print(f"{error_message_preffix} {result.stderr.decode()}")
        return None
    else:
        try:
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for {url}: {e}")
            return None
