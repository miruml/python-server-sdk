import os

from dotenv import load_dotenv

from miru_server_sdk import Miru

# set the MIRU_API_KEY environment variable in your '.env' file
# place this file in the /examples directory
load_dotenv()


def main() -> None:
    if not os.getenv("MIRU_API_KEY"):
        raise ValueError("MIRU_API_KEY is not set")

    client = Miru(api_key=os.getenv("MIRU_API_KEY"))

    device = client.devices.retrieve(
        device_id="dvc_MoU7XtRE4U5GuDAEHdTfyfXfswkjydioc"
    )
    print(device.to_json())


if __name__ == "__main__":
    main()
