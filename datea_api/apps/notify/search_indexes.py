from haystack import indexes
from models import ActivityLog

class ActvityLogIndex(indexes.SearchIndex, indexes.Indexable):
    
    text = indexes.CharField(document=True, use_template=True, template_name="search/indexes/notify/activitylog_index.txt")
    obj_id = indexes.IntegerField(model_attr='pk')

    created = indexes.DateTimeField(model_attr='created')
    actor = indexes.CharField()
    actor_id = indexes.IntegerField()
    action_key = indexes.CharField(model_attr="action_key")
    action_id = indexes.IntegerField()
    action_type = indexes.CharField()

    target_user = indexes.CharField(null=True)
    target_user_id = indexes.IntegerField(null=True)
    target_key = indexes.CharField(model_attr="target_key", null=True)
    target_id = indexes.IntegerField(null=True)
    target_type = indexes.CharField(null=True)

    follow_keys = indexes.MultiValueField()

    tags = indexes.MultiValueField()

    def get_model(self):
        return ActivityLog
    
    def index_queryset(self, using=None):
        return self.get_model().objects.all()

    def prepare_actor(self, obj):
        return obj.actor.username

    def prepare_actor_id(self, obj):
        return obj.actor.pk

    def prepare_action_id(self, obj):
        return obj.action_object.pk

    def prepare_action_type(self, obj):
        return obj.action_object._meta.model_name

    def prepare_target_user(self, obj):
        if obj.target_user:
            return obj.target_user.username
        return None

    def prepare_target_user_id(self, obj):
        if obj.target_user:
            return obj.target_user.pk
        return None

    def prepare_target_id(self, obj):
        if obj.target_object:
            return obj.target_object.pk
        return None

    def prepare_target_type(self, obj):
        if obj.target_object:
            return obj.target_object._meta.model_name
        return None

    def prepare_tags(self, obj):
        return [tag.tag for tag in obj.tags.all()]

    def prepare_follow_keys(self, obj):
        keys = ['tag.'+str(tag.pk) for tag in obj.tags.all()]
        if obj.target_key is not None:
            keys.append(str(obj.target_key))
        return keys


