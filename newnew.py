# import time
import keyboard as ky
import random

low = list(map(chr, range(97, 123)))
trans = {44: None, 39: None, 32: None}
low = str(low).translate(trans)
base = str(low)
cap = base.upper()
rez = [low, cap]
str(rez).translate(trans)
ra = random.randint(1, 26)
ra1 = random.randint(1, 26)
k = 0
j = 100
for i in range(j):
    ra = random.randint(1, 26)
    ra1 = random.randint(1, 26)
    ky.block_key(rez[0][ra])
    ky.block_key(rez[1][ra1])
inva = ["\u0250",
        "\u0252",
        "\u00E1",
        "\u0252",
        "\u1D43",
        "\u0103",
        "\u1FB7",
        "\u2090",
        "\u0101",
        "\u1F07",
        "\u2C65",
        "\uA73B"]

invb = ["\u0535",
        "\u0411",
        "\u2C13",
        "\u10EE",
        "\u0184",
        "\u03E6",
        "\u07D5",
        "\u1472",
        "\u159A",
        "\u1D47",
        "\uA64F"]

invc = ["\u0109",
        "\u0109",
        "\u023C",
        "\u1004",
        "\u0188",
        "\u0254",
        "\u03F2",
        "\u1466",
        "\u1004",
        "\u00A2",
        "\u0107",
        "\u010B"]

invd = ["\u1470",
        "\u056A",
        "\u010F",
        "\u018C",
        "\u0257",
        "\u0503",
        "\u0501",
        "\u0500",
        "\u1470",
        "\u1D48",
        "\u1E0B"]

inve = ["\u00E8",
        "\u0117",
        "\u0205",
        "\u0247",
        "\u0258",
        "\u04D7",
        "\u03F5",
        "\u0435",
        "\u0451",
        "\u011B",
        "\u0CEC",
        "\u01DD"]

invf = ["\u0192",
        "\u0284",
        "\u16AA",
        "\u1E1F",
        "\u24D5",
        "\u017F",
        "\u0493",
        "\u04FB",
        "\u16A8",
        "\u16A9",
        "\u16AB"]

invg = ["\u011D",
        "\u011F",
        "\u0121",
        "\u01E5",
        "\u1045",
        "\u0E87",
        "\u1CA7",
        "\u1E21",
        "\u0123",
        "\u01F5",
        "\u01E7",
        "\u0AED"]

invh = ["\u0127",
        "\u021F",
        "\u0266",
        "\u0267",
        "\u13F2",
        "\u16B3",
        "\u1E25",
        "\u1E2B",
        "\u2C68",
        "\u2D19",
        "\u045B"]
invi = ["\u0129",
        "\u0209",
        "\u0268",
        "\u03CA",
        "\u0456",
        "\u0457",
        "\u0671",
        "\u0773",
        "\u0F0F",
        "\u1EC9",
        "\u13A5",
        "\u1E2D"]

invj = ["\u148D",
        "\u06B5",
        "\u029D",
        "\u029D",
        "\u0458",
        "\u0249",
        "\u025F",
        "\u0135",
        "\u0248",
        "\u02B2",
        "\u03F3"]

invk = ["\u0137",
        "\u0199",
        "\u01E9",
        "\u029E",
        "\u03BA",
        "\u043A",
        "\u045C",
        "\u049B",
        "\u049D",
        "\u049F",
        "\u1D4F",
        "\u1D84"]

invl = ["\u1DAB",
        "\u03B9",
        "\u14AA",
        "\u14AB",
        "\u230A",
        "\u23BF",
        "\u31C4",
        "\u31DF",
        "\u230A",
        "\u23BF",
        "\u03B9"]

invm = ["\u1D6F",
        "\u1D50",
        "\u1E41",
        "\u1E43",
        "\u1E3F",
        "\u1E43",
        "\u1E41",
        "\u1DAC",
        "\u1D86",
        "\u1D6F",
        "\u1C6C",
        "\u1C9D"]

invn = ["\u1E45",
        "\u1E47",
        "\u1E49",
        "\u1E4B",
        "\u1F20",
        "\u1F20",
        "\u1F22",
        "\u00f1",
        "\u0149",
        "\u0144",
        "\u0377"]

