from tkinter import *
from netcommands import *

class uiWindow():
    def __init__(self):

        bgcolor = "#FFFFFF"
        fgcolor = "#000000"
        status = 20
        self.refreshrate = 500                      # Refresh rate in milliseconds


        self.root = Tk()                            # Makes the window
        self.root.wm_title("WiFi Strength Tool")    # Makes the title that will appear in the top left
        self.root.config(background = bgcolor)
        self.nc = netcommands()
        
        # Instantiate all Frame Elements
        self.mainframe = Frame(self.root, width=100, height = 600, bg = bgcolor)
        self.mainframe.grid(row=0, column=0, padx=10, pady=2)
        
        # Updates the Frame
        self.root.update()
        
        # Draws all the frame elements
        self.mainframe = self.uiPanel(self.root, self.mainframe, bgcolor)
        
    def start(self):
        self.root.mainloop()                        #start monitoring and updating the GUI

    def uiPanel(self, root, frame, color):
        self.root = root
        self.frame = frame
        self.color = color

        # Right Frame and its contents
        # Create Button Frame
        self.btnFrame = Frame(self.frame, width=200, height=10, borderwidth=1, bg=self.color)
        self.btnFrame.grid(row=1, column=0, padx=10, pady=2)

        # Create Start Button
        self.gettempbtn = Button(self.btnFrame, text="Start", command=lambda:self.startloop())
        self.gettempbtn.grid(row=0, column=0, padx=10, pady=2)

        # Create Stop Button
        self.stoptempbtn = Button(self.btnFrame, text="Stop", command=lambda:self.stoploop())
        self.stoptempbtn.grid(row=0, column=1, padx=10, pady=2)

        # Create Exit Button
        self.closeexitbtn = Button(self.btnFrame, text="Quit", command=lambda:self.closeexit())
        self.closeexitbtn.grid(row=0, column=2, padx=10, pady=2)

        # Create Running Label
        self.runningstr = StringVar()
        self.runningstr.set("")
        self.runningstrtext = Label(self.btnFrame, textvariable=self.runningstr,bg=self.color,font=("Arial",10))
        self.runningstrtext.grid(row=2,column=0,columnspan=3, padx=10, pady=2)

        # Create Wifi SSID Label
        self.wifissid = StringVar()
        self.wifissid.set("SSID")
        self.wifissidtext = Label(self.btnFrame, textvariable=self.wifissid,bg=self.color,font=("Arial",18))
        self.wifissidtext.grid(row=3,column=0,columnspan=3, padx=10, pady=2)

        # Create Wifi Strenth Label
        self.wifistrength = StringVar()
        self.wifistrength.set("0%")
        self.wifistrengthtext = Label(self.btnFrame, textvariable=self.wifistrength,bg=self.color,font=("Arial",50))
        self.wifistrengthtext.grid(row=4,column=0,columnspan=3, padx=10, pady=2)

    # Get the wifi strength and updates stuff
    def gettemp(self):
        ssid,strength = self.nc.getnetstr()
        self.wifissid.set(ssid)
        self.wifistrength.set(strength)
        
        run = self.runningstr.get()
        if len(run)>3:
            run="."
        else:
            run=run+"."
        
        self.runningstr.set(run)


    # Passes in object for progress bar
    def startloop(self):
        self.runacquisition = TRUE
        self.updateSTR()
    
    # Stops acquisition
    def stoploop(self):
        self.runacquisition = FALSE

    # Runs if runacquisition is set to run
    def updateSTR(self):
        if self.runacquisition:
            self.gettemp()
            self.frame.after(self.refreshrate, self.updateSTR)
    
    # Exit the program
    def closeexit(self):
        exit(0)

if __name__ == '__main__':
    wifiUI = uiWindow()
    wifiUI.start()