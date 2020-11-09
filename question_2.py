def common_letter(t):

    #convert int to array
    text = t.lower();

    a=0;b=0;c=0;d=0;e=0;f=0;g=0;h=0;i=0;j=0;k=0;l=0;m=0;n=0;o=0;p=0;q=0;r=0;s=0;t=0;u=0;v=0;w=0;x=0;y=0;z=0;

    a = text.count('a');
    b = text.count('b');
    c = text.count('c');
    d = text.count('d');
    e = text.count('e');
    f = text.count('f');
    g = text.count('g');
    h = text.count('h');
    i = text.count('i');
    j = text.count('j');
    k = text.count('k');
    l = text.count('l');
    m = text.count('m');
    n = text.count('n');
    o = text.count('o');
    p = text.count('p');
    q = text.count('q');
    r = text.count('r');
    s = text.count('s');
    t = text.count('t');
    u = text.count('u');
    v = text.count('v');
    w = text.count('w');
    x = text.count('x');
    y = text.count('y');
    z = text.count('z');


    al={
        'a':a,
        'b':b,
        'c':c,
        'd':d,
        'e':e,
        'f':f,
        'g':g,
        'h':h,
        'i':i,
        'j':j,
        'k':k,
        'l':l,
        'm':m,
        'n':n,
        'o':o,
        'p':p,
        'q':q,
        'r':r,
        's':s,
        't':t,
        'u':u,
        'v':v,
        'w':w,
        'x':x,
        'y':y,
        'z':z

        
    }
    sorted(al);
   #for key, value in al.items():
        #print(key, ' : ', value)
    key = list(al.keys())[0] 
    val = list(al.values())[0] 
    print(al);


        
common_letter("hello");