invo = ["\u03BF",
        "\u03CC",
        "\u043E",
        "\u0473",
        "\u04E7",
        "\u04EB",
        "\u101D",
        "\u1D52",
        "\u1ECD",
        "\u1ED9",
        "\u1ED3",
        "\u1ED5"]

invp = ["\u01A5",
        "\u03F8",
        "\u048F",
        "\u16B9",
        "\u1D29",
        "\u1D7D",
        "\u1D71",
        "\u1E55",
        "\u1E57",
        "\u01A4",
        "\u01F7"]
invq = ["\u01A3",
        "\u1CB9",
        "\u1D68",
        "\u1D91",
        "\u24E0",
        "\u01EB",
        "\u01ED",
        "\u051B",
        "\u0566",
        "\u1475",
        "\u1485",
        "\u24AC"]

invr = ["\u0155",
        "\u0157",
        "\u0159",
        "\u0211",
        "\u02B3",
        "\u1E59",
        "\u1E5B",
        "\u0491",
        "\u04F7",
        "\u1D63",
        "\u1E59"]

invs = ["\u015B",
        "\u015D",
        "\u0161",
        "\u0219",
        "\u0455",
        "\u1DB3",
        "\u1E61",
        "\u1E63",
        "\u1E69",
        "\u2D27",
        "\u01A8",
        "\u015F"]

invt = ["\u0163",
        "\u0165",
        "\u0167",
        "\u16BE",
        "\u1D75",
        "\u1E6B",
        "\u1E6D",
        "\u1E71",
        "\u03EF",
        "\u1D7C",
        "\u1E6F"]

invu = ["\u00F9",
        "\u00FA",
        "\u00FB",
        "\u00FC",
        "\u0169",
        "\u01DA",
        "\u0367",
        "\u1D64",
        "\u1DB6",
        "\u1DB8",
        "\u1E77",
        "\u1E73"]

invv = ["\u02C5",
        "\u036E",
        "\u0475",
        "\u0477",
        "\u1E7D",
        "\u1E7F",
        "\u24B1",
        "\u24E5",
        "\u2A52",
        "\u0264",
        "\u02EC"]

invw = ["\u1E81",
        "\u1E83",
        "\u1E85",
        "\u1E87",
        "\u1E89",
        "\u03C9",
        "\u0449",
        "\u051D",
        "\u1799",
        "\u2C73",
        "\u2D0D",
        "\u03E3"]

invx = ["\u0445",
        "\u04B3",
        "\u04FD",
        "\u1D61",
        "\u1D8D",
        "\u1E8B",
        "\u1E8D",
        "\u24B3",
        "\u1D8D",
        "\u2093",
        "\u2179"]
invy = ["\u00FD",
        "\u00FF",
        "\u0177",
        "\u01B4",
        "\u024F",
        "\u0233",
        "\u028F",
        "\u03B3",
        "\u045E",
        "\u04B1",
        "\u04AF",
        "\u04F1"]

invz = ["\u017A",
        "\u017C",
        "\u017E",
        "\u01B6",
        "\u0225",
        "\u1D76",
        "\u1DBB",
        "\u1DBC",
        "\u1DBD",
        "\u1E93",
        "\u1E91"]

