import sys

Ans = ""
Name = ""
Genre = ""
XBucle = False

print ""
print " Darutik presents..."
print ""
print " 01000010 01110010 01101111 01111001 01100001"
print " More knowed as..."
print ""
print ""
print ""
print " :::::::::  :::::::::   ::::::::  :::   :::   :::     "
print " :+:    :+: :+:    :+: :+:    :+: :+:   :+: :+: :+:   "
print " +:+    +:+ +:+    +:+ +:+    +:+  +:+ +:+ +:+   +:+  "
print " +#++:++#+  +#++:++#:  +#+    +:+   +#++: +#++:++#++: "
print " +#+    +#+ +#+    +#+ +#+    +#+    +#+  +#+     +#+ "
print " #+#    #+# #+#    #+# #+#    #+#    #+#  #+#     #+# "
print " #########  ###    ###  ########     ###  ###     ### "
print ""
print ""
print ""
raw_input("")
print " When something like ==> apear, you must select a number."
raw_input("")
print ""

print ""
print " SOMEONE:"
print " Hello."
raw_input("")
print " YOU:"
print " He-hello...?"
raw_input("")
print "SOMEONE:"
print " Are you OK?"
print ""
print " 1. Yes..."
print " 2. Who are you?"
print " 3. I'm dead..."
while (XBucle != True):
    Ans = raw_input("==> ")
    if Ans == "1":
        print " YOU:"
        print " Yes..."
        raw_input("")
        print " SOMEONE:"
        print " Sure?"
        raw_input("")
        print " YOU:"
        print " Yes, I'm right..."
        raw_input("")
        print " SOMEONE:"
        print " What's your name?"
        Name = raw_input("==> ")
        print " " + Name + ":"
        print " I'm... " + Name + "."
        print " People call me " + Name + "..."
        raw_input("")
        print " SOMEONE:"
        print " Okay, " + Name + ". I'm Kevin, and I found you near the river, in the East."
        print " You were unconscious, so I let you in my house, inside the forest."
        XBucle = True
    elif Ans == "2":
        print " YOU:"
        print " Who are you?"
        raw_input("")
        print " SOMEONE:"
        print " I'm Kevin. I found you near the river, in the East."
        print " You were unconscious, so I let you in my house, inside the forest."
        raw_input("")
        print " KEVIN:"
        print " So, you got it. Now let me ask you..."
        print " How should I call you?"
        Name = raw_input("==> ")
        print " " + Name + ":"
        print " I'm... " + Name + "."
        print " People call me " + Name + "..."
        XBucle = True
    elif Ans == "3":
        print " YOU:"
        print " I'm dead..."
        raw_input("")
        print " SOMEONE:"
        print " Yes, and I am Bill Gates."
        print " So, how should I call you, ghost? Casper???"
        Name = raw_input("==> ")
        print " " + Name + ":"
        print " I'm not Casper. I'm " + Name + "."
        raw_input("")
        print " SOMEONE:"
        print " Sorry, " + Name + ", I'm not Bill Gates too."
        raw_input("")
        print " SOMEONE:"
        print " I'm Kevin. I found you near the river, in the East."
        print " You were unconscious, so I let you in my house, inside the forest."
        XBucle = True
    else:
        print " SYSTEM:"
        print " I don't like what you are saying..."
        raw_input("")
        XBucle = False
