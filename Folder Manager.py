import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,filedialog
import os
import shutil

root=tk.Tk()
# root.geometry("500x500")
# root.resizable(,0)
root.minsize(550,200)
root.configure(bg='#00FFFF')
root.title("Folder Manager")
root.wm_iconbitmap('folder.ico')
##################Welcome Lable###########################3

lable0=tk.Label(root,text='Welcome to Folder Manager',font=("Arial",25),fg="Red",bg='#00FFFF')
lable0.grid(row=0,column=0,columnspan=3)

######################### Select Type ####################

lable1=tk.Label(root,text='Select Type',font=("Arial",20),bg='#00FFFF')
lable1.grid(row=1,column=0,sticky=tk.W)
e1var=tk.StringVar()
e1=ttk.Combobox(root,font=("Arial",10),width=21,textvariable=e1var)
l1=['PDF Files','Picture Files','Video Files','Audio File','Excel File','Word File']
e1['values']=l1
e1.current(0)
e1.grid(row=1,column=1)

######################## Folder Path ########################
path_choose_image=tk.PhotoImage(file='Folder-Open-icon (2).png')
l2=tk.Label(root,text='Folder Path',font=("Arial",20),bg='#00FFFF')
l2.grid(row=2,column=0,sticky=tk.W)
e2var=tk.StringVar()
e2=ttk.Entry(root,font=("Arial",10),width=25,textvariable=e2var)
e2.grid(row=2,column=1)
def b2_func():
    global folder_path
    folder_path = filedialog.askdirectory(title='Select File')
    e2var.set(folder_path)
b2 = ttk.Button(root,image=path_choose_image,command=b2_func,text='Select Path')
b2.grid(row=2,column=3)
count1=5

################### Submit button #################################
color_changer=0
def sub_func():
    global count1,color_changer
    color_changer+=1
    type=e1var.get()
    folder_path = e2var.get()
    ################ extensions ###################
    count1+=1
    music_extencens=('.aif ','.cda','. mid','. midi','.mp3','.mpa','.wav ','.wma','.ogg','.mp3', '.wva', '.wav', '.m4a', '.flac')
    pdf_extencens=('.pdf','.rtf','.tex')
    picture_extencens=['.jpeg','.png','.gif','.tiff','.psd','.heic']
    video_extencens=['.mp4', '.mkv', '.MKV', '.flv', '.mpeg']
    excel_extencens=['.xlsx','.ods']
    word_extencens=['.odt','. docx']
    extencens = [pdf_extencens,picture_extencens,video_extencens,music_extencens,excel_extencens,word_extencens]

    def file_finder(folder_path,extencen):
        global type
        type1=type
        a=[]
        for j in extencen:
            for i in os.listdir(folder_path):
                if i.endswith(j):
                    a.append(i)
        thanks_lable=tk.Label(text='Thanks For Using Our App',font=('Arial',15),bg='#FFFF00',fg='#FF0000')
        thanks_lable.grid(row=count1, columnspan=3, sticky=tk.W)
        return a

    try:
        for m in range(len(extencens)):
            if os.path.exists(f'{folder_path}\\{type}'):
                pass
            else:
                os.mkdir(f'{folder_path}\\{type}')
            if l1.index(type) == m:
                music=file_finder(folder_path,extencens[m])
                count=0
                try:
                    for i in music:
                        count+=1
                        shutil.move(f'{folder_path}\\{i}',f'{folder_path}\\{type}')
                except:
                    return
        # ttk.Label(text=f'total {type} file moved in {len(music)} deep').grid(row=count1, column=0, sticky=tk.W)
    except ValueError:
        tk.messagebox.askretrycancel('Error', 'Please Select Right Value')
    except FileNotFoundError:
        tk.messagebox.askretrycancel('Error', 'Path Not Found')
    except:
        return
    e2var.set('')
    if color_changer%2==1:
        root.configure(bg='#61FF00')
        lable0.configure(bg='#61FF00')
        lable1.configure(bg='#61FF00')
        l2.configure(bg='#61FF00')
    else :
        root.configure(bg='#00FFFF')
        lable1.configure(bg='#00FFFF')
        lable0.configure(bg='#00FFFF')
        l2.configure(bg='#00FFFF')
submit_butt=ttk.Button(text="Submit",command=sub_func)
submit_butt.grid(row=3,columnspan=3)
submit_butt.focus()
root.mainloop()