while k == 0:
    if ky.is_pressed("a"):
        rana: list[str] = random.choices(inva)
        transa = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowa = str(rana).translate(transa)
        ky.write(str(lowa))
    if ky.is_pressed("b"):
        ranb: list[str] = random.choices(invb)
        transb = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowb = str(ranb).translate(transb)
        ky.write(str(lowb))
    if ky.is_pressed("c"):
        ranc: list[str] = random.choices(invc)
        transc = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowc = str(ranc).translate(transc)
        ky.write(str(lowc))
    if ky.is_pressed("d"):
        rand: list[str] = random.choices(invd)
        transd = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowd = str(rand).translate(transd)
        ky.write(str(lowd))
    if ky.is_pressed("e"):
        rane: list[str] = random.choices(inve)
        transe = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowe = str(rane).translate(transe)
        ky.write(str(lowe))
    if ky.is_pressed("f"):
        ranf: list[str] = random.choices(invf)
        transf = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowf = str(ranf).translate(transf)
        ky.write(str(lowf))
    if ky.is_pressed("g"):
        rang: list[str] = random.choices(invg)
        transg = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowg = str(rang).translate(transg)
        ky.write(str(lowg))
    if ky.is_pressed("h"):
        ranh: list[str] = random.choices(invh)
        transh = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowh = str(ranh).translate(transh)
        ky.write(str(lowh))
    if ky.is_pressed("i"):
        rani: list[str] = random.choices(invi)
        transi = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowi = str(rani).translate(transi)
        ky.write(str(lowi))
    if ky.is_pressed("j"):
        ranj: list[str] = random.choices(invj)
        transj = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowj = str(ranj).translate(transj)
        ky.write(str(lowj))
    if ky.is_pressed("k"):
        rank: list[str] = random.choices(invk)
        transk = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowk = str(rank).translate(transk)
        ky.write(str(lowk))
    if ky.is_pressed("l"):
        ranl: list[str] = random.choices(invl)
        transl = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowl = str(ranl).translate(transl)
        ky.write(str(lowl))
    if ky.is_pressed("m"):
        ranm: list[str] = random.choices(invm)
        transm = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowm = str(ranm).translate(transm)
        ky.write(str(lowm))
    if ky.is_pressed("n"):
        rann: list[str] = random.choices(invn)
        transn = {44: None, 39: None, 32: None, 91: None, 93: None}
        lown = str(rann).translate(transn)
        ky.write(str(lown))
    if ky.is_pressed("o"):
        rano: list[str] = random.choices(invo)
        transo = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowo = str(rano).translate(transo)
        ky.write(str(lowo))
    if ky.is_pressed("p"):
        ranp: list[str] = random.choices(invp)
        transp = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowp = str(ranp).translate(transp)
        ky.write(str(lowp))
    if ky.is_pressed("q"):
        ranq: list[str] = random.choices(invq)
        transq = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowq = str(ranq).translate(transq)
        ky.write(str(lowq))
    if ky.is_pressed("r"):
        ranr: list[str] = random.choices(invr)
        transr = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowr = str(ranr).translate(transr)
        ky.write(str(lowr))
    if ky.is_pressed("s"):
        rans: list[str] = random.choices(invs)
        transs = {44: None, 39: None, 32: None, 91: None, 93: None}
        lows = str(rans).translate(transs)
        ky.write(str(lows))
    if ky.is_pressed("t"):
        rant: list[str] = random.choices(invt)
        transt = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowt = str(rant).translate(transt)
        ky.write(str(lowt))
    if ky.is_pressed("u"):
        ranu: list[str] = random.choices(invu)
        transu = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowu = str(ranu).translate(transu)
        ky.write(str(lowu))
    if ky.is_pressed("v"):
        ranv: list[str] = random.choices(invv)
        transv = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowv = str(ranv).translate(transv)
        ky.write(str(lowv))
    if ky.is_pressed("w"):
        ranw: list[str] = random.choices(invw)
        transw = {44: None, 39: None, 32: None, 91: None, 93: None}
        loww = str(ranw).translate(transw)
        ky.write(str(loww))
    if ky.is_pressed("x"):
        ranx: list[str] = random.choices(invx)
        transx = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowx = str(ranx).translate(transx)
        ky.write(str(lowx))
    if ky.is_pressed("y"):
        rany: list[str] = random.choices(invy)
        transy = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowy = str(rany).translate(transy)
        ky.write(str(lowy))
    if ky.is_pressed("z"):
        ranz: list[str] = random.choices(invz)
        transz = {44: None, 39: None, 32: None, 91: None, 93: None}
        lowz = str(ranz).translate(transz)
        ky.write(str(lowz))
    if ky.is_pressed("`"):
        raise SystemExit
# import keyboard

# while a >= 3 and a <= 50:
#   print(a)
#   a = a+1
#   time.sleep(.01)
# a = 0

# while a == 0:
#    if keyboard.is_pressed("m"):
#        print("\b")
#        keyboard.press("u")
#        a = 1
#   menu = input("PLease select option \n"
#               "1.\n"
#               "2.\n"
#               "3.\n")
#  if menu == "1":
#      print("1")
#  elif menu == "2":
#     print("2")
#  elif menu == "3":
#       print("3")

#   else:
#   a = 1
#     print("no option selected")
