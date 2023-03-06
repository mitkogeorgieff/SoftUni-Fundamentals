class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
data = input()
while data != "Stop":
    sender, receiver, content = data.split()
    email = Email(sender, receiver, content)
    emails.append(email)

    data = input()

idx_emails_to_be_send = [int(el) for el in input().split(", ")]

for idx, email in enumerate(emails):
    if idx in idx_emails_to_be_send:
        emails[idx].send()

for email in emails:
    print(email.get_info())
