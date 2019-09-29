import random
import string
import base64

from django.core.signing import Signer

ALPHABET = string.printable * 70

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    signer = Signer()

    email_verification_link = models.CharField(
        null=True,
        max_length=1024
    )
    is_email_verified = models.BooleanField(default=False)
    verification_email_sent_at = models.DateTimeField(null=True)
    incorrect_attempts = models.PositiveSmallIntegerField(default=0)
    is_seller = models.BooleanField(default=False)
    initial_secret_key = models.CharField(max_length=256)

    def generate_key(self):
        key = "".join(
            random.sample(ALPHABET, 256)
        )
        self.initial_secret_key = key
        self.save()

        signed_key = self.signer.sign(key)
        print(signed_key)
        return str(base64.b64encode(bytes(signed_key, encoding='ascii')))

    def verify_email(self):
        encoded_key = self.generate_key()
        url = "http://127.0.0.1:8000/verify?key={}".format(
            encoded_key[2:-1]
        )
        self.email_user(
            "Verification Link",
            url,
            "admin@cars.com"
        )

    def check_key(self, key):
        signed_key = str(base64.b64decode(key))
        print(signed_key)
        initial_key = self.signer.unsign(signed_key)
        return self.initial_secret_key == initial_key
