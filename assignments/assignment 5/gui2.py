from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


def initiate_encrypt():
    # button to encrypt file for user provided key
    infilename = askopenfilename()
    open_file = open(infilename, "r")
    read_file = open_file.read()
    text_box_input = int(key_text.get())
    
    outfilename = asksaveasfilename()
    write_file = open(outfilename, "w")
    smol_list = list(read_file)
        

    for i in range(len(smol_list)):

        smol_list[i] = ord(smol_list[i])

        if 65 <= smol_list[i] <= 90:
            if (smol_list[i] + text_box_input) <= 90:
                smol_list[i] = smol_list[i] + text_box_input
            elif (smol_list[i] + text_box_input) > 90:
                smol_list[i] = 65 + ((smol_list[i] + text_box_input) - 90)

        elif 97 <= smol_list[i] <= 122:
            if (smol_list[i] + text_box_input) <= 122:
                smol_list[i] = smol_list[i] + text_box_input
            elif (smol_list[i] + text_box_input) > 122:
                smol_list[i] = 97 + ((smol_list[i] + text_box_input) - 122)

    for number in range(len(smol_list)):
           smol_list[number] = chr(smol_list[number])

    print(''.join(smol_list), file=write_file)
    
    open_file.close()
    write_file.close()





window = Tk()
window.title("Hail Caesar")
window.geometry('450x250')

heading = Label(window, text="CS 161 - Caesar Cypher \n \n This program will"
                            "take in a text and shift the characters \n"
                            "in the document according to the key. \n"
                            "You will be prompted to open the file and then \n"
                            "save the file. \n")
heading.pack()

key_text = Entry(window,width=10)
key_text.pack()

Label(window, text="Enter a Key \n \n").pack()
btn_1 = Button(window, bd=5, text="Initiate Program", command=initiate_encrypt)
btn_1.pack()



window.mainloop()