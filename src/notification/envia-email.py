import yagmail
import os

# pegando variáveis de ambiente do GitHub Actions
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

yag = yagmail.SMTP(EMAIL_SENDER, EMAIL_PASSWORD)

yag.send(
    to=EMAIL_RECEIVER,
    subject="Status da Pipeline",
    contents="Pipeline executada! 🚀📧"
)

