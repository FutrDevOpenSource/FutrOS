import os

print ("""
  ███████╗██╗░░░██╗████████╗██████╗░  ░█████╗░░██████╗
    ██╔════╝██║░░░██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝
    █████╗░░██║░░░██║░░░██║░░░██████╔╝  ██║░░██║╚█████╗░
    ██╔══╝░░██║░░░██║░░░██║░░░██╔══██╗  ██║░░██║░╚═══██╗
    ██║░░░░░╚██████╔╝░░░██║░░░██║░░██║  ╚█████╔╝██████╔╝
    ╚═╝░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░╚═════╝░   BETA 1.0
""")

print (""" 
[1] Continue with setup
[2] I've already done setup
""")

setup = input ("[?]:")
if setup == '1':
        name = input(str("Please enter your username to be displayed:"))
        pas  = input(str("Please enter your Password to login:"))


        with open('username.txt' , 'w') as f:
            f.write(name)

print ("[1] About \n©2021 FutrDev 2021. All rights reserved. ")
setup = input ("[?]:")

if setup ==  '1':
        print ("""   
    ╔═══╦╗───────╔╗     
    ║╔═╗║║──────╔╝╚╗
    ║║─║║╚═╦══╦╗╠╗╔╝
    ║╚═╝║╔╗║╔╗║║║║║
    ║╔═╗║╚╝║╚╝║╚╝║╚╗
    ╚╝─╚╩══╩══╩══╩═╝
        
        


    ███████╗██╗░░░██╗████████╗██████╗░  ░█████╗░░██████╗
    ██╔════╝██║░░░██║╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝
    █████╗░░██║░░░██║░░░██║░░░██████╔╝  ██║░░██║╚█████╗░
    ██╔══╝░░██║░░░██║░░░██║░░░██╔══██╗  ██║░░██║░╚═══██╗
    ██║░░░░░╚██████╔╝░░░██║░░░██║░░██║  ╚█████╔╝██████╔╝
    ╚═╝░░░░░░╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ░╚════╝░╚═════╝░
    Version 2.1 
    ©2021 FutrDev. This is a liscenced and authentic version of 
    FutrOS.  if you have any questions or want to report bugs go to:
    www.futrdev.wixiste.com/home and Contact Us. 

    """)

if setup ==  'awesome':
        print ("""

╔══╦╗──────╔╗────────╔╗──────────────────────────╔╗───╔╗─────────╔╗
╚╗╔╣╚╦═╗╔═╦╣╠╗╔╦╦═╦╦╗║╚╦═╗╔═╦═╦═╦═╦╦╦╦╦═╦═╦╦═╗╔╦╦╣╚╦═╗║╚╦═╦╗╔═╦═╦╝║
─║║║║║╬╚╣║║║═╣║║║╬║║║║╔╣╬║║╩╬╗║╔╣╩╣╔╣║║╬║║║║╩╣║║║║║║╬║║║║╩╣╚╣╬║╩╣╬║
─╚╝╚╩╩══╩╩═╩╩╝╠╗╠═╩═╝╚═╩═╝╚═╝╚═╝╚═╩╝╠╗╠═╩╩═╩═╝╚══╩╩╩═╝╚╩╩═╩═╣╔╩═╩═╝
──────────────╚═╝───────────────────╚═╝─────────────────────╚╝
─────╔╗──╔══╗╔╗──╔═╦══╗
╔═╦═╦╝╠═╗║═╦╬╣╚╦╦╣║║══╣
║═╣╬║╬║╩╣║╔╣║║╔╣╔╣║╠══║
╚═╩═╩═╩═╝╚╝╚═╩═╩╝╚═╩══╝

               """)

if setup ==  '!beta':
        print ("""         

This is a beta version of FutrOS

               """)

if setup ==  '!help':
        print ("""         
If you have questions or need help navigating FutrOS contact us with our website: https://bit.ly/contactusfutros  """)