def tamanho_lista(a):
    return len(a) if a else 0

def tamanho_lista__(a):
    x = 0
    for i in a:
        x =+ i
        
    return x

def maior_numero(a):
    return max(a) if a else 0

def maior_numero__(a):
    if len(a) > 0:
        x = a[0]
        for i in a:
            if i > x:
                x = i
        
        return x
    else:
        return 0