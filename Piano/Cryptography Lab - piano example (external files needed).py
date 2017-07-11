import winsound

# Play Windows exit sound.
def main(l):
    x = input('put in a note: ')
    list = l
    notes = ['a4', 'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'c5', 'p_a', 'p_b', 'p_bb', 'p_c']
    if x == 'fin':
           play(list)
           return
    elif x not in notes:
            print("not a valid note")
            main(list)
    else:
        list += [x]
    main(list)
    

def play(list):
    for i in list:
        winsound.PlaySound(i, winsound.SND_FILENAME)
    

main([])
