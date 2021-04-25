import argparse
import itertools
import os
parser = argparse.ArgumentParser()
parser.add_argument('-f', dest="path", required=False,help="select the wordlist for capitalise")
parser.add_argument('-fname', dest="fname",help="First name ex : -fname hayley)")
parser.add_argument('-mname', dest="mname",help="MIddlename ex: -mname marhsall ")
parser.add_argument('-lname', dest="lname",help="Lastname ex -lname drew")
parser.add_argument('-n', dest="number",help="use -n for numbers that will be requested later " ,action="store_true")
parser.add_argument('-r', dest="remove",help="using this will remove peviously generated list by this script" ,action="store_true")

Nlist = []
args = parser.parse_args()
f_name=args.fname
m_name = args.mname
l_name = args.lname
location_path = args.path
clk = 0
if args.remove:
    if os.path.exists("alphanumeric_wordlist.txt"):
        os.remove("alphanumeric_wordlist.txt")
    elif os.path.exists("NEW_Wordlist.txt"):    
        os.remove("NEW_Wordlist.txt")
    elif os.path.exists("alpha_wordlist.txt"):    
        os.remove("alpha_wordlist.txt")

def capitalise():
    if args.path:
        P_list = open(location_path, "r").readlines()
        for i in P_list :
                x = open("NEW_Wordlist.txt","a")
                x.write(i.title())
#  capitalise given name


def name(F,M,L):
    Flist = []
    Mlist = []
    Llist = []
    if args.fname:
        Flist.append(F)
        if F != F.title():
            Flist.append(F.title())
    for place in Flist:
        Nlist.append(place)
    if args.mname:
        Mlist.append(M)
        if M != M.title():  
            Mlist.append(M.title())
    if args.lname:
        Llist.append(L)    
        if L != L.title():
            Llist.append(L.title())

# input has middle names , lastname
    if args.mname and args.lname:
        print("all")
        for (item1,item2,item3) in zip(Flist,Mlist,Llist):
            for m in Mlist:
                for name in Llist:
                    Nlist.append(item1+m+name)  
                    # firstname+middlename+lastname
#input has lname             
    if args.lname:
            print(args.lname)
            for(item1,item2) in zip(Flist,Llist):
                for i in Llist:
                    Nlist.append(item1+i) # firstname + lastname


    
    with open("alpha_wordlist.txt" , "a") as apl:
            for letters in Nlist:
                apl.write("%s\n" %letters)
            if args.fname:
                print("done with",len(Nlist),"lines in alpha_wordlist ")
            

def list_numbers(chrs,n):
    
    for i in range(1,n+1):
        for xs in itertools.product(chrs, repeat=i):
            for word in Nlist:
                global clk
                clk+=1
                Alpha_numeric = open("alphanumeric_wordlist.txt" , "a")
                Alpha_numeric.write(word+"".join(xs)+"\n")
    print("done with",clk,"lines in alphanumeric_wordlist")

name(f_name,m_name,l_name)

while (args.number):
    digit = input("[+] enter required numbers without space: ")
    n = int(input("[+] enter number of combination: "))
    list_numbers(digit,n)
    exit(0)

if args.path:
    capitalise()
