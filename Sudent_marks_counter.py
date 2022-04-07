# Sudent_marks counter 
#copyright of this code has Abdirizak abdullahi hussein 

def Student_marks():
    i = 0
    limit = 3
    
    while i < limit:
        print('Enter the Sudent_marks')
        Math = int(input('Math_marks'))
        English = int(input('English_marks'))
        Arabic = int(input('Arabic_marks'))
        sum = (Math + English + Arabic)
        print('TOTAL =', sum)
        average = (sum / 3)
        print('average =', average)
        if average >= 95:
            print('High-level', 'Passed')
        elif average > 52:
            print('Passed')
        else:
            print('Failed')
        i += 1
Student_marks()
