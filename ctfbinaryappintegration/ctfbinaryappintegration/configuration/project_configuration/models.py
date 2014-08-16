from django.db import models


class ObjectStore(models.Model):
    object_id = models.PositiveIntegerField(primary_key=True)
    object_title = models.CharField(max_length=255)
    class Meta:
        #give table name as appname_tablename so that it is
        #easy to find to which app this belongs to
        db_table = "configuration_objects"