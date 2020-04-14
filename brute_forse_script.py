from urllib.request import urlopen, hashlib

print('''
 mmmmm                  m           mmmmmm                                   
 #    #  m mm  m   m  mm#mm   mmm   #       mmm    m mm   mmm    mmm         
 #mmmm"  #"  " #   #    #    #"  #  #mmmmm #" "#   #"  " #"  "  #"  #        
 #    #  #     #   #    #    #""""  #      #   #   #     #      #""""        
 #mmmm"  #     "mm"#    "mm  "#mm"  #      "#m#"   #     "#mm"  "#mm"        
                                                                             
                                                                             
                                                                             
  mmmm  m    m   mm   mmm                                                    
 #"   " #    #   ##     #                                                    
 "#mmm  #mmmm#  #  #    #                                                    
     "# #    #  #mm#    #                                                    
 "mmm#" #    # #    # mm#mm  by WamGleb\n ''')

sha1hash = input("Введите ваш хэшь для его взлома:\n>")
list_of_common_ps =str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt').read(), 'utf-8')

for guess in list_of_common_ps.split('\n'):
    hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
    if hashedGuess == sha1hash:
        print("Ваш пароль: ", str(guess))
        quit()
    elif hashedGuess != sha1hash:
        print("Пароль ", str(guess), " не совпадает, попробуйте следующий...")
print("Пароля нет в базах данных, мы это исправим в следующих обновлениях")