XBucle = False
raw_input("")
print " " + Name + " and Kevin are in a bedroom of the house of Kevin."
print " The walls of the room are colored with blue colors."
print " " + Name + " is lying in the white bed. His backpack is placed in an empty desk wich have a classical lamp."
print " Kevin is sitting near " + Name + " in the same bed."
raw_input("")
print " " + Name + ":"
print " My backpack..."
raw_input("")
print " Kevin gived the Backpack to " + Name + "."
raw_input("")
print " " + Name + ":"
print " Wait."
raw_input("")
print " " + Name + ":"
print " I didn't have any backpack..."
raw_input("")
print " There is a tag with the name of someone in the backpack."
raw_input("")
print " KEVIN:"
print " Who is Broya?"
raw_input("")
print " " + Name + ":"
print " Broya..."
raw_input("")
print " " + Name + ":"
print " When you find me..."
raw_input("")
print " " + Name + ":"
print " ...I was alone?"
print " There aren't anyone more outside?"
raw_input("")
print " KEVIN:"
print " I didn't find any more than you and this backpack."
print " But..."
raw_input("")
print " KEVIN:"
print " Who is Broya???"
print ""
print " 1. Broya..."
print " 2. Broya..."
while (XBucle != True):
    Ans = raw_input("==> ")
    if Ans == "1":
        Genre = "Male"
        print " " + Name + ":"
        print " Broya..."
        print " Broya is my friend..."
        raw_input("")
        print " KEVIN:"
        print " He was with you?"
        raw_input("")
        print " " + Name + ":"
        print " Let me think..."
        raw_input("")
        print " " + Name + ":"
        print " Yes..."
        print " He was with me..."
        raw_input("")
        print " " + Name + ":"
        print " I must help him!!!"
        raw_input("")
        print " KEVIN:"
        print " (Stopping " + Name + ")"
        print " Not now!"
        raw_input("")
        print " KEVIN:"
        print " It's dark outside, and you aren't ready for the dangers."
        print " Too dangerous for you now..."
        raw_input("")
        print " " + Name + ":"
        print " ..."
        raw_input("")
        print " KEVIN:"
        print " You can search him tomorrow."
        print " He'll be ok..."
        raw_input("")
        print ""
        print " " + Name + " is sleeping, when a computer sound wake him..."
        print ""
        raw_input("")
        print ""
        print " " + Name + ":"
        print " What..."
        print " What's this?"
        raw_input("")
        print ""
        print " ..."
        raw_input("")
        print ""
        print " ..."
        raw_input("")
        print ""
        print " " + Name +":"
        print " What should I do now?"
        print ""
        print " 1. Ignore it and sleep."
        print " 2. Go and see what's up there."
        print " 3. Sing a song loudly."
        while (XBucle != True):
            Ans = raw_input("==> ")
            if Ans == "1":
                PlayerDream = True
                print ""
                print " " + Name + ":"
                print " I should be sleeping."
                print " I need energy to find Broya tomorrow..."
                raw_input("")
                print ""
                print " " + Name + " go back to the bed, and close his eyes."
                raw_input("")
                print "..."
                raw_input("")
                print "..."
                raw_input("")
                print "..."
                raw_input("")
                print ""
                print " KEVIN:"
                print " Uf..."
                raw_input("")
                print ""
                print " KEVIN:"
                print " This was close..."
                XBucle = True
            elif Ans == "2":
                PlayerDream = True
                print ""
                print " " + Name + ":"
                print " Hmm..."
                raw_input("")
                print ""
                print " " + Name + " go to take a look out there."
                print " What can be that sound?"
                raw_input("")
                print ""
                print " " + Name + " walk to the source of the sound."
                raw_input("")
                print ""
                print " The sound come from a computer."
                print " The computer is powered"
                raw_input("")
                print ""
                print " " + Name + " is in a dark room illuminated by the computer screen."
                print " There are normal things everywhere."
                raw_input("")
                print ""
                print " In the wall there is a big paper with the logo of a company."
                raw_input("")
                print ""
                print " " + Name + ":"
                print " 'NEXTMIND Laboratories'..."
                raw_input("")
                print ""
                print " " + Name + ":"
                print " I don't remember this name."
                print " Hmm..."
                raw_input("")
                print ""
                print " " + Name + " don't know what to do..."
                raw_input("")
                while (XBucle != True):
                    print ""
                    print " 1. See what's showing the screen."
                    print " 2. Open the drawer of the table."
                    print " 3. Turn on the lights."
                    print " 4. Go back to the bed."
                    Ans = raw_input("==> ")
                    if Ans == "1":
                        print ""
                        print " The screen shows a chat window."
                        raw_input("")
                        print ""
                        print " 1. Read it."
                        print " 2. Do nothing."
                        while (XBucle != True):
                            Ans = raw_input("==> ")
                            if Ans == "1":
                                PlayerDream = False
                                print ""
                                print " Marlo Rekreff (@Paco77)              [_] [ ] [x]"
                                print " ----------------------------------------------"
                                print " A FEW DAYS AGO"
                                print " @Paco77"
                                print " Look at this men!"
                                print " http://www.darutik.deviantart.com/"
                                print " He have great drawings and poems..."                 # Subliminal ad...
                                print ""
                                print " @KevinAFM"
                                print " Yeah, but I love more this one:"
                                print " http://www.kalexshi.deviantart.com/"
                                print " He drawed very well too... :("                          # R.I.P.  （；_・）
                                print ""
                                raw_input("")
                                print ""
                                print " TWO DAYS AGO"
                                print " @Paco77"
                                print " We have a few new subjects down here."
                                print ""
                                print " @KevinAFM"
                                print " Yes? What about they?"
                                print ""
                                print " @Paco77"
                                print " They are from the city."
                                print " Five homeless that NEXTMIND caught."
                                print ""
                                print " @KevinAFM"
                                print " What experiment are going to try with them?"
                                print " It's boring living here, alone..."
                                print ""
                                print " @Paco77"
                                print " Well, we are under maintenance, so they are on"
                                print " a cell waiting to the experiments."
                                print " Don't worry. Coming soon I'll visit you ;)"
                                print ""
                                print " @KevinAFM"
                                print " What would think our bosses about this chat?"
                                print ""
                                print " @Paco77"
                                print " Do you really think that they can think?"
                                print " The only brains who think down here are the"
                                print " scientifics' brains!"
                                raw_input("")
                                print " @KevinAFM"
                                print " Hahaha!"
                                print " Great one friend..."
                                print ""
                                print " @Paco77"
                                print " And you? What happens in the surface???"
                                print ""
                                print " @KevinAFM"
                                print " Nothing interesting..."
                                print " Only hunter and eating. And browsing some photos"
                                print " You know... ;)"
                                print ""
                                print " @Paco77"
                                print " Sorry, but I can't be online more."
                                print " My boss is calling me!"
                                print ""
                                print " YESTERDAY"
                                print " @Paco77"
                                print " Kevin, if you see someone arround there, caught them."
                                print " When we are testing with the second new subject, the"
                                print " other subjects escaped from the cell!"
                                print ""
                                print " @Paco77"
                                print " Kevin, please answer me as soon as posible..."
                                print ""
                                raw_input("")
                                print " 19 HOURS AGO"
                                print " @KevinAFM"
                                print " Sorry, I was hunting some food..."
                                print " So, they escaped from the hands of NEXTMIND?"
                                print ""
                                print " @Paco77"
                                print " Yes, they are two."
                                print " The third was fired by a security guard..."
                                print ""
                                print " @KevinAFM"
                                print " OK, then I'm going to look outside."
                                print " They will survive to the forest?"
                                print ""
                                print " ONE HOUR AGO"
                                print " @KevinAFM"
                                print " Hey, I found something!"
                                print " A man called " + Name + " in the forest."
                                print ""
                                print " @Paco77"
                                print " Sure? Let me search his name..."
                                print ""
                                print " @KevinAFM"
                                print " He was unconscious. He weared an empty bag"
                                print " with the name of Broya written in a tag."
                                print ""
                                print " @Paco77"
                                print " Broya?"
                                raw_input("")
                                print " @KevinAFM"
                                print " Yes. " + Name + " says that he doesn't remember"
                                print " him."
                                print " I don't know if " + Name + " is lying me or he's"
                                print " truly lost."
                                print ""
                                print " @Paco77"
                                print " Ok, I got " + Name + "'s history in my screen."
                                print " I'll look for Broya later. My boss is calling me"
                                print " again..."
                                print ""
                                print " @KevinAFM"
                                print " Well, then I'm going to keep " + Name + " here."
                                print " See you!"
                                print ""
                                raw_input("")
                                XBucle = True
                            elif Ans == "2":
                                print ""
                                print " " + Name + ":"
                                print " I'll not break his privacy..."
                                raw_input("")
                                XBucle = True
                            else:
                                print " SYSTEM:"
                                print " I don't like what you are saying..."
                                raw_input("")
                                XBucle = False
                        XBucle = False
                    elif Ans == "2":
                        print ""
                        print " " + Name + " open the drawer of the table."
                        raw_input("")
                        print " There is only a 'The Wall' album..."
                        raw_input("")
                        print " ..."
                        raw_input("")
                        print ""
                        print " Hey! Theres an ID Card too."
                        print ""
                        print " 1. Read it."
                        print " 2. Close the drawer."
                        while (XBucle != True):
                            Ans = raw_input("==> ")
                            if Ans == "1":
                                PlayerDream = False
                                print ""
                                print " NEXTMIND Laboratories"
                                print ""
                                print " Employee card!"
                                print ""
                                print " NAME:"
                                print " Kevin Reverguntter Lymphelt"
                                print ""
                                print " <There's a BIDI code at the bottom>"
                                raw_input("")
                                print " It will take you to more info about Kevin..."
                                raw_input("")
                                XBucle = True
                            elif Ans == "2":
                                print ""
                                print " " + Name + " close slowly the drawer."
                                raw_input("")
                                print ""
                                print " ...and nothing happened."
                                raw_input("")
                                XBucle = True
                            else:
                                print " SYSTEM:"
                                print " I don't like what you are saying..."
                                raw_input("")
                                XBucle = False
                        else:
                            print " SYSTEM:"
                            print " I don't like what you are saying..."
                            raw_input("")
                            XBucle = False
                    elif Ans == "3":
                        print ""
                        print " " + Name + " press the button on the wall."
                        raw_input("")
                        print " And the light become..."
                        raw_input("")
                        print ""
                        print " ..."
                        print ""
                        raw_input("")
                        print ""
                        print " ..."
                        print ""
                        raw_input("")
                        print ""
                        print " " + Name + " press the button on the wall again."
                        print " And the darkness came again to the room, broke by the screen..."
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " Consuming too much energy."
                        print " Think in the trees..."
                        raw_input("")
                        XBucle = False
                    elif Ans == "4":
                        print ""
                        print " " + Name + ":"
                        print " I should go to sleep..."
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " What will happen if Kevin sees me here?"
                        XBucle = True
                    else:
                        print " SYSTEM:"
                        print " I don't like what you are saying..."
                        raw_input("")
                        XBucle = False
                XBucle = True
            elif Ans == "3":
                PlayerDream = True
                print ""
                print " " + Name + ":"
                print " Para bailar la bamba!!!"
                raw_input("")
                print ""
                print " " + Name + ":"
                print " Para bailar la bamba!"
                print " Se necesita"
                print " Una poca de gracia!!!"
                raw_input("")
                print ""
                print " KEVIN:"
                print " Urg..."
                raw_input("")
                print ""
                print " " + Name + ":"
                print " Una poca de gracia!"
                print " Pa mi pa ti"
                print " Ay y arriba y arriba!!!"
                raw_input("")
                print ""
                print " KEVIN:"
                print " WTF?!!!"
                raw_input("")
                print ""
                print " " + Name + ":"
                print " Yo no soy marinero!!!"
                raw_input("")
                print ""
                print " KEVIN:"
                print " What are you doing???!"
                raw_input("")
                print ""
                print " " + Name + ":"
                print " Yo no soy marinero!"
                raw_input("")
                print ""
                print " KEVIN:"
                print " SHUT UP!!!"
                raw_input("")
                print ""
                print " " + Name + ":"
                print " ..."
                raw_input("")
                print ""
                print " KEVIN:"
                print " What you're thinking about?!!!"
                raw_input("")
                print ""
                print " 1. I can't sleep..."
                print " 2. You don't like 'La bamba'???"
                print " 3. I listened a sound..."
                while (XBucle != True):
                    Ans = raw_input("==> ")
                    if Ans == "1":
                        print ""
                        print " " + Name + ":"
                        print " I can't sleep..."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " What?"
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " Now you are a kid?"
                        raw_input("")
                        print " ..."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " Go back to the bed..."
                        print " Don't be a child..."
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " ..."
                        raw_input("")
                        print  ""
                        print " KEVIN:"
                        print " And " + Name + "..."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " If you are tired tomorrow, you will not be able to"
                        print " find Broya."
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " !!!"
                        XBucle = True
                    elif Ans == "2":
                        print ""
                        print " " + Name + ":"
                        print " You don't like 'La bamba'???"
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " No, I love 'La Bamba'."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " I only hate 'La Bamba' when someone sing it"
                        print " loudly at TWO O'CLOCK, AT NIGHT!"
                        raw_input("")
                        print ""
                        print " KEVIN looks angry."
                        raw_input("")
                        print ""
                        print " Suddenly, KEVIN target the Guest's Room of his house."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " Please, don't wake up at night again..."
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " Sorry..."
                        XBucle = True
                    elif Ans == "3":
                        print ""
                        print " " + Name + ":"
                        print " I listened a sound..."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " We are in the forest."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " There are hundreds of wild animals around us!"
                        print " Right now!!!"
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " ..."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " You should go back to bed."
                        print " And ignore the sounds from the outside."
                        XBucle = True
                    else:
                        print " SYSTEM:"
                        print " I don't like what you are saying..."
                        raw_input("")
                        XBucle = False
                XBucle = True
            else:
                print " SYSTEM:"
                print " I don't like what you are saying..."
                raw_input("")
                XBucle = False
        raw_input("")
        print ""
        raw_input("")
        print ""
        print " In the next day, " + Name + " and Kevin wake up."
        raw_input("")
        print ""
        print " As Kevin prepare the breakfast, " + Name + " wanted to ask somthing to him."
        raw_input("")
        print ""
        print " 1. What's out there, in the forest?"
        print " 2. Do you know how to touch a wall with an apple?"
        print " 3. Did you listen a strangle sound at night?"
        while (XBucle != True):
            Ans = raw_input("==> ")
            if Ans == "1":
                print ""
                print " " + Name + ":"
                print " What's out there, in the forest?"
                raw_input("")
                print ""
                print " KEVIN:"
                print " Well..."
                raw_input("")
                print ""
                print " KEVIN:"
                print " Do you know what kind of animals usually are on the forest?"
                print ""
                print " 1. Yes"
                print " 2. No"
                print " 3. Don't press the '3' button..."
                while (XBucle != True):
                    Ans = raw_input("==> ")
                    if Ans == "1":
                        print ""
                        print " " + Name + ":"
                        print " Yes, I know a bit about animals and these things."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " Well."
                        print " Then..."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " Then forgot what you should see at a forest."
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " What?"
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " Why..."
                        print " ?"
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " Well, this is not a regullar forest."
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " So, this is a irregular forest, ah?"
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " You can call it... 'amazing'"
                        raw_input("")
                        XBucle = True
                    elif Ans == "2":
                        print ""
                        print " " + Name + ":"
                        print " No, I'm an absolutely noob in these topics..."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " Well, so..."
                        print " Are you hard?"
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " I'm a city man..."
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " ..."
                        raw_input("")
                        print ""
                        print " " + Name + ":"
                        print " Not too hard at all"
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " Hmm..."
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " How can I explain you...?"
                        raw_input("")
                        print ""
                        print " KEVIN:"
                        print " ..."
                        raw_input("")
                        XBucle = True
                    elif Ans == "3":
                        print ""
                        print " SYSTEM:"
                        print " I told you that you cannot do that."
                        raw_input("")
                        print " You are an stupid thing..."
                        raw_input("")
                        XBucle = False
                    else:
                        print " SYSTEM:"
                        print " I don't like what you are saying..."
                        raw_input("")
                        XBucle = False
                print ""
                print " KEVIN:"
                print " Anyway, you should be prepared for your search"
                XBucle = True
            elif Ans == "2":
                print ""
                print " " + Name + ":"
                print " Do you know how to touch a wall with an apple?"
                raw_input("")
                print ""
                print " KEVIN:"
                print " I watched the video too..."
                raw_input("")
                print ""
                print " " + Name + ":"
                print " But you know how to do it with any color???"
                raw_input("")
                print ""
                print " KEVIN:"
                print " Yes..."
                raw_input("")
                print ""
                print " " + Name + ":"
                print " ..."
                raw_input("")
                XBucle = True
            elif Ans == "3":
                print ""
                print " " + Name + ":"
                print " Did you listen a strangle sound at night?"
                raw_input("")
                print ""
                print " KEVIN:"
                print " No..."
                raw_input("")
                if PlayerDream == True:
                    print ""
                    print " KEVIN:"
                    print " I was with the computer until midnight, and I didn't hear anything..."
                    print ""
                    print " 1. Computer?"
                    print " 2. Headphones..."
                    while (XBucle != True):
                        Ans = raw_input("==> ")
                        if Ans == "1":
                            print ""
                            print " " + Name + ":"
                            print " Do you have a computer?"
                            raw_input("")
                            print ""
                            print " " + Name + ":"
                            print " Here???"
                            raw_input("")
                            print ""
                            print " KEVIN:"
                            print " Err... yes..."
                            raw_input("")
                            print ""
                            print " KEVIN:"
                            print " No?"
                            raw_input("")
                            print ""
                            print " " + Name + ":"
                            print " Can you let me check my Twitter? Facebook? VK? Last.fm? My Space?"
                            print " YouTube? deviantART? GitHub? TaikoTime? Furaffinity? Google+?"
                            print " Yo? Steam? Skype? Whatsapp? Line? Telegram? Twitch?"
                            raw_input("")
                            print ""
                            print " KEVIN:"
                            print " ¬ ¬"
                            raw_input("")
                            print ""
                            print " " + Name + ":"
                            print " No?"
                            raw_input("")
                            print ""
                            print " KEVIN:"
                            print " ..."
                            raw_input("")
                            print ""
                            print " KEVIN:"
                            print " No"
                            raw_input("")
                            print ""
                            print " " + Name + ":"
                            print " ..."
                            raw_input("")
                            print ""
                            print " " + Name + ":"
                            print " Forget it..."
                            raw_input("")
                            XBucle = True
                        elif Ans == "2":
                            print ""
                            print " " + Name + ":"
                            print " Headphones..."
                            raw_input("")
                            print ""
                            print " KEVIN:"
                            print " Nani?"
                            raw_input("")
                            print ""
                            print " " + Name + ":"
                            print " I mean, you were listening to music, do you?"
                            raw_input("")
                            print ""
                            print " " + Name + ":"
                            print " Technologyc?" #Daft Punk
                            print " Seirogan2000?" #Taiko no Tatsujin!
                            print " Hungarian Rhapsody No.2?" #Better with stepped motors xD
                            print " The Wall?" #Pink Floyd
                            raw_input("")
                            print ""
                            print " KEVIN:"
                            print " I hate The Wall!"
                            raw_input("")
                            print ""
                            print " 1. But you have it!" #Die, player..
                            print " 2. I hate it too" #False xD It's awesome!
                            print " 3. It's the best album EVER!" #and Alive2007
                            while (XBucle != True):
                                Ans = raw_input("==> ")
                                if Ans == "1":
                                    print ""
                                    print " " + Name + ":"
                                    print " But you have it!"
                                    raw_input("")
                                    print ""
                                    print " KEVIN:"
                                    print " What?"
                                    raw_input("")
                                    print ""
                                    print " " + Name + ":"
                                    print " You have 'The Wall' on your Drawer"
                                    raw_input("")
                                    print ""
                                    print " Kevin looks upset, thinking about something fast..."
                                    raw_input("")
                                    print ""
                                    print " " + Name + ":"
                                    print " Are you listening to-"
                                    raw_input("")
                                    print ""
                                    print " But " + Name + " never finished that sentence..."
                                    raw_input("")
                                    print ""
                                    print " Kevin triggered his sleeping gun before " + Name + "'s brain noticed that"
                                    print " Kevin was with a hand near his waist, were that gun was."
                                    raw_input("")
                                    print ""
                                    print " And " + Name + " fell down to the floor, while Kevin was pressing"
                                    print " some buttons on his phone."
                                    raw_input("")
                                    print ""
                                    print " KEVIN:"
                                    print " Marlo! I..."
                                    raw_input("")
                                    raw_input("")
                                    raw_input("")
                                    print " end"
                                    raw_input("")
                                    print " ?"
                                    raw_input("")
                                    XBucle = True
                                    sys.exit()
                                elif Ans == "2":
                                    print ""
                                    print " " + Name + ":"
                                    print " Well, I hate it too..."
                                    raw_input("")
                                    print ""
                                    
                                    XBucle = True
                                elif Ans == "3":
                                    print ""
                                    print " " + Name + ":"
                                    print " How you can say that???"
                                    raw_input("")
                                    print ""
                                    print " " + Name + ":"
                                    print " It's the best album EVER!!!"
                                    print " <3" #xD
                                    XBucle = True
                                else:
                                    print " SYSTEM:"
                                    print " I don't like what you are saying..."
                                    raw_input("")
                                    XBucle = False
                            XBucle = True
                        else:
                            print " SYSTEM:"
                            print " I don't like what you are saying..."
                            raw_input("")
                            XBucle = False
                elif PlayerDream == False:
                    print ""
                else:
                    print "/*/ERROR/*/"
                    raw_input("")
                XBucle = True
            else:
                print " SYSTEM:"
                print " I don't like what you are saying..."
                raw_input("")
                XBucle = False
        print ""
        print " KEVIN:"
        print " So, in two hours your're gonna be at the forest"
        raw_input("")
        print ""
        print " KEVIN:"
        print " Alone"
        raw_input("")
        XBucle = True
    elif Ans == "2":
        Genre = "Female"
        print " " + Name + ":"
        print " Broya.."
        print " Broya is my partner..."
        raw_input("")
        print " KEVIN:"
        print " Your partner???"
        print " You mean your journey partner, no?"
        raw_input("")
        print " " + Name + ":"
        print " I supose..."
        print " I only know that I have this word recorded on my mind..."
        raw_input("")
        print ""
        print " " + Name + ":"
        print " her name..."
        XBucle = True
    else:
        print " SYSTEM:"
        print " I don't like what you are saying..."
        raw_input("")
        XBucle = False
XBucle = False
raw_input("")
print "DEADLINE"
print "The code ends here..."
raw_input("")
