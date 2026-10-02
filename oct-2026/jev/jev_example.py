QUESTIONS = {
  "refund": {
    "type": "noul",
    "instructions": "Is the customer asking for money back?",
  },
  "team": {
    "type": "choice",
    "instructions": "Which team should handle this ticket?",
    "criteria": {
      "billing": "Charges, refunds",
      "technical": "Bugs, errors",
      "account": "Login, profile",
      "shipping": "Delivery, parcels",
    },
  },
  "mood": {
    "type": "score",
    "instructions": "How upset is the customer?",
    "criteria": ["calm", "slightly annoyed", "annoyed",
                 "angry", "furious"],
  },
}
import os
import requests

TICKET = ("I was charged twice for my "
          "subscription this month. I already "
          "wrote to you last week and got no "
          "answer. Please fix this now.")

r = requests.post(
  "https://openrouter.ai/api/alpha/decisions",
  headers={
    "Authorization":
      "Bearer " + os.environ["OPENROUTER_API_KEY"],
  },
  json={
    "model": "~typesafe/jev-latest",
    "state": TICKET,
    "questions": QUESTIONS,
  },
)
a = r.json()["answers"]
print(a["refund"]["noul"])   # about 0.75
print(a["team"]["choice"])   # billing
print(a["mood"]["score"])    # about 2.8
