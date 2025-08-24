# # standard library imports
# import os

# # third party imports
# from dotenv import load_dotenv

# from miru_server_sdk import Miru
# from miru_server_sdk.webhooks import Webhook, WebhookVerificationError

# # set the MIRU_API_KEY environment variable in your '.env' file
# # place this file in the /examples directory
# load_dotenv()


# def main() -> None:
#     if not os.getenv("MIRU_API_KEY"):
#         raise ValueError("MIRU_API_KEY is not set")
#     api_key = os.getenv("MIRU_API_KEY")
    
#     if not os.getenv("MIRU_WEBHOOK_SECRET"):
#         raise ValueError("MIRU_WEBHOOK_SECRET is not set")
#     webhook_secret = os.getenv("MIRU_WEBHOOK_SECRET")

#     payload = request.get_data()

#     wh = Webhook(SECRET)
#     webhookPayload = wh.verify(payload, headers)

#     # TODO: check if the webhook payload is valid
#     print(webhookPayload)


#     client = Miru(api_key=api_key)

#     event = client.webhooks.unwrap(
#         payload="",
#     )

#     print(event.to_json())


# if __name__ == "__main__":
#     main()
