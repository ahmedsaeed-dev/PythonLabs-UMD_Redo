print('Welcome to the Inventory Calculation Program')
productName = input('Enter product name: ')
productQuantity = int(input('Enter product quantity: '))
productUnitPrice = float(input('Enter product unit price: '))
productTotalPrice = productQuantity * productUnitPrice

print('{:<13} {:<13} {}'.format('Product', 'Quantity', 'Unit Price ($)'))
print('{:<13} {:<13} {}'.format(productName, productQuantity, productUnitPrice))
print('The total price is ${0:.2f}'.format(productTotalPrice))