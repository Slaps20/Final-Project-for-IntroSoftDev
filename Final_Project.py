"""
Author: Justin May
Data Written: 9/16/2024
Last Modiflied: 9/16/2024
Assignment:
Program Name: Elden Ring Randomizer
This program allows the user to interact with a GUI and pick a set of chooices for a random weapon from
the game Elden Rign.
"""
#imports
import random
from breezypythongui import EasyFrame
#empty list
aList = []
#weapon list
daggers_base = ["Dagger", "Parrying Dagger", "Misericorde", "Great Knife", "Bloodstanied Dagger",
                "Erdsteel Dagger", "Wakizashi", "Celebrants sickle", "Ivory sickle", "Crystal Knife",
                "Scorpions Stinger", "Cinquedea", "Glintstone Kris", "Reduvia, Blade of Calling",
                "Blakc Knife"]
daggers_dlc = ["Fire Knight ShortSword", "Main-gauche"]
straightSwords_base = ["Short Sword", "Longswrod", "Broadsword", "Weathered Straight Sword",
                       "Lordsworn's Straight Sword", "Noble's Slender Sword", "Cane Sword",
                       "Warhawk's Talon", "Lazuli Glintstone Sword", "Carian Knight's Sword",
                       "Crystal Sword", " Rotten Crystal Sword", "Miquellan Knight's Sword",
                       "Ornamental Straight Sword", "Golden Epitaph", "Sword of St Trina",
                       "Regaila of Eochaid", "Coded Sword", "Sword of Night and Flame"]
straightSwords_dlc = ["Velvet Sword of St Trina", "Stone-Sheathed Sword", "Sowrd of Light",
                      "Sword of Darkness"]
greatSwords_base = ["Bastard Sword", "Claymore", "Iron Greatsword", "Lordsworn's Greatsword",
                    "Knight's Greatsword", "Banished Knight's Greatsword", "Forked Greatsword",
                    "Flamberge", "Gargoyle's Greatsword", "Gargoyle's Blackblade", "Inseparable Sword",
                    "Sword of Milos", "Marais Executioner's Sword", "Ordovies's Greatsword",
                    "Alabaster Lord's Sword", "Death's Poker", "Helphen's Steeple", "Blasphemous Blade",
                    "Golden Order Greatsword", "Dark Moon Greatsword", "Sacred Relic Sword"]
greatSwords_dlc = ["Lizard Greatsword", "Greatswrod of Danmation", " Greatsword of Solitude"]
#GUI for base or dlc selection
class BaseOrDlc(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Base or DLC")
        #label for instructions of GUI
        self.addLabel(text = "Please selec base, dlc, or both for your weapon", row = 0, column = 0, columnspan = 2)
        self.addLabel(text = "Then hit next when your ready to move on", row = 1, column = 0, columnspan = 2)
        #buttons
        self.baseCB = self.addCheckbutton(text = "Base", row = 2, column = 0, command = self.checker)
        self.dlcCB = self.addCheckbutton(text = "DLC", row = 2, column = 1, command = self.checker)
        self.nextBtn = self.addButton(text = "Next", row = 3, column = 0, columnspan = 3, state = "disabled", command = self.next)
        self.addButton(text = "Exit", row = 4, column = 1, command = self.exits)
    #Check Box commands
    def checker(self):
        if self.baseCB.isChecked() or self.dlcCB.isChecked():
            self.nextBtn["state"] = "normal"
        else:
            self.nextBtn["state"] = "disabled"
    #next button command
    def next(self):
        global WeaponClass
        global check
        if self.baseCB.isChecked() and self.dlcCB.isChecked():
            check = 2
        elif self.baseCB.isChecked():
            check = 1
        elif self.dlcCB.isChecked():
            check = 0
        #need this to close window and open other gui
        self.quit()
        self.destroy()
    #the exit button
    def exits(self):
        quit(None)
#GUI weapon class selection
class WeaponClass(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "Weapon Class")
        #label for instructions of GUI
        self.addLabel(text = "Please select all weapon class you would like", row = 0, column = 0, columnspan = 3)
        self.addLabel(text = "You have to choose at least one option before you can continue", row = 1, column = 0, columnspan= 3)
        self.hidden = self.addLabel(text = "", row = 4, column = 0, columnspan = 3)
        #buttons for GUI
        self.daggerCB = self.addCheckbutton(text = "Daggers", row = 2, column = 0, command = self.checker)
        self.straightCB = self.addCheckbutton(text = "Straight Swords", row = 2, column = 1, command = self.checker)
        self.greatCB = self.addCheckbutton(text = "Great Swords", row = 2, column = 2, command = self.checker)
        self.okBtn = self.addButton(text = "OK", row = 3, column = 0, columnspan = 3, state = "disabled", command = self.ok)
        self.addButton(text = "Start Over", row = 5, column = 0, command = self.restart)
        self.addButton(text = "Exit", row = 5, column = 2, command = self.exits)
    #check box commands
    def checker(self):
        if self.daggerCB.isChecked() or self.straightCB.isChecked() or self.greatCB.isChecked():
            self.okBtn["state"] = "normal"
        else:
            self.okBtn["state"] = "disabled"
    #okay button command
    def ok(self):
        #disables buttons after clicking ok
        self.hidden["text"] = "Please hit start over to restart the process"
        self.daggerCB["state"] = "disabled"
        self.straightCB["state"] = "disabled"
        self.greatCB["state"] = "disabled"
        self.okBtn["state"] = "disabled"
        #adding daggers to aList
        if self.daggerCB.isChecked():
            if check == 2:
                aList.extend(daggers_base)
                aList.extend(daggers_dlc)
            elif check == 1:
                aList.extend(daggers_base)
            elif check == 0:
                aList.extend(daggers_dlc)
        #adding straight swords to aList
        if self.straightCB.isChecked():
            if check == 2:
                aList.extend(straightSwords_base)
                aList.extend(straightSwords_dlc)
            elif check == 1:
                aList.extend(straightSwords_base)
            elif check == 0:
                aList.extend(straightSwords_dlc)
        #adding great swords to aList
        if self.greatCB.isChecked():
            if check == 2:
                aList.extend(greatSwords_base)
                aList.extend(greatSwords_dlc)
            elif check == 1:
                aList.extend(greatSwords_base)
            elif check == 0:
                aList.extend(greatSwords_dlc)
        #pickes weapons from created list
        weapon = random.choice(aList)
        #Pops up a window to tell you the choosen weapon
        self.messageBox(title = "The Choice", message = "Drum roll please. Your weapon is... " + weapon, width = 65)
    #The restart button
    def restart(self):
        global aList
        aList = []
        self.destroy()
        self.quit()
        main()
    #the exit button
    def exits(self):
        exit(None)
    
#function to run program
def main():
    BaseOrDlc().mainloop()
    WeaponClass().mainloop()

if __name__ == "__main__":
    main()
