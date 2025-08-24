# standard library imports
import os

# third party imports
from miru_server_sdk import Miru


def main() -> None:
    client = Miru(api_key=os.getenv("MIRU_API_KEY"))

    device = client.devices.retrieve(
        device_id="dvc_MoU7XtRE4U5GuDAEHdTfyfXfswkjydioc"
    )
    print(device.to_json())


if __name__ == "__main__":
    main()
