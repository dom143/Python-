a=[]
x=0
while True :
    print('____________________\n\n ร้านรองเท้าของดอมดอม\n____________________\n')
    print('1) Nike[n]\n2) Adidas[a]\n3) Show Pay[s]\n4) Exit[x]')
    brand=(input(" -> Select Brand : "))
    brand=brand.lower()
    while brand=='n':
        print("\n*********** Nike ***********\n\n   1) Nike Epic React\n   2) Nike Zoom fly 3\n   3) Nike Zoom Pegasus\n   4) Back")
        gen=(input(" -> Select Generation : "))
        gen=gen.lower()
        if gen=='1' :
            ne=('Nike Epic React:4990:-998:3992')
            a.append(ne)
            x+=3992
        elif gen=='2' :
            nz1=('Nike Zoom fly:3990:-798:3192')
            a.append(nz1)
            x+=3192
        elif gen=='3' :
            nz2=('Nike Zoom Pegasus:3590:-1077:2513')
            a.append(nz2)
            x+=2513
        elif gen=='4' :
            break
    while brand=='a':
        print("\n*********** Adidas ***********\n\n   1) Adidas Pusha T Ozweego\n   2) Adidas Ozweego 3\n   3) Adidas Sleek\n   4) Back")
        gena=(input(" -> Select Generation : "))
        gena=gena.lower()
        if gena=='1' :
            apt=('Adidas Pusha T Ozweego:5390:-1617:3773')
            a.append(apt)
            x+=3773
        elif gena=='2' :
            ao=('Adidas Ozweego:4300:-1290:3010')
            a.append(ao)
            x+=3010
        elif gena=='3' :
            asl=('Adidas Sleek:3590:-1077:2513')
            a.append(asl)
            x+=2513
        elif gena=='4' :
            break
    if brand=='s' :
        print('{0:-<80}'.format(""))
        print('{0:' '<35}{1:' '<20}{2:' '<20}{3:' '<20}'.format('รุ่น','ราคา','ส่วนลด','จ่ายจริง'))
        print('{0:-<80}'.format(""))
        for d in a :
            e=d.split(':')
            print('{0[0]:<32}{0[1]:<20}{0[2]:<20}{0[3]:<20}'.format(e))
        print('{0:-<80}'.format(""))
        print("รวมเป็นเงิน                                                               %d"%x)
        print('{0:-<80}'.format(""))
        break
    if brand=='x':
        break
    else :
        print("-----Error-----")
