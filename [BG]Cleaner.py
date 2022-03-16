# Creator : MR.D3F417 > BLACK GUARD TM > WWW.blackberryy.ir 
# Discord : https://discord.gg/KsskgvE48z
# Prerequisites : 
# Dont Copy Script Kids
# Zlink : https://zil.ink/mrd3f417
# IranHack : https://www.iranhack.com/forum/member/5816-mr-def411
# GitHub : https://github.com/MRD3F417

import tkinter
import tkinter.messagebox
import os
import os.path
import threading

rubbishExt = ['.tmp', '.bak', '.old', '.wbk', '.xlk', '_mp', '.gid',
              '.chk', '.syd', '.$$$', '.@@@', ".~*"]


def GetDrives():
    drives = []
    for i in range(65, 91):
        vol = chr(i) + ":/"
        if os.path.isdir(vol):
            drives.append(vol)
    return tuple(drives)


class Window:
    def __init__(self):
        self.root = tkinter.Tk()

        # Create menu.
        menu = tkinter.Menu(self.root)

        # Create 'System' submenu
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label="About...", command=self.MenuAbout)
        submenu.add_separator()
        submenu.add_command(label="Quit", command=self.MenuExit)
        menu.add_cascade(label="System", menu=submenu)

        # Create 'Clean' submenu
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label="Scan", command=self.MenuScanRubbish)
        submenu.add_command(label="Delete", command=self.MenuDelRubbish)
        menu.add_cascade(label="Clean", menu=submenu)

        # Create 'Search' submenu
        submenu = tkinter.Menu(menu, tearoff=0)
        submenu.add_command(label="Search Big Files",
                            command=self.MenuScanBigFile)
        submenu.add_separator()
        submenu.add_command(label="Search Big Files By Name",
                            command=self.MenuSearchFile)
        menu.add_cascade(label="Search", menu=submenu)

        self.root.config(menu=menu)

        # Create labels to show info
        self.progress = tkinter.Label(self.root, anchor=tkinter.W,
                                      text='Status', bitmap='hourglass',
                                      compound='left')
        self.progress.place(x=10, y=370, width=480, height=15)

        # Create text box to show file list
        self.flist = tkinter.Text(self.root)
        self.flist.place(x=10, y=10, width=480, height=350)

        # Create scroll bar for text box
        self.vscroll = tkinter.Scrollbar(self.flist)
        self.vscroll.pack(side='right', fill='y')
        self.flist['yscrollcommand'] = self.vscroll.set
        self.vscroll['command'] = self.flist.yview

    def MainLoop(self):
        self.root.title("Black Guard")
        self.root.minsize(500, 400)
        self.root.maxsize(500, 400)
        self.root.mainloop()

    def MenuAbout(self):
        tkinter.messagebox.showinfo("Black Guard",
                                    "This a disk clean-up program. Create By : Black Guard Cyber Team" +
                                    " your advice.")

    def MenuExit(self):
        self.root.quit()

    def MenuScanRubbish(self):
        result = tkinter.messagebox.askquestion("Black Guard", "Scaning" +
                                                " junk files may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Black Guard", "Scaning in no time!")
        # self.ScanRubbish()
        self.drives = GetDrives()
        t = threading.Thread(target=self.ScanRubbish, args=(self.drives,))
        t.start()

    def MenuDelRubbish(self):
        result = tkinter.messagebox.askquestion("Black Guard",
                                                "Deleting junk files may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Black Guard", "Deleting in no time!")
        self.drives = GetDrives()
        t = threading.Thread(target=self.DeleteRubbish, args=(self.drives,))
        t.start()

    def MenuScanBigFile(self):
        result = tkinter.messagebox.askquestion("Black Guard",
                                                "Scaning big files may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Black Guard", "Scaning in no time!")

    def MenuSearchFile(self):
        result = tkinter.messagebox.askquestion("Black Guard",
                                                "Searching big files by name may cost much time. Continue?")
        if result == 'no':
            return
        tkinter.messagebox.showinfo("Black Guard", "Searching in no time!")

    def ScanRubbish(self, scanpath):
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:
                                fname = os.path.join(
                                    os.path.abspath(root), fil)
                                filesize += os.path.getsize(fname)
                                if total % 20 == 0:
                                    self.flist.delete(0.0, tkinter.END)
                                self.flist.insert(tkinter.END, fname+'\n')
                                l = len(fname)
                                if l > 60:
                                    self.progress['text'] = fname[:30] + '...' + \
                                        fname[l-30:l]
                                else:
                                    self.progress['text'] = fname
                                total += 1
                        except ValueError:
                            pass
                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = "Find %s junk files, occupy %.2f M disk space" \
            % (total, filesize/1024/1024)

    def DeleteRubbish(self, scanpath):
        global rubbishExt
        total = 0
        filesize = 0
        for drive in scanpath:
            for root, dirs, files in os.walk(drive):
                try:
                    for fil in files:
                        filesplit = os.path.splitext(fil)
                        if filesplit[1] == '':
                            continue
                        try:
                            if rubbishExt.index(filesplit[1]) >= 0:
                                fname = os.path.join(
                                    os.path.abspath(root), fil)
                                filesize += os.path.getsize(fname)
                                try:
                                    os.remove(fname)
                                    l = len(fname)
                                    if l > 50:
                                        fname = fname[:25] + "..." + \
                                            fname[l-25:l]
                                    if total % 15 == 0:
                                        self.flist.delete(0.0, tkinter.END)
                                    self.flist.insert(tkinter.END, 'Deleted '
                                                      + fname + '\n')
                                    self.progress['text'] = fname
                                    total += 1
                                except:
                                    pass
                        except ValueError:
                            pass
                except Exception as e:
                    print(e)
                    pass
        self.progress['text'] = f"Deleted {total} junk files, recover {filesize/1024/1024} M disk space"


if __name__ == "__main__":
    window = Window()
    window.MainLoop()