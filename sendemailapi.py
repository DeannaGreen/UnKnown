import requests
def send_simple_message(emailto, emailtext):
    return requests.post(
        "https://api.mailgun.net/v3/sandbox7be174d6fe3b464fbad278bc97bd7c28.mailgun.org/messages",
        auth=("api", "220b0a312b06175524292b3157a79404-8889127d-dbaabf56"),
        data={"from": "deanna@16vmini.co.uk",
              "to": [emailto],
              "subject": "Hello",
              "text": emailtext})
