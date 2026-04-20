# Domain Checker
*Simple python script to check if a domain is available*
## Adding a Domain

Create a Json file in the following format:
```python

{
        "domains": [
                "domain_one.de",
                "domain_two.com",
        ]
}

```

## Messaging
[Twilio](https://console.twilio.com/us1/develop/sms/try-it-out/whatsapp-learn?frameUrl=%2Fconsole%2Fsms%2Fwhatsapp%2Flearn%3Fx-target-region%3Dus1) is used to send a Whatsapp Message to your phone.

The .env has to have the following values set
```bash
USER_SID=
AUTH_TOKEN=
WHATSAPP_FROM=
WHATSAPP_TO=

```
