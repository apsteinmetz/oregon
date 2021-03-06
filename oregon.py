# __author__ = 'steinmetz'
#
# 10 REM PROGRAM NAME - OREGON        VERSION: 01/01/78
# 20 REM ORIGINAL PROGRAMMING BY BILL HEINEMANN - 1971
# 30 REM SUPPORT RESEARCH AND MATERIALS BY DON RAWITSCH,
# 40 REM      MINNESOTA EDUCATIONAL COMPUTING CONSORTIUM STAFF
# 50 REM CDC CYBER 70/73-26     BASIC 3.1
# 60 REM DOCUMENTATION BOOKLET 'OREGON' AVAILABLE FROM
# 61 REM    MECC SUPPORT SERVICES
# 62 REM    2520 BROADWAY DRIVE
# 63 REM    ST. PAUL, MN 55113
# 80 REM
# 150 REM  *FOR THE MEANING OF THE VARIABLES USED, LIST LINES 6470-6790*
# 155 REM
# 6470 REM ***IDENTIFICATION OF VARIABLES IN THE PROGRAM***
# 6480 REM amtAnimals= AMOUNT SPENT ON ANIMALS
# 6490 REM AmtAmmo= AMOUNT SPENT ON AMMUNITION
# 6500 REM shotResponse = ACTUAL RESPONSE TIME FOR INPUTTING "BANG"
# 6510 REM ShotClock = CLOCK TIME START OF INPUTTING "BANG"
# 6520 REM C = AMOUNT SPENT ON CLOTHING
# 6530 REM C1 = FLAG FOR INSUFFICIENT CLOTHING IN COLD WEATHER
# 6540 REM YesOrNo = YES/NO RESPONSE TO QUESTIONS
# 6550 REM D1 = COUNTER IN GENERATING EVENTS
# 6560 REM D3 = TURN NUMBER FOR SETTING DATE
# 6570 REM D4 = CURRENT DATE
# 6580 REM shootingSkill = CHOICE OF SHOOTING EXPERTISE LEVEL
# 6590 REM E = CHOICE OF EATING
# 6600 REM amtFood = AMOUNT SPENT ON FOOD
# 6610 REM F1 = FLAG FOR CLEARING SOUTH PASS
# 6620 REM F2 = FLAG FOR CLEARING BLUE MOUNTAINS
# 6630 REM F9 = FRACTION OF 2 WEEKS TRAVELED ON FINAL TURN
# 6640 REM X5 = FLAG FOR INJURY
# 6650 REM L1 = FLAG FOR BLIZZARD
# 6660 REM M = TOTAL MILEAGE WHOLE TRIP
# 6670 REM M1 = AMOUNT SPENT ON MISCELLANEOUS SUPPLIES
# 6680 REM M2 = MILEAGE UP THROUGH PREVIOUS TURN
# 6690 REM M9 = FLAG FOR CLEARING SOUTH PASS IN SETTING MILEAGE
# 6700 REM P = AMOUNT SPENT ON ITEMS AT FORT
# 6710 REM R1 = RANDOM NUMBER IN CHOOSING EVENTS
# 6720 REM S4 = FLAG FOR ILLNESS
# 6730 REM S5 = ""HOSTILITY OF RIDERS"" FACTOR
# 6740 REM S6 = SHOOTING WORD SELECTOR
# 6750 REM S$ = VARIATIONS OF SHOOTING WORD
# 6760 REM cashBalance= CASH LEFT OVER AFTER INITIAL PURCHASES
# 6770 REM T1 = CHOICE OF TACTICS WHEN ATTACKED
# 6780 REM X = CHOICE OF ACTION FOR EACH TURN
# 6790 REM fortOption = FLAG FOR FORT OPTION

def inputInt(message, errmsg):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            assert isinstance(errmsg)
            print(errmsg)
            continue
        else:
            return userInput
            break


def inputYorN(message):
    errmsg = 'Type Yes or No'
    while True:
        try:
            userInput = input(message)
        except userInput not in ("YES", "NO", "yes", "no"):
            assert isinstance(errmsg)
            print(errmsg)
            continue
        else:
            return userInput
            break


YesOrNo = input("DO YOU NEED INSTRUCTIONS (YES/NO)")

# 180 REM RANDOMIZE REMOVED
# If YesOrNo="NO" THEN 690
def showIinstructions():
    print()
    print()
    # 230 REM ***INSTRUCTIONS***
    print("THIS PROGRAM SIMULATES A TRIP OVER THE OREGON TRAIL FROM")
    print("INDEPENDENCE MISSOURI TO OREGON CITY, OREGON IN 1847.")
    print("YOUR FAMILY OF FIVE WILL COVER THE 2040 MILE OREGON TRAIL")
    print("IN 5-6 MONTHS --- if YOU MAKE IT ALIVE.")
    print()
    print("YOU HAD SAVED $900 TO SPEND FOR THE TRIP, AND YOU'VE JUST")
    print("   PAID $200 FOR A WAGON.")
    print("YOU WILL NEED TO SPEND THE REST OF YOUR MONEY ON THE")
    print("   FOLLOWING ITEMS:")
    print()
    print("     OXEN – YOU CAN SPEND $200-$300 ON YOUR TEAM")
    print("            THE MORE YOU SPEND, THE FASTER YOU'LL GO")
    print("               BECAUSE YOU'LL HAVE BETTER ANIMALS")
    print()
    print("     FOOD – THE MORE YOU HAVE, THE LESS CHANCE THERE")
    print("               IS OF GETTING SICK")
    print()
    print("     AMMUNITION - $1 BUYS A BELT OF 50 BULLETS")
    print("            YOU WILL NEED BULLETS FOR ATTACKS BY ANIMALS")
    print("               AND BANDITS, AND FOR HUNTING FOOD")
    print()
    print("     CLOTHING – THIS IS ESPECIALLY IMPORTANT FOR THE COLD")
    print("               WEATHER YOU WILL ENCOUNTER WHEN CROSSING")
    print("               THE MOUNTAINS")
    print()
    print("     MISCELLANEOUS SUPPLIES – THIS INCLUDES MEDICINE AND")
    print("               OTHER THINGS YOU WILL NEED FOR SICKNESS")
    print("               AND EMERGENCY REPAIRS")
    print()
    print()
    print("YOU CAN SPEND ALL YOUR MONEY BEFORE YOU START YOUR TRIP -")
    print("OR YOU CAN SAVE SOME OF YOUR CASH TO SPEND AT FORTS ALONG")
    print("THE WAY WHEN YOU RUN LOW. HOWEVER, ITEMS COST MORE AT")
    print("THE FORTS. YOU CAN ALSO GO HUNTING ALONG THE WAY TO GET")
    print("MORE FOOD.")
    print("WHENEVER YOU HAVE TO USE YOUR TRUSTY RIFLE ALONG THE WAY,")
    print("YOU WILL BE TOLD TO TYPE IN A WORD (ONE THAT SOUNDS LIKE A")
    print("GUN SHOT). THE FASTER YOU TYPE IN THAT WORD AND HIT THE")
    print("**RETURN** KEY, THE BETTER LUCK YOU'LL HAVE WITH YOUR GUN.")
    print()
    print("AT EACH TURN, ALL ITEMS ARE SHOWN IN DOLLAR AMOUNTS")
    print("EXCEPT BULLETS")
    print("WHEN ASKED TO ENTER MONEY AMOUNTS, DON'T USE A **$**.")
    print()
    print("GOOD LUCK!!!")
    print()
    # 700


print("HOW GOOD A SHOT ARE YOU WITH YOUR RIFLE?")
print("  (1) ACE MARKSMAN,  (2) GOOD SHOT,  (3) FAIR TO MIDDLIN'")
print("         (4) NEED MORE PRACTICE,  (5) SHAKY KNEES")
print("ENTER ONE OF THE ABOVE – THE BETTER YOU CLAIM YOU ARE, THE")
print("FASTER YOU'LL HAVE TO BE WITH YOUR GUN TO BE SUCCESSFUL.")
shootingSkill = inputInt("1,2,3,4 or 5", "Type a number between 1 and 5")
if (shootingSkill < 0) or (shootingSkill > 5):  shootingSkill = 0
# 800 REM ***INITIAL PURCHASES***# 800

