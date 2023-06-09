from django.db import models

# Create your models here.


class ChainDate(models.Model):
    baseFeePerGas = models.CharField(max_length=250)
    difficulty = models.CharField(max_length=250)
    extraData = models.CharField(max_length=250)
    gasLimit = models.CharField(max_length=250)
    gasUsed = models.CharField(max_length=250)
    hash = models.CharField(max_length=250)
    logsBloom = models.TextField(max_length=250)
    miner = models.CharField(max_length=250)
    mixHash = models.CharField(max_length=250)
    nonce = models.CharField(max_length=250)
    number = models.IntegerField()
    parentHash = models.CharField(max_length=250)
    receiptsRoot = models.CharField(max_length=250)
    sha3Uncles = models.CharField(max_length=250)
    size = models.CharField(max_length=250)
    stateRoot = models.CharField(max_length=250)
    timestamp = models.CharField(max_length=250)
    totalDifficulty = models.CharField(max_length=250)
    transactions = models.TextField(max_length=250)
    transactionsRoot = models.CharField(max_length=250)
    uncles = models.CharField(max_length=250)


class TransferDate(models.Model):
    blockHash = models.CharField(max_length=250)
    blockNumber = models.IntegerField()
    contractAddress = models.CharField(max_length=250, null=True)
    cumulativeGasUsed = models.CharField(max_length=250)
    effectiveGasPrice = models.CharField(max_length=250)
    From = models.CharField(max_length=250)
    gasUsed = models.CharField(max_length=250)
    logs = models.CharField(max_length=250)
    logsBloom = models.TextField(max_length=250)
    status = models.CharField(max_length=250)
    to = models.CharField(max_length=250)
    transactionHash = models.CharField(max_length=250)
    transactionIndex = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    value = models.CharField(max_length=250)
    timestamp = models.CharField(max_length=250)

