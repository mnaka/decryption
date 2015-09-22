import sys

#f = open('twelve.txt', 'r')
f = open('thirteen.txt', 'r')

text = f.read().lower().split()
for i in range(0,len(text)):
    text[i] = text[i].replace(",","");
out = open("output.txt", "w")

def search_twelve (keyword):


    for loopnumber in range(0,len(keyword)):
        #print loopnumber;
        a = "a";
        b = "b";
        c = "c";
        d = "d";
        e = "e";
        f = "f";
        g = "g";
        h = "h";
        i = "i";
        j = "j";
        k = "k";
        l = "l";
        m = "m";
        n = "n";
        o = "o";
        p = "p";
        q = "q";
        r = "r";
        s = "s";
        t = "t";
        u = "u";
        v = "v";
        w = "w";
        x = "x";
        y = "y";
        z = "z";

        word = "szzekliyfjqf"
        #print len(word)
        #for check in range(0,12):
        #    print keyword[loopnumber][check];

        s = keyword[loopnumber][0].upper()
        z = keyword[loopnumber][1].upper()
        z = keyword[loopnumber][2].upper()
        e = keyword[loopnumber][3].upper()
        k = keyword[loopnumber][4].upper()
        l = keyword[loopnumber][5].upper()
        i = keyword[loopnumber][6].upper()
        y = keyword[loopnumber][7].upper()
        f = keyword[loopnumber][8].upper()
        j = keyword[loopnumber][9].upper()
        q = keyword[loopnumber][10].upper()
        f = keyword[loopnumber][11].upper()

        word2 = word;
        word2 = word2.replace("s",s);
        word2 = word2.replace("z",z);
        word2 = word2.replace("e",e);
        word2 = word2.replace("k",k);
        word2 = word2.replace("l",l);
        word2 = word2.replace("i",i);
        word2 = word2.replace("y",y);
        word2 = word2.replace("f",f);
        word2 = word2.replace("j",j);
        word2 = word2.replace("q",q);
        #print keyword[loopnumber];
        if(word2.lower() == keyword[loopnumber]):
            code = "pjq kefp yklexpsvp lxelqxpb em s lxerxsk yf gjqpjqx yp szzekliyfjqf pjq yvpqvpyev em ypf cfqx. - z.s.x. jesxq"
            code = code.replace("s",s);
            code = code.replace("z",z);
            code = code.replace("e",e);
            code = code.replace("k",k);
            code = code.replace("l",l);
            code = code.replace("i",i);
            code = code.replace("y",y);
            code = code.replace("f",f);
            code = code.replace("j",j);
            code = code.replace("q",q);

            #assume p = T
            code = code.replace("p","T");
            #assume x = R
            #assume v = N
            code = code.replace("x","R");
            code = code.replace("v","N");
            #assume b = Y
            code = code.replace("b","Y");
            #assume r = G
            code = code.replace("r","G");
            code = code.replace("g","W");
            code = code.replace("m","F");
            code = code.replace("c","U");

            out.write(keyword[loopnumber] + "\n");
            out.write(code + "\n \n");
search_twelve(text)
