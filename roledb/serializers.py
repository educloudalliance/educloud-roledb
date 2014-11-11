
from rest_framework import serializers
from roledb.models import User, Attribute, UserAttribute, Municipality, School, Role, Attendance, Source


class QuerySerializer(serializers.ModelSerializer):
  roles = serializers.SerializerMethodField('role_data')
  attributes = serializers.SerializerMethodField('attribute_data')

  class Meta:
    model = User
    fields = ('username','first_name','last_name','roles','attributes')

  def role_data(self, obj):
    data = []
    for a in obj.attendances.all():
      d = {}
      d['school'] = a.school.school_id
      d['group'] = a.group
      d['role'] = a.role.name
      data.append(d)
    return data

  def attribute_data(self, obj):
    data = []
    for a in obj.attributes.all():
      d = {}
      d['name'] = a.attribute.name
      d['value'] = a.value
      data.append(d)
    return data


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('id', 'username', 'first_name', 'last_name')


class AttributeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Attribute


class UserAttributeSerializer(serializers.ModelSerializer):
  data_source = serializers.PrimaryKeyRelatedField(read_only=True)

  class Meta:
    model = UserAttribute

  def save(self, *args, **kwargs):
    username = self.context['request'].user.username
    data_source_obj, _ = Source.objects.get_or_create(name=username)
    self.object.data_source = data_source_obj
    return super(UserAttributeSerializer, self).save(*args, **kwargs)


class MunicipalitySerializer(serializers.ModelSerializer):
  data_source = serializers.PrimaryKeyRelatedField(read_only=True)

  class Meta:
    model = Municipality

  def save(self, *args, **kwargs):
    username = self.context['request'].user.username
    data_source_obj, _ = Source.objects.get_or_create(name=username)
    self.object.data_source = data_source_obj
    return super(MunicipalitySerializer, self).save(*args, **kwargs)


class SchoolSerializer(serializers.ModelSerializer):
  data_source = serializers.PrimaryKeyRelatedField(read_only=True)

  class Meta:
    model = School

  def save(self, *args, **kwargs):
    username = self.context['request'].user.username
    data_source_obj, _ = Source.objects.get_or_create(name=username)
    self.object.data_source = data_source_obj
    return super(SchoolSerializer, self).save(*args, **kwargs)


class RoleSerializer(serializers.ModelSerializer):
  class Meta:
    model = Role


class AttendanceSerializer(serializers.ModelSerializer):
  data_source = serializers.PrimaryKeyRelatedField(read_only=True)

  class Meta:
    model = Attendance

  def save(self, *args, **kwargs):
    username = self.context['request'].user.username
    data_source_obj, _ = Source.objects.get_or_create(name=username)
    self.object.data_source = data_source_obj
    return super(AttendanceSerializer, self).save(*args, **kwargs)

