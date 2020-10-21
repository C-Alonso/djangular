from rest_framework import serializers

from .models import Section, Instrument


class InstrumentSerializer(serializers.ModelSerializer):
    """Serializer for Instrument objects"""

    #section = serializers.PrimaryKeyRelatedField(many=False, read_only=True, allow_null=True)
    section = serializers.SlugRelatedField(
        many=False,
        read_only=False,
        slug_field='name',
        queryset=Section.objects.all(),
        required=False
    )

    class Meta:
        model = Instrument
        fields = ('id', 'name', 'section', 'invention_date', 'image')
        raad_only_fields = ('id',)  # So it can't be updated by the user.
    
    def to_representation(self, instance):
        self.fields['section'] = serializers.StringRelatedField(read_only=True, source='section.name')
        return super(InstrumentSerializer, self).to_representation(instance)
    

class SectionSerializer(serializers.ModelSerializer):
    """Serializer for Section objects"""

    instruments = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        slug_field='name',
        queryset=Instrument.objects.all(),
        required=False
    )

    url = serializers.SerializerMethodField() # define a SerializerMethodField        

    def get_url(self, obj):
        return obj.get_absolute_url() # return the absolute url of the object

    class Meta:
        model = Section
        fields = ('id', 'name', 'instruments', 'url')
        raad_only_fields = ('id')


    
