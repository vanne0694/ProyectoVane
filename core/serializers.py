from rest_framework import serializers
from .models import Person, Store, Client, Category, Product


class PersonSerializers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'firstname', 'lastname', 'birthday', 'height']

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.firstname = validate_data.get('firstname', instance.firstname)
        instance.lastname = validate_data.get('lastname', instance.lastname)
        instance.birthday = validate_data.get('birthday', instance.birthday)
        instance.height = validate_data.get('height', instance.height)
        instance.save()
        return instance


class StoreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'type']

    def create(self, validated_data):
        return Store.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('model', instance.model)
        instance.type = validate_data.get('firstname', instance.firstname)
        instance.save()
        return instance


class ClientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'Person', 'Store', 'type', 'member']

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.Person = validate_data.get('Person', instance.Person)
        instance.Store = validate_data.get('Store', instance.Store)
        instance.type = validate_data.get('type', instance.type)
        instance.member = validate_data.get('member', instance.bmember)
        instance.save()
        return instance


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get('name', instance.name)
        instance.save()
        return instance

    class ProductSerializers(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ['id', 'name', 'description', 'price', 'foto']

        def create(self, validated_data):
            return Product.objects.create(**validated_data)

        def update(self, instance, validate_data):
            instance.name = validate_data.get('name', instance.name)
            instance.description = validate_data.get('description', instance.description)
            instance.price = validate_data.get('price', instance.price)
            instance.foto = validate_data.get('foto', instance.foto)
            instance.save()
            return instance