cashBalance = 700
while cashBalance > 0:
    fortOption = False  # 810
    # 820 K8*S4*F1*F2*M*M9*D3=0 # 820
    # 830 print()
    # 840 print()
    amtAnimals = 0
    while (amtAnimals < 200) or (amtAnimals > 300):
        amtAnimals=inputInt( "HOW MUCH DO YOU WANT TO SPEND ON YOUR OXEN TEAM?","Enter a number") # 850
        if amtAnimals < 200: print("Not Enough!")
        if amtAnimals < 300: print("Too Much!")

    cashBalance = cashBalance-amtAnimals
    amtFood = 0
    while (amtFood <1):
        amtFood = inputInt( "HOW MUCH DO YOU WANT TO SPEND ON FOOD?","Enter a number") # 850
        if amtFood < 1: print("Impossible! Try Again.")
        if cashBalance-amtFood < 0: print("Too Much!")

    # 980 print( "HOW MUCH DO YOU WANT TO SPEND ON AMMUNITION";
    # 990 INPUT B
    # 1000 if AmtAmmo>= 0 THEN 1030
    # 1010 print( "IMPOSSIBLE"
    # 1020 GOTO 980
    # 1030 print( "HOW MUCH DO YOU WANT TO SPEND ON CLOTHING";
    # 1040 INPUT C
    # 1050 if C >= 0 THEN 1080
    # 1060 print( "IMPOSSIBLE"
    # 1070 GOTO 1030
    # 1080 print( "HOW MUCH DO YOU WANT TO SPEND ON MISCELLANEOUS SUPPLIES";
    # 1090 INPUT M1
    # 1100 if M1 >= 0 THEN 1130
    # 1110 print( "IMPOSSIBLE"
    # 1120 GOTO 1080
    # 1130 T=700-A-F-B-C-M1
    # 1140 if cashBalance>= 0 THEN 1170
    # 1150 print( "YOU OVERSPENT—YOU ONLY HAD $700 TO SPEND. BUY AGAIN"
    # 1160 GOTO 830
    # 1170 B=50+B
    # 1180 print( "AFTER ALL YOUR PURCHASES, YOU NOW HAVE ";cashBalance;" DOLLARS LEFT"
    # end initial spend
