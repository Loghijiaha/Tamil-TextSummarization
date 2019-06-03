
from tkinter import *
from tkinter import  messagebox
from tkinter.filedialog import askopenfilename
import  shutil,os
from text_segmentation import split_into_sentences
from cosine_similarity import cosineVal
from Genertae_Summary import train

def addMain():
    cwd = os.getcwd()
    filename_src = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    shutil.copy(filename_src, cwd + "/Input_file")
    e1.insert(20,filename_src)
def addSec():
    filename_src = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    e2.insert(20,filename_src)
def addSup():
    filename_src = askopenfilename()  # show an "Open" dialog box and return the path to the selected file
    e3.insert(20,filename_src)
def predict():
    cwd=os.getcwd()
    filename=os.listdir(cwd + "/Input_file")[0]
    # file = open(cwd + "/Input_file/"+filename, 'r')
    # text = file.read()
    # file.close();
    extracted =train(filename)
    shutil.move(os.path.join(cwd + "/Input_file",filename),os.path.join(cwd + "/data",filename))

    file = open(e2.get(), 'r', encoding='utf-8-sig')
    secText = file.read();
    file.close()
    file = open(e3.get(), 'r', encoding='utf-8-sig')
    supText = file.read();
    file.close()
    secList = split_into_sentences(secText)
    supList = split_into_sentences(supText)
    secList.extend(supList)
    coisine = []
    # extracted=""
    for text in secList:
        if (text.strip() != extracted):
            coisine.append([text.strip(), cosineVal(extracted, text)])
    coisine.sort(key=lambda x: x[1], reverse=True)
    extracted += coisine[0][0] + coisine[1][0]
    messagebox.showinfo("result", extracted)
    print(extracted)
    #
    # except:
    #     print("Error in files")
    # return output
if __name__ == '__main__':
    parent = Tk()
    secText=""
    supText=""
    Label(parent, text="Main File").grid(row=1)
    Label(parent, text="Secondary File").grid(row=2)
    Label(parent, text="Support File").grid(row=3)

    e1 = Entry(parent)
    e2 = Entry(parent)
    e3 = Entry(parent)

    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)

    Button(parent, text ="Add main article", command = addMain).grid(row=4, column=0)
    Button(parent, text ="Add secondary article", command = addSec).grid(row=4, column=1, sticky=W, pady=4)
    c=Button(parent, text ="Add support article", command = addSup).grid(row=4, column=2, sticky=W, pady=4)
    r=Button(parent, text ="Run", command = predict).grid(row=4, column=3, sticky=W, pady=4)
    Button(parent, text='Quit', command=parent.quit).grid(row=4, column=4, sticky=W, pady=4)
    # t=Text(parent).grid(row=5,column=4)

    mainloop()
    # try:



