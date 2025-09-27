import requests
import sys
import json
from pathlib import Path
from yaspin import yaspin

BASE_SERVER_URL = "http://localhost:8000"

def handle_error(error, name="API Call fail"):
    print(f"\n[ERROR] {name}: {error}")
    sys.exit(1)


def uploading_file_compile(flags):
    with yaspin(text="Uploading file and processing...", color="yellow") as spinner:
        try:
            file_path = Path(flags.get("compile"))
            if not file_path.exists():
                handle_error("File not found")

            files = {"file": (file_path.name, open(file_path, "rb"))}
            data = {}

            if flags.get("outputFile"):
                data["outputName"] = flags["outputFile"]

            if flags.get("args"):
                data["args"] = json.dumps(flags["args"])

            response = requests.post(f"{BASE_SERVER_URL}/compile", files=files, data=data)

            if response.status_code != 200:
                handle_error(response.text)

            resp_data = response.json()
            download_url = f"{BASE_SERVER_URL}{resp_data['download']}"
            output_file = resp_data["download"].replace("/download/", "")

            download = requests.get(download_url, stream=True)
            with open(output_file, "wb") as f:
                for chunk in download.iter_content(1024):
                    f.write(chunk)

            spinner.ok("✅")
            print(f"Compiled file: {output_file}")

        except Exception as e:
            spinner.fail("💥")
            handle_error(e)


def uploading_file_interprate(flags, cli=None):
    cli = cli or {}
    with yaspin(text="Uploading file and processing...", color="yellow") as spinner:
        try:
            file_path = Path(flags.get("interpreted"))
            if not file_path.exists():
                handle_error("File not found")

            files = {"file": (file_path.name, open(file_path, "rb"))}
            data = {}

            if flags.get("outputFile"):
                data["outputName"] = flags["outputFile"]

            if flags.get("args"):
                args_val = flags["args"]
                if cli.get("input") and cli.get("flags", {}).get("args"):
                    args_val += " " + " ".join(cli["input"])
                data["args"] = json.dumps(str(args_val))

            response = requests.post(f"{BASE_SERVER_URL}/interprate", files=files, data=data)

            if response.status_code != 200:
                handle_error(response.text)

            resp_data = response.json()
            spinner.ok("✅")
            print(f"\n---\n{resp_data['output']}---")

        except Exception as e:
            spinner.fail("💥")
            handle_error(e)
