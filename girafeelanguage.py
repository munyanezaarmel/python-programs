def translate(phase):
 translation=''
for word in phase:
    if word in 'AEIUOaeiuo':
        translation=translation+'g'
else:
        translation=translation+word
return translation
print(translate(input("Enter a phrase")))

