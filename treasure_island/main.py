print('''
  ..oo$00ooo..                    ..ooo00$oo..
                .o$$$$$$$$$'                          '$$$$$$$$$o.
             .o$$$$$$$$$"             .   .              "$$$$$$$$$o.
           .o$$$$$$$$$$~             /$   $\              ~$$$$$$$$$$o.
         .{$$$$$$$$$$$.              $\___/$               .$$$$$$$$$$$}.
        o$$$$$$$$$$$$8              .$$$$$$$.               8$$$$$$$$$$$$o
       $$$$$$$$$$$$$$$              $$$$$$$$$               $$$$$$$$$$$$$$$
      o$$$$$$$$$$$$$$$.             o$$$$$$$o              .$$$$$$$$$$$$$$$o
      $$$$$$$$$$$$$$$$$.           o{$$$$$$$}o            .$$$$$$$$$$$$$$$$$
     ^$$$$$$$$$$$$$$$$$$.         J$$$$$$$$$$$L          .$$$$$$$$$$$$$$$$$$^
     !$$$$$$$$$$$$$$$$$$$$oo..oo$$$$$$$$$$$$$$$$$oo..oo$$$$$$$$$$$$$$$$$$$$$!
     {$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$}
     6$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$?
     '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
      o$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$o
       $$$$$$$$$$$$$$;'~`^Y$$$7^''o$$$$$$$$$$$o''^Y$$$7^`~';$$$$$$$$$$$$$$$
       '$$$$$$$$$$$'       `$'    `'$$$$$$$$$'     `$'       '$$$$$$$$$$$$'
        !$$$$$$$$$7         !       '$$$$$$$'       !         V$$$$$$$$$!
         ^o$$$$$$!                   '$$$$$'                   !$$$$$$o^
           ^$$$$$"                    $$$$$                    "$$$$$^
             'o$$$`                   ^$$$'                   '$$$o'
               ~$$$.                   $$$.                  .$$$~
                 '$;.                  `$'                  .;$'
                    '.                  !                  .`
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
user = input('Where do you want to go? left or right\n ').lower()
if user == 'left':
  second = input('''A door opened and you went there. After a long way, there is a river. Do you want to swim or do you want to 
    wait for a boat? Type 'swim' or 'wait' \n''').lower()
  if second == 'wait':
    color = input('''A boat came and took you to a castle. The castle gate opened and you went in. There are 4 doors which are painted Blue, Green, Pink and Red. Which one do you choose? \n''').lower()
    if color == "blue":
      print('A beast came and ate you! Game over!')
    elif color == 'red':
      print('You entered and there was a fire. You were burnt alive. Game over!')
    elif color == 'yellow':
      print("Congrats! Let's fight crime together! You won")
    else:
      print('You died of heart attack. Game over!')
      

  else:
    print('You were eaten by a shark. Game over! :-(')
else:
  print('You fell into a hole. Game Over!')
  
