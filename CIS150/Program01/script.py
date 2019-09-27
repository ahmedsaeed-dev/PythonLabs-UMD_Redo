print('Welcome to the Calculation Program')
firstName = input('Please enter your first name: ')

intNumberOne, intNumberTwo = [int(x) for x in input('Please enter two integer values: ').split()]
print('{} + {} = {}'.format(intNumberOne, intNumberTwo, int((intNumberOne + intNumberTwo))))
print('{} - {} = {}'.format(intNumberOne, intNumberTwo, int((intNumberOne - intNumberTwo))))
print('{} * {} = {}'.format(intNumberOne, intNumberTwo, int((intNumberOne * intNumberTwo))))
print('{} / {} = {}'.format(intNumberOne, intNumberTwo, int((intNumberOne / intNumberTwo))))
print('{} % {} = {}'.format(intNumberOne, intNumberTwo, int((intNumberOne % intNumberTwo))))

floatNumberOne, floatNumberTwo = [float(x) for x in input('Please enter two real values: ').split()]
print('{} + {} = {}'.format(floatNumberOne, floatNumberTwo, float((floatNumberOne + floatNumberTwo))))
print('{} - {} = {}'.format(floatNumberOne, floatNumberTwo, float((floatNumberOne - floatNumberTwo))))
print('{} * {} = {}'.format(floatNumberOne, floatNumberTwo, float((floatNumberOne * floatNumberTwo))))
print('{} / {} = {}'.format(floatNumberOne, floatNumberTwo, float((floatNumberOne / floatNumberTwo))))
print('{} % {} = {}'.format(floatNumberOne, floatNumberTwo, float((floatNumberOne % floatNumberTwo))))

print('{}, thank you for using the program written by Ahmed.'.format(firstName))