# 1190 print()
# 1200 print( "MONDAY MARCH 29 1847"
# 1210 print(
# 1220 GOTO 1750
# 1230 if M >= 2040 THEN 5430
# 1240 REM ***SETTING DATE****
# 1250 D3=D3+1
# 1260 print(
# 1270 print( "MONDAY ";
# 1280 if D3>10 THEN 1300
# 1290 ON D3 GOTO 1310,1330,1350,1370,1390,1410,1430,1450,1470,1490
# 1300 ON D3-10 GOTO 1510,1530,1550,1570,1590,1610,1630,1650,1670,1690
# 1310 print( "APRIL 12";
# 1320 GOTO 1720
# 1330 print( "APRIL 26 ";
# 1340 GOTO 1720
# 1350 print( "MAY 10";
# 1360 GOTO 1720
# 1370 print( "MAY 24 ";
# 1380 GOTO 1720
# 1390 print( "JUNE 7 ";
# 1400 GOTO 1720
# 1410 print( "JUNE 21 ";
# 1420 GOTO 1720
# 1430 print( "JULY 5 ";
# 1440 GOTO 1720
# 1450 print( "JULY 19 ";
# 1460 GOTO 1720
# 1470 print( "AUGUST 2 "'
# 1480 GOTO 1720
# 1490 print( "AUGUST 16 ";
# 1500 GOTO 1720
# 1510 print( "AUGUST 31 ";
# 1520 GOTO 1720
# 1530  print( "SEPTEMBER 13";
# 1540 GOTO 1720
# 1550 print( "SEPTEMBER 27 ";
# 1560 GOTO 1720
# 1570 print( "OCTOBER 11 ";
# 1580 GOTO 1720
# 1590 print( "OCTOBER 25"
# 1600 GOTO 1720
# 1610 print( "NOVEMBER 8 ";
# 1620 GOTO 1720
# 1630 print( "NOVEMBER 22 ";
# 1640 GOTO 1720
# 1650 print( "DECEMBER 6 ";
# 1660 GOTO 1720
# 1670 print( "DECEMBER 20 ";
# 1680 GOTO 1720
# 1690 print( "YOU HAVE BEEN ON THE TRAIL TOO LONG  ------"
# 1700 print( "YOUR FAMILY DIES IN THE FIRST BLIZZARD OF WINTER"
# 1710 GOTO 5170
# 1720 print( "1847"
# 1730 print(
# 1740 REM ***BEGINNING EACH TURN***
# 1750 if amtFood >= 0 THEN 1770
# 1760 F=0
# 1770 if AmtAmmo>= 0 THEN 1790
# 1780 B=0
# 1790 if C >= 0 THEN 1810
# 1800 C = 0
# 1810 if M1 >= 0 THEN 1830
# 1820 M1=0
# 1830 if amtFood >= 13 THEN 1650
# 1840 print( "YOU'D BETTER DO SOME HUNTING OR BUY FOOD AND SOON!!!!"
# 1850 F=INT(F)
# 1860 B=INT(B)
# 1870 C=INT(C)
# 1880 M1=INT(M1)
# 1890 T=INT(T)
# 1900 M=INT(M)
# 1910 M2=M
# 1920 if S4=1 THEN 1950
# 1930 if K8=1 THEN 1950
# 1940 GOTO 1990
# 1950 T=T-20
# 1960 if T<0 THEN 5080
# 1970 print( "DOCTOR'S BILL IS $20"
# 1980 LET K8=S4=0
# 1990 if M9=1 THEN 2020
# 2000 print( "TOTAL MILEAGE IS";M
# 2010 GOTO 2040
# 2020 print( "TOTAL MILEAGE IS 950"
# 2030 M9=0
# 2040 print( "FOOD","BULLETS","CLOTHING","MISC. SUPP.","CASH"
# 2050 print( F,B,C,M1,T
# if  fortOption = False: 2170
# fortOption= not(fortOption)
# 2080 print( "DO YOU WANT TO (1) STOP AT THE NEXT FORT, (2) HUNT, ";
# 2090 print( "OR (3) CONTINUE"
# 2100 INPUT X
# 2110 if X>2 THEN 2150
# 2120 if X<1 THEN 2150
# 2130 LET X=INT(X)
# 2140 GOTO 2270
# 2150 LET X=3
# 2160 GOTO 2270
# print( "DO YOU WANT TO (1) HUNT, OR (2) CONTINUE"
# 2180 INPUT X
# 2190 if X=1 THEN 2210
# 2200 LET X=2
# 2210 LET X=X+1
# 2220 if X=3 THEN 2260
# 2230 if B>39 THEN 2260
# 2240 print( "TOUGH---YOU NEED MORE BULLETS TO GO HUNTING"
# 2250 GOTO 2170
# 2260 fortOption= not(fortOption)
# 2270 ON X GOTO 2290,2540,2720
# 2280 REM ***STOPPING AT FORT***
# 2290 print( "ENTER WHAT YOU WISH TO SPEND ON THE FOLLOWING"
# 2300 print( "FOOD";
# 2310 GOSUB 2330
# 2320 GOTO 2410
# 2330 INPUT P
# 2340 if P<0 THEN 2400
# 2350 T=T-P
# 2360 if T >= 0 THEN 2400
# 2370 print( "YOU DON'T HAVE THAT MUCH--KEEP YOUR SPENDING DOWN"
# 2380 T=T+P
# 2390 P=0
# 2400 RETURN
# 2410 F=F+2/3*P
# 2420 print( "AMMUNITION";
# 2430 GOSUB 2330
# 2440 LET B=INT(B+2/3+P*50)
# 2450 print( "CLOTHING";
# 2460 GOSUB 2330
# 2470 C=C+2/3*P
# 2480 print( "MISCELLANEOUS SUPPLIES";
# 2490 GOSUB 2330
# 2500 M1=M1+2/3*P
# 2510 M=M-45
# 2520 GOTO 2720
# 2530 REM ***HUNTING***
# 2540 if B>39 THEN 2570
# 2550 print( "TOUGH---YOU NEED MORE BULLETS TO GO HUNTING"
# 2560 GOTO 2080
# 2570 M=M-45
# 2580 GOSUB 6140
# 2590 if shotResponse <= 1 THEN 2660
# 2600 if 100*RND(-1)<13*shotResponse THEN 2710
# 2620 print( "NICE SHOT—RIGHT ON TARGET—GOOD EATIN' TONIGHT!!"
# 2630 B=B-10-3*shotResponse
# 2640 GOTO 2720
# 2650 REM **BELLS IN LINE 2660**
# 2660 print( "RIGHT BETWEEN THE EYES---YOU GOT A BIG ONE!!!!"
# 2670 print( "FULL BELLIES TONIGHT!"
# 2680 F=F+52+RND(-1)*6
# 2690 B=B-10-RND(-1)*4
# 2700 GOTO 2720
# 2710 print( "YOU MISSED---AND YOUR DINNER GOT AWAY....."
# 2720 if amtFood >= 13 THEN 2750
# 2730 GOTO 5060
# 2740 REM ***EATING***
# 2750 print( "DO YOU WANT TO EAT (1) POORLY  (2) MODERATELY"
# 2760 print( "OR (3) WELL";
# 2770 INPUT E
# 2780 if E>3 THEN 2750
# 2790 if E<1 THEN 2750
# 2800 LET E=INT(E)
# 2810 LET F=F-8-5*E
# 2820 if amtFood >= 0 THEN 2860
# 2830 F=F+8+5*E
# 2840 print( "YOU CAN'T EAT THAT WELL"
# 2850 GOTO 2750
# 2860 LET M=M+200+(A-220)/5+10*RND(-1)
# 2870 L1=C1=0
# 2880 REM ***RIDERS ATTACK***
# 2890 if RND(-1)*10>((M/100-4)**27+72)/((M/100-4)**2+12)-1 THEN 3550
# 2900 print( "RIDERS AHEAD.  THEY ";
# 2910 S5=0
# 2920 if RND(-1)<.8 THEN 2950
# 2930 print( "DON'T ";
# 2940 S5=1
# 2950 print( "LOOK HOSTILE"
# 2960 print( "TACTICS"
# 2970 print( "(1) RUN  (2) ATTACK  (3) CONTINUE  (4) CIRCLE WAGONS"
# 2980 if RND(-1)>.2 THEN 3000
# 2990 S5=1-S5
# 3000 INPUT T1
# 3010 if T1<1 THEN 2970
# 3020 if T1>4 THEN 2970
# 3030 T1=INT(T1)
# 3040 if S5=1 THEN 3330
# 3050 if T1>1 THEN 3110
# 3060 M=M+20
# 3070 M1=M1-15
# 3080 B=B-150
# 3090 A=A-40
# 3100 GOTO 3470
# 3110 if T1>2 THEN 3240
# 3120 GOSUB 6140
# 3130 B=B-shotResponse*40-80
# 3140 if shotResponse>1 THEN 3170
# 3150 print( "NICE SHOOTING---YOU DROVE THEM OFF"
# 3160 GOTO 3470
# 3170 if shotResponse <= 4 THEN 3220
# 3180 print( "LOUSY SHOT---YOU GOT KNIFED"
# 3190 K8=1
# 3200 print( "YOU HAVE TO SEE OL' DOC BLANCHARD"
# 3210 GOTO 3470
# 3220 print( "KINDA SLOW WITH YOUR COLT .45"
# 3230 GOTO 3470
# 2340 if T1>3 THEN 2390
# 3250 if RND(-1)>.8 THEN 3450
# 2360 LET B=B-150
# 2370 M1=M1-15
# 2380 GOTO 3470
# 3290 GOSUB 6140
# 3300 B=B-shotResponse*30-80
# 3310 M=M-25
# 3320 GOTO 3140
# 3330 if T1>1 THEN 3370
# 3340 M=M+15
# 3350 A=A-10
# 3360 GOTO 3470
# 3370 if T1>2 THEN 3410
# 3380 M=M-5
# 3390 B=B-100
# 3400 GOTO 3470
# 3410 if T1>3 THEN 3430
# 3420 GOTO 3470
# 3430 M=M-20
# 3440 GOTO 3470
# 3450 print( "THEY DID NOT ATTACK"
# 3460 GOTO 3550
# 3470 if S5=0 THEN 3500
# 3480 print( "RIDERS WERE FRIENDLY, BUT CHECK FOR POSSIBLE LOSSES"
# 3490 GOTO 3550
# 3500 print( "RIDERS WERE HOSTILE--CHECK FOR LOSSES"
# 3510 if AmtAmmo>= 0 THEN 3550
# 3520 print( "YOU RAN OUT OF BULLETS AND GOT MASSACRED BY THE RIDERS"
# 3530 GOTO 5170
# 3540 REM ***SELECTION OF EVENTS***
# 3550 LET D1=0
# 3560 RESTORE
# 3570 R1=100*RND(-1)
# 3580 LET D1=D1+1
# 3590 if D1=16 THEN 4670
# 3600 READ D
# 3610 if R1>D THEN 3580
# 3620 DATA 6,11,13,15,17,22,32,35,37,42,44,54,64,69,95
# 3630 if D1>10 THEN 3650
# 3640 ON D1 GOTO 3660,3700,3740,3790,3820,3850,3880,3960,4130,4190
# 3650 ON D1-10 GOTO 4220,4290,4340,4650,4610,4670
# 3660 print( "WAGON BREAKS DOWN--LOSE TIME AND SUPPLIES FIXING IT"
# 3670 LET M=M-15-5*RND(-1)
# 3680 LET M1=M1-8
# 3690 GOTO 4710
# 3700 print( "OX INJURES LEG---SLOWS YOU DOWN REST OF TRIP"
# 3710 LET M=M-25
# 3720 LET A=A-20
# 3730 GOTO 4710
# 3740 print( "BAD LUCK---YOUR DAUGHTER BROKE HER ARM"
# 3750 print( "YOU HAD TO STOP AND USE SUPPLIES TO MAKE A SLING"
# 3760 M=M-5-4*RND(-1)
# 3770 M1=M1-2-3*RND(-1)
# 3780 GOTO 4710
# 3790 print( "OX WANDERS OFF---SPEND TIME LOOKING FOR IT"
# 3800 M=M-17
# 3810 GOTO 4710
# 3820 print( "YOUR SON GETS LOST---SPEND HALF THE DAY LOOKING FOR HIM"
# 3830 M=M-10
# 3840 GOTO 4710
# 3850 print( "UNSAFE WATER--LOSE TIME LOOKING FOR CLEAN SPRING"
# 3860 LET M=M-10*RND(-1)*-2
# 3870 GOTO 4710
# 3880 if M>950 THEN 4490
# 3890 print( "HEAVY RAINS---TIME AND SUPPLIES LOST"
# 3910 F=F-10
# 3920 B=B-500
# 3930 M1=M1-15
# 3940 M=M-10*RND(-1)-5
# 3950 GOTO 4710
# 3960 print( "BANDITS ATTACK"
# 3970 GOSUB 6140
# 3980 B=B-20*shotResponse
# 3990 if B>= 0- THEN 4030
# 4000 print( "YOU RAN OUT OF BULLETS---THEY GET LOTS OF CASH"
# 4010 T=T/3
# 4020 GOTO 4040
# 4030 if shotResponse <= 1 THEN 4100
# 4040 print( "YOU GOT SHOT IN THE LEG AND THEY TOOK ONE OF YOUR OXEN"
# 4050 K8=1
# 4060 print( "BETTER HAVE A DOC LOOK AT YOUR WOUND"
# 4070 M1=M1-5
# 4080 A=A-20
# 4090 GOTO 4710
# 4100 print( "QUICKEST DRAW OUTSIDE OF DODGE CITY!!!"
# 4110 print( "YOU GOT 'EM!"
# 4120 GOTO 4710
# 4130 print( "THERE WAS A FIRE IN YOUR WAGON--FOOD AND SUPPLIES DAMAGE!"
# 4140 F=F-40
# 4150 B=B-400
# 4160 LET M1=M1-RND(-1)*68-3
# 4170 M=M-15
# 4180 GOTO 4710
# 4190 print( "LOSE YOUR WAY IN HEAVY FOG---TIME IS LOST"
# 4200 M=M-10-5*RND(-1)
# 4210 GOTO 4710
# 4190 print( "LOSE YOUR WAY IN HEAVY FOG---TIME IS LOST"
# 4200 M=M-10-5*RND(-1)
# 4210 GOTO 4710
# 4220 print( "YOU KILLED A POISONOUS SNAKE AFTER IT BIT YOU"
# 4230 B=B-10
# 4240 M1=M1-5
# 4250 if M1 >= 0 THEN 4280
# 4260 print( "YOU DIE OF SNAKEBITE SINCE YOU HAVE NO MEDICINE"
# 4270 GOTO 5170
# 4280 GOTO 4710
# 4290 print( "YOUR WAGON GETS SWAMPED FORDING RIVER--LOSE FOOD AND CLOTHES"
# 4300 F=F-30
# 4310 C=C-20
# 4320 M=M-20-20*RND(-1)
# 4330 GOTO 4710
# 4340 print( "WILD ANIMALS ATTACK!"
# 4350 GOSUB 6140
# 4360 if B>39 THEN 4410
# 4370 print( "YOU WERE TOO LOW ON BULLETS--"
# 4380 print( "THE WOLVES OVERPOWERED YOU"
# 4390 K8=1
# 440 GOTO 5120
# 4410 if ShotResponse>2 THEN 4440
# 4420 print( "NICE SHOOTIN' PARDNER---THEY DIDN'T GET MUCH"
# 4430 GOTO 4450
# 4440 print( "SLOW ON THE DRAW---THEY GOT AT YOUR FOOD AND CLOTHES"
# 4450 B=B-20*ShotResponse
# 4460 C=C-ShotResponse*4
# 4470 F=F-ShotResponse*8
# 4480 BOTO 4710
# 4490 print( "COLD WEATHER---BRRRRRRR!---YOU ";
# 4500 if C>22+4*RND(-1) THEN 4530
# 4510 print( "DON'T ";
# 4520 C1=1
# 4530 print( "HAVE ENOUGH CLOTHING TO KEEP WARM"
# 4540 if C1=0 THEN 4710
# 4550 GOTO 6300
# 4560 print( "HAIL STORM---SUPPLIES DAMAGED"
# 4570 M=M-5-RND(-1)*10
# 4580 B=B-200
# 4590 M1=M1-4-RND(-1)*3
# 4600 GOTO 4710
# 4610 if E=1 THEN 6300
# 4620 if E=3 THEN 4650
# 4630 if RND(-1)>.25 THEN 6300
# 4640 GOTO 4710
# 4650 if RND(-1)<.5 THEN 6300
# 4660 GOTO 4710
# 4670 print( "HELPFUL INDIANS SHOW YOU WHERE TO FIND MORE FOOD"
# 4680  F=F+14
# 4690 GOTO 4710
# 4700 REM ***MOUNTAINS***
# 4710 if M <= 950 THEN 1230
# 4720 if RND(-1)*10>9-((M/100-15)**2+72)/((M/100-15)**2+12) THEN 4560
# 4730 print( "RUGGED MOUNTAINS"
# 4740 if RND(-1)>.1 THEN 4780
# 4750 print( "YOU GOT LOST---LOSE VALUABLE TIME TRYING TO FIND TRAIL!"
# 4760 M=M-60
# 4770 GOTO 4560
# 4780 if RND(-1)>.11 THEN 4840
# 4790 print( "WAGON DAMAGED!---LOSE TIME AND SUPPLIES"
# 4800 M1=M1-5
# 4810 B=B-200
# 4820 M=M-20-30*RND(-1)
# 4830 GOTO 4860
# 4840 print( "THE GOING GETS SLOW"
# 4850 M=M-45-RND(-1)/.02
# 4860 if F1=1 THEN 4900
# 4870 F1=1
# 4880 if RND(-1)<.8 THEN 4970
# 4890 print( "YOU MADE IT SAFELY THROUGH SOUTH PASS--NO SNOW"
# 4900 if M<1700 THEN 4940
# 4910 if F2=1 THEN 4940
# 4920 F2=1
# 4930 if RND(-1)<.7 THEN 4970
# 4940 if M>950 THEN 1230
# 4950 M9=1
# 4960 GOTO 1230
# 4970 print( "BLIZZARD IN MOUNTAIN PASS--TIME AND SUPPLIES LOST"
# 4980 L1=1
# 4990 F=F-25
# 5000 M1=M1-10
# 5010 B=B-300
# 5020 M=M-30-40*RND(-1)
# 5030 if C<18+2*RND(-1) THEN 6300
# 5040 GOTO 4940
# 5050 REM ***DYING***
# 5060 print( "YOU RAN OUT OF FOOD AND STARVED TO DEATH"
# 5070 GOTO 5170
# 5080 LET T=0
# 5090 print( "YOU CAN'T AFFORD A DOCTOR"
# 5100 GOTO 5120
# 5110 print( "YOU RAN OUT OF MEDICAL SUPPLIES"
# 5120 print( "YOU DIED OF ";
# 5130 if K8=1 THEN 5160
# 5140 print( "PNEUMONIA"
# 5150 GOTO 5170
# 5160 print( "INJURIES"
# 5170 print(
# 5180 print( "DUE TO YOUR UNFORTUNATE SITUATION, THERE ARE A FEW"
# 5190 print( "FORMALITIES WE MUST GO THROUGH"
# 5200 print(
# 5210 print( "WOULD YOU LIKE A MINISTER?"
# 5220 INPUT YesOrNo
# 5230 print( "WOULD YOU LIKE A FANCY FUNERAL?"
# 5240 INPUT YesOrNo
# 5250 print( "WOULD YOU LIKE US TO INFORM YOUR NEXT OF KIN?"
# 5260 INPUT YesOrNo
# 5270 if YesOrNo="YES" THEN 5310
# 5280 print( "BUT YOUR AUNT SADIE IN ST. LOUIS IS REALLY WORRIED ABOUT YOU
# 5290 print(
# 5300 GOTO 5330
# 5310 print( "THAT WILL BE $4.50 FOR THE TELEGRAPH CHARGE."
# 5320 print(
# 5330 print( "WE THANK YOU FOR THIS INFORMATION AND WE ARE SORRY YOU"
# 5340 print( "DIDN'T MAKE IT TO THE GREAT TERRITORY OF OREGON"
# 5350 print( "BETTER LUCK NEXT TIME"
# 5360 print(
# 5370 print(
# 5380 print( TAB(30);"SINCERELY"
# 5390 print(
# 5400 print( TAB(17);"THE OREGON CITY CHAMBER OF COMMERCE"
# 5410 STOP
# 5420 REM ***FINAL TURN***
# 5430 F9=(2040-M2)/(M-M2)
# 5440 F=F+(1-F9)*(8+5*E)
# 5450 print(
# 5460 REM **BELLS IN LINES 5470,5480**
# 5470 print( "YOU FINALLY ARRIVED AT OREGON CITY"
# 5480 print( "AFTER 2040 LONG MILES---HOORAY!!!!!"
# 5490 print( "A REAL PIONEER!"
# 5500 print(
# 5510 F9=INT(F9*14)
# 5520 D3=D3*14+F9
# 5530 F9=F9+1
# 5540 if F9<5 THEN 5560
# 5550 F9=F9-7
# 5560 ON F9 GOTO 5570,5590,5610,5630,5650,5670,5690
# 5570 print( "MONDAY ";
# 5580 GOTO 5700
# 5590 print( "TUESDAY ";
# 5600 GOTO 5700
# 5610 print( "WEDNESDAY ";
# 5620 GOTO 5700
# 5630 print( "THURSDAY ";
# 5640 GOTO 5700
# 6650 print( "FRIDAY ";
# 5660 GOTO 5700
# 5670 print( "SATURDAY ";
# 5680 GOTO 5700
# 5690 print( "SUNDAY ";
# 5700 if D3>124 THEN 5740
# 5710 D3=D3-93
# 5720 print( "JULY ";D3;" 1847"
# 5730 GOTO 5920
# 5740 if D3>155 THEN 5780
# 5750 D3=D3-124
# 5760 print( "AUGUST ";D3;" 1847"
# 5770 GOTO 5920
# 5780 if D3>165 THEN 5820
# 5790 D3=D3-155
# 5800 print( "SEPTEMBER ";D3;" 1847"
# 5810 GOTO 5920
# 5820 if D3>216 THEN 5860
# 5830 D3=D3-185
# 5840 print( "OCTOBER ";D3;" 1847"
# 5850 GOTO 5920
# 5860 if D3>246 THEN 5900
# 5870 D3=D3-216
# 5880 print( "NOVEMBER ";D3;" 1847"
# 5890 GOTO 5920
# 5900 D3=D3-246
# 5910 print( "DECEMBER ";D3;"1847"
# 5920 print(
# 5930 print( "FOOD","BULLETS","CLOTHING","MISC. SUPP.","CASH"
# 5940 if B>0 THEN 5960
# 5950 LET B=0
# 5960 if C>0 THEN 5950
# 5970 LET C=0
# 5980 if M1>0 THEN 6000
# 5990 LET M1=0
# 6000 if T>0 THEN 6020
# 6010 LET T=0
# 6020 if F>0 THEN 6040
# 6030 LET F=0
# 6040 print( INT(F),INT(B),INT(C),INT(M1),INT(T)
# 6050 print(
# 6060 print( TAB(11); "PRESIDENT JAMES K. POLK SENDS YOU HIS"
# 6070 print( TAB(17); "HEARTIEST CONGRATULATIONS"
# 6080 print(
# 6090 print( TAB(11);"AND WISHES YOU A PROSERPOUS LIFE AHEAD"
# 6100 print(
# 6110 print( TAB(22);"AT YOUR NEW HOME"
# 6120 STOP
# 6130 REM ***SHOOTING SUB-ROUTINE***
# 6131 REM THE METHOD OF TIMING THE SHOOTING (LINES 6210-6240)
# 6132 REM WILL VARY FROM SYSTEM TO SYSTEM. FOR EXAMPLE, H-P
# 6133 REM USERS WILL PROBABLY PREFER TO USE THE 'ENTER' STATEMENT.
# 6134 REM if TIMING ON THE USER'S SYSTEM IS HIGHLY SUCEPTIBLE
# 6135 REM TO SYSTEM RESPONSE TIME, THE FORMULA IN LINE 6240 CAN
# 6136 REM BE TAILORED TO ACOMMODATE THIS BY EITHER INCREASING
# 6137 REM OR DECREASING THE 'SHOOTING' TIME RECORDED BY THE SYSTEM.
# 6140 DIM S$(5)
# 6150 S$(1)="BANG"
# 6160 S$(2)="BLAM"
# 6170 S$(3)="POW"
# 6180 S$(4)="WHAM"
# 6190 S6=INT(RND(-1)*4+1)
# 6200 print( "TYPE "; S$(56)
# 6210 ShotClock = CLK(0)
# 6220 INPUT YesOrNo
# 6230 ShotResponse = CLK(0)
# 6240 ShotResponse=((ShotResponse-ShotClock)*3600)-(shootingSkill-1)
# 6250 print(
# 6255 if ShotResponse>0 THEN 6260
# 6257 ShotResponse=0
# 6260 if YesOrNo=S$(56) THEN 6280
# 6270 ShotResponse=0
# 6280 RETURN
# 6290 REM ***ILLNESS SUB-ROUTINE***
# 6300 if 100*RND(-1)<10+35(E-1) THEN 6370
# 6310 if 100*RND(-1)<100-(40/4**(E-1)) THEN 6410
# 6320 print( "SERIOUS ILLNESS---"
# 6330 print( "YOU MUST STOP FOR MEDICAL ATTENTION"
# 6340 M1=M1-10
# 6350 S4=1
# 6360 GOTO 6440
# 6370 print( "MILD ILLNESS---MEDICINE USED"
# 6380 M=M-5
# 6390 M1=M1-2
# 6400 GOTO 6440
# 6410 print( "BAD ILLNESS---MEDICINE USED"
# 6420 M=M-5
# 6430 M1=M1-5
# 64540 if M1<0 THEN 5110
# 6450 if L1=1 THEN 4940
# 6460 GOTO 4710

# 6800 END

showIinstructions()