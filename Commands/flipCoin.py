from random import randint
import Functions.message as ms										    ## Own module

def flipCoinAnswer():
    coin = randint(1, 6000)
    print(coin)
    if coin < 3000:
        return ms.flipHead
    elif coin > 3000:
        return ms.flipTail
    return ms.flipEdge
