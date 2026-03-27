s1= 'Thirty'
s2= 'Days'
s3= 'Of'
s4= 'Python'
sf= s1 + ' ' + s2 + ' ' + s3 + ' ' + s4
print(sf)

ss1= 'Coding'
ss2= 'For'
ss3= 'All'
ssf= ss1 + ' ' + ss2 + ' ' + ss3
print(ssf)

company= 'Coding For All'
print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase()) 

pal = company.split()
cortado = ' '.join(pal[1:])
print(cortado)

ora= 'Coding For All'
ss='Coding'
print(ora.index(ss))

print(ora.replace('Coding', 'Python'))

ora2= 'Python For Everyone'
print(ora2.replace('Everyone', 'All'))

print(ora.split()) 

ora3= 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(ora3.split(', ')) 

print(ora[0]) 
print(ora[-1]) 
print(ora[10]) 


a1= 'Python For Everyone'
lala= a1.split()
abb= ''.join(lala[0] for lala in a1.split())
print(abb)

a2= 'Coding For All'
lala2= a2.split()
abb2= ''.join(lala2[0] for lala2 in a2.split())
print(abb2)


l='C'
print(ora.index(l))

n='F'
print(ora.index(n)) 

ora4= 'Coding For All People'
print(ora4.rfind('l')) 

ora5= 'You cannot end a sentence with because because because is a conjunction'

print(ora5.find('because')) 

print(ora5.rindex('because'))

#25 
pall=ora5.split()
ress=' '.join(pall[6:9])
print(ress) 

print(ora5.find('because')) 

pal2=ora5.split()
ress=' '.join(pall[6:9])
print(ress) 

#27
print(ora.startswith('Coding'))

print(ora.endswith('coding')) 

print('   Coding For All      '.strip()) 

ola= '30 Days Of Python'
print(ola.isidentifier()) 
ola2= 'thirty_days_of_python'
print(ola2.isidentifier()) 

ola3=['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result= '# '.join(ola3) 
print(result)

ola4 = 'I am enjoying this challenge.'  
print(ola4.split())
ola5= 'i just wonder what is next.'
print(ola5.split())

ora6='Name\tAge\tCountry\tCity'   
ora7= 'Asabeneh\t250\tFinland\tHelsinki'
print(ora6.expandtabs(10))
print(ora7.expandtabs(10))

radius= 10
area= 3.14 * radius ** 2  
print(f'El área de un círculo con radio {radius} es: {area}')

a=8
b=6
print(f'{a}+{b}={a+b}\n{a}-{b}={a-b}\n{a}{b}={a*b}\n{a}/{b}={a/b:.2f}\n{a}%{b}={a%b}\n{a}{b}={a*b}') *