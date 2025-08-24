from miru_server_sdk import Miru


def main() -> None:
    client = Miru(
        api_key="sk_4eCajhxMSnScF2YuaTZvoSxdmDtQWpVEjXDZYsiKTzh1U5tiRsiuma1cDJHQUQRVAKKnQniHsFPKcdVbSvukdHs5_1630c6",
    )

    event = client.webhooks.unwrap(
        payload="",
    )

    print(event.to_json())


if __name__ == "__main__":
    main()
