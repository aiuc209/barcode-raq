def hisobla(barcode):
    jami = 0
    for i, raqam in enumerate(barcode[:-1]):
        if i % 2 == 0:
            jami += int(raqam) * 3
        else:
            jami += int(raqam)
    qoldiq = jami % 10
    check_digit = (10 - qoldiq) % 10
    return barcode[:-1] + str(check_digit)

def yangila(barcode_roxyat):
    yangi_roxyat = []
    for barcode in barcode_roxyat:
        yangi_barcode = hisobla(barcode)
        yangi_roxyat.append(yangi_barcode)
    return yangi_roxyat

barcode_roxyat = ["1234567890", "2345678901", "3456789012"]
yangi_roxyat = yangila(barcode_roxyat)
print(yangi_roxyat)
