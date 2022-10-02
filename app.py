import sys
command = ''
note_count = 0
note_value = 0

print('\33[94m')

while command == '':
    print('''
    ==================================================
             Welcome to the money counter
    ==================================================

            Please enter the amount of notes
    ''')
    note_count = int(input('--> '))

    print('''
    ==================================================
           Please enter the value of notes
    ==================================================
    ''')
    note_value = int(input('--> '))

    output = f'''\33[92m
                          Calculation Results
    =================================================================
       You have {note_count:,d} notes, In total are\33[93m {note_value * note_count:,d}\33[92m
    =================================================================
    '''
    print(output)

    print('''
    \33[94m
    =================================================================
                If you want to stop the program enter \33[93m'Quit'\33[94m
                If not, Just click \33[93menter\33[94m
    =================================================================
    ''')

    command = input('--> ').lower()
    if command == 'quit':
        print('''
        \33[91m
        =================================================================
                          The program has stopped running
        =================================================================
        ''')
        command = 'quit'
    else:
        command = ''
