from django.db import models

class TgUser(models.Model):
    chat_id = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.chat_id)

    class Meta:
        verbose_name = "Telegram user"
        verbose_name_plural = "Telegram users"