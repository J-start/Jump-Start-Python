from dataBase.updateDatas import *
from teste.testsMain import *
import sys
import time

def progress_bar(progress):
    bar_length = 50
    block = int(round(bar_length * progress))
    text = "\rProgresso: [{0}] {1:.2f}%".format("#" * block + "-" * (bar_length - block), progress * 100)
    sys.stdout.write(text)
    sys.stdout.flush()

index =0
passed = 0
progress_bar(index)

if shouldInsertOneDataSelic():
    passed+=1

index=0.25
progress_bar(index)

if shouldInsertOneDataAcoes():
    passed+=1

index=0.5
progress_bar(index)

if shouldInsertOneDataCoins():
    passed+=1

index=0.75
progress_bar(index)

if shouldInsertOneDataCrypto():
    passed+=1

index=1
progress_bar(index)

print("\nTestes finalizados")
print(f"Resumo : Testes passados: {passed}/4")


