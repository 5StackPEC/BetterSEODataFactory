import json
import subprocess
from utils import web


def run_lighthouse(url):
    site_name = web.get_site_name(url)
    print(f"{site_name}: Running Lighthouse")
    cmd = f"npx lighthouse {url} --output=json --quiet"
    result = subprocess.run(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    error_message_preffix = f"Error running Lighthouse command for {url}:"
    if result.returncode != 0:
        # TODO: Append to failed urls new dataset for a second try
        if result.returncode == None:
            print(f"{error_message_preffix} no error code was generated")
        else:
            print(f"{error_message_preffix} {result.stderr.decode()}")
        return None
    else:
        try:
            print(f"{site_name}: Lighthouse completed")
            return json.loads(result.stdout)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON for {url}: {e}")
            return None
