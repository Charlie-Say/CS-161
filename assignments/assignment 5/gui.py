from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename


def initiate_encrypt():
    # button to encrypt file for user provided key
    infilename = askopenfilename()
    open_file = open(infilename, "r")
    read_file = open_file.read()
    text_box_input = int(key_text.get())
    alphabet_map = ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV')
    outfilename = asksaveasfilename()
    write_file = open(outfilename, "w")
    smol_brain_list = list(read_file)

    for i in range(len(smol_brain_list)):
    # this loop shifts the characters in smol_brain_list, according to the key
        if smol_brain_list[i] in alphabet_map:
            alphabet_pos = alphabet_map.find(smol_brain_list[i])
            smol_brain_list[i] = alphabet_map[alphabet_pos + text_box_input]

    print(''.join(smol_brain_list), file=write_file)
    open_file.close()
    write_file.close()


window = Tk()
window.title("Hail Caesar")
window.geometry('450x250')

heading = Label(window, text="CS 161 \n This program will take in a key and shift the characters\n"
                "in the document according to the key. \n You will be prompted to open the file and then \n"
                "save the file.")
heading.pack()

key_text = Entry(window,width=10)
key_text.pack()

Label(window, text="Enter a Key").pack()
btn_1 = Button(window, text="Initiate", command=initiate_encrypt)
btn_1.pack()



window.mainloop()