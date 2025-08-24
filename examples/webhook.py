# standard library imports
import os

# third party imports
from miru_server_sdk import Miru


def main() -> None:
    client = Miru(api_key=os.getenv("MIRU_API_KEY"))

    event = client.webhooks.unwrap(
        payload="",
    )

    print(event.to_json())


if __name__ == "__main__":
    main()
