message = input('>')
message1=message.split(" ")
#split the message and save as a list
emojis={
    ':)':'😊',
    ':(':'😥',
   
}
output=''
for i in message1:
    output += emojis.get(i,i)+" "
print(output)
#############################################
def emj(message):
        message1 = message.split(" ")
        # split the message and save as a list
        emojis = {
            ':)': '😊',
            ':(': '😥',
        }
        output = ''
        for i in message1:
            output += emojis.get(i, i) + " "
        print(output)
message = input('>')
emj(message)
