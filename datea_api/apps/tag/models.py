from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _
import re
from datea_api.apps.api.utils import remove_accents


class Tag(models.Model):

	created = models.DateTimeField(_('created'), auto_now_add=True)

	tag = models.SlugField(_('Tag'), max_length=100, unique=True, db_index=True)
	title = models.CharField(_('Title'), max_length=100, blank=True, null=True)
	description = models.TextField(_('Description (optional)'), max_length=500, blank=True, null=True)

	follow_count = models.IntegerField(_('Follow count'), default=0, blank=True, null=True)
	dateo_count = models.IntegerField(_('Dateo count'), default=0, blank=True, null=True)
	image_count = models.IntegerField(_("Image count"), default=0)

	client_domain = models.CharField(_('CLient Domain'), max_length=100, blank=True, null=True)

	def save(self, *args, **kwargs):
		self.tag = remove_accents(re.sub("[\W_]", '', self.tag, flags=re.UNICODE))
		super(Tag, self).save(*args, **kwargs)

	class Meta:
		verbose_name = _('Tag')
		verbose_name_plural = _('Tags')

	def __unicode__(self):
		return self.tag


