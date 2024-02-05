from django.core.mail import send_mail


class TestMailhog:
    def test_mail_sent(self, client, faker):
        email_sent = send_mail(
            "Subject here",
            "Here is the message.",
            "from@example.com",
            ["to@example.com"],
            fail_silently=False,
        )
        assert email_sent == 1
