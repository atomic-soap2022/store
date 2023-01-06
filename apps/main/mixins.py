from django.db import models

class MetaTagMixin (models.Model):
    name = None
    meta_title = models.CharField(verbose_name='Meta Title', max_length=255, null=True, blank=True)
    meta_description = models.CharField(verbose_name='Meta Desxription', max_length=255, null=True, blank=True)
    keyword = models.CharField(verbose_name='Meta Keyword', max_length=255, null=True, blank=True)

    def get_meta_title(self):
        if self.meta_title:
            return self.meta_title
        return self.name
    class Meta:
        abstract = True

