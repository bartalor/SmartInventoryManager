# serializers/customer.py
from rest_framework import serializers
from inventory.models.customer import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

# serializers/transaction.py
from rest_framework import serializers
from inventory.models.transaction import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
