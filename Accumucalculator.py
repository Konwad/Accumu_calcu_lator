import os
import pygubu
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import threading
import time


# odwołanie do GUI stworzonego przy pomocy zewnętrznej biblioteki pygubu
PROJECT_PATH = os.path.dirname(__file__)
PROJECT_UI = os.path.join(PROJECT_PATH, "accu_calc_GUI.ui")


# klasa wątku obliczeniowego
class obliczenia(threading.Thread):
    def __init__(self, argumenty, wyniki=[]):
        threading.Thread.__init__(self)
        self.wyniki_gotowe = False
        self.argumenty = argumenty
        self.wyniki = wyniki

    # zdefiniowanie polecenia run odpowiedzialnego za obliczenie wyników
    def run(self):
        # przypisanie wartości z GUI zmiennym
        self.Osz=self.argumenty[7]
        self.Or=self.argumenty[8]
        self.Psz=self.argumenty[9]
        self.Pr=self.argumenty[10]
        self.Um=self.argumenty[1]
        self.Un=self.argumenty[2]
        self.C=self.argumenty[3]
        self.Im=self.argumenty[4]
        self.Isz=self.argumenty[5]
        self.m=self.argumenty[6]

        # lista z wynikami
        self.wyniki=[round(self.Osz * self.Or * self.Psz * self.Pr, 0),
                       round(self.Um * self.Osz * self.Psz, 2),
                       round(self.Un * self.Osz * self.Psz, 2),
                       round(self.Im * self.Or * self.Pr, 2),
                       round(self.Isz * self.Or * self.Pr, 2),
                       round(self.Um * self.Osz * self.Psz * self.Im * self.Or * self.Pr / 1000, 2),
                       round(self.Um * self.Osz * self.Psz * self.Isz * self.Or * self.Pr / 1000, 2),
                       round(self.Osz * self.Or * self.Psz * self.Pr * self.Um * self.C * 3.6 / 1000000, 4),
                       round((self.Osz * self.Or * self.Psz * self.Pr * self.Um * self.C * 3.6 / 1000000) / 3.6 * 1000, 2),
                       round(self.m * self.Osz * self.Or * self.Psz * self.Pr, 2),
                       round(((self.Osz * self.Or * self.Psz * self.Pr * self.Um * self.C * 3.6 / 1000000) / 3.6 * 1000) / (self.m * self.Osz * self.Or * self.Psz * self.Pr), 5)
                       ]

        time.sleep(1)

        self.wyniki_gotowe = True


# klasa GUI
class AccuCalcGuiApp:
    def __init__(self, parent, obliczenia, argumenty, wyniki):
        self.obliczenia = obliczenia
        self.argumenty = argumenty
        self.wyniki = wyniki
        self.builder = builder = pygubu.Builder()  # 1: Create a builder
        builder.add_resource_path(PROJECT_PATH)
        builder.add_from_file(PROJECT_UI)  # 2: Load an .ui file
        self.mainwindow = builder.get_object('top_level_frame', parent)  # 3: Create the mainwindow
        builder.connect_callbacks(self)

        # pobranie wartości z GUI do zmiennych
        self.lab_1 = builder.get_object('lab_1', parent)
        self.lab_2 = builder.get_object('lab_2', parent)
        self.lab_3 = builder.get_object('lab_3', parent)
        self.lab_4 = builder.get_object('lab_4', parent)
        self.lab_5 = builder.get_object('lab_5', parent)
        self.lab_6 = builder.get_object('lab_6', parent)
        self.lab_7 = builder.get_object('lab_7', parent)
        self.lab_8 = builder.get_object('lab_8', parent)
        self.lab_9 = builder.get_object('lab_9', parent)
        self.lab_10 = builder.get_object('lab_10', parent)
        self.lab_11 = builder.get_object('lab_11', parent)
        self.gestosc_energii = builder.get_object('gestosc_energii', parent)
        self.masa_ogniw = builder.get_object('masa_ogniw', parent)
        self.energia_Wh = builder.get_object('energia_Wh', parent)
        self.energia_MJ = builder.get_object('energia_MJ', parent)
        self.moc_szczyt = builder.get_object('moc_szczyt', parent)
        self.moc_max = builder.get_object('moc_max', parent)
        self.prad_szczyt = builder.get_object('prad_szczyt', parent)
        self.prad_max = builder.get_object('prad_max', parent)
        self.napiecie_nom = builder.get_object('napiecie_nom', parent)
        self.napiecie_max = builder.get_object('napiecie_max', parent)
        self.ilosc_ogniw = builder.get_object('ilosc_ogniw', parent)

    # definiowanie wyboru ogniwa
    def select(self):
        value = self.lab_1.get()
        if value == 'SonyUS18650_VTC6':
            # przypisanie wartości dla wybranego ogniwa
            self.lab_2.insert(0, 4.2)
            self.lab_3.insert(0, 3.6)
            self.lab_4.insert(0, 3000)
            self.lab_5.insert(0, 30)
            self.lab_6.insert(0, 80)
            self.lab_7.insert(0, 46.6)

        elif value == 'SamsungINR18650-35E':
            # przypisanie wartości dla wybranego ogniwa
            self.lab_2.insert(0, 4.2)
            self.lab_3.insert(0, 3.6)
            self.lab_4.insert(0, 3500)
            self.lab_5.insert(0, 8)
            self.lab_6.insert(0, 13)
            self.lab_7.insert(0, 48.3)

        elif value == 'PanasonicUR18650NSX':
            # przypisanie wartości dla wybranego ogniwa
            self.lab_2.insert(0, 4.2)
            self.lab_3.insert(0, 3.6)
            self.lab_4.insert(0, 2600)
            self.lab_5.insert(0, 22)
            self.lab_6.insert(0, 50)
            self.lab_7.insert(0, 45.4)

        # w przypadku braku wyboru - zostawiamy puste do wpisania przez użytkownika
        elif value == '-':
            self.lab_2.insert(0, '')
            self.lab_3.insert(0, '')
            self.lab_4.insert(0, '')
            self.lab_5.insert(0, '')
            self.lab_6.insert(0, '')
            self.lab_7.insert(0, '')

    # zdefiniwanie obliczeń
    def calculate(self):

        # ostrzeżenia na wypadek, gdy komórki pozostają puste
        if self.lab_2.get() == '':
            messagebox.showinfo("Warrning", "Wprowadź napięcie max ogniwa!")
        if self.lab_3.get() == '':
            messagebox.showinfo("Warrning", "Wprowadź napięcie nominalne ogniwa!")
        if self.lab_4.get() == '':
            messagebox.showinfo("Warrning", "Wprowadź pojemność nominalną ogniwa!")
        if self.lab_5.get() == '':
            messagebox.showinfo("Warrning", "Wprowadź max prąd rozładowania ogniwa!")
        if self.lab_6.get() == '':
            messagebox.showinfo("Warrning", "Wprowadź szczytowy prąd rozładowania ogniwa!")
        if self.lab_7.get() == '':
            messagebox.showinfo("Warrning", "Wprowadź masę ogniwa!")
        if self.lab_8.get() == '':
            messagebox.showinfo("Warrning", "Wprowadź dane dot. ilości ogniw w szeregu!")
        if self.lab_9.get() == '':
            messagebox.showinfo("Warrning", "Wprowadź dane dot. ilości ogniw w rzędzie!")
        if self.lab_10.get() == '':
            messagebox.showinfo("Warrning", "Wprowadź dane dot. ilości pakietów w szeregu!")
        if self.lab_11.get() == '':
            messagebox.showinfo("Warrning", "Wprowadź dane dot. ilości pakietów w rzędzie!")
        # gdy komórki są wypełnione- pobranie danych z komórek do zmiennnych
        else:
            self.rodzaj = (self.lab_1.get())
            self.Um = float(self.lab_2.get())
            self.Un = float(self.lab_3.get())
            self.C = float(self.lab_4.get())
            self.Im = float(self.lab_5.get())
            self.Isz = float(self.lab_6.get())
            self.m = float(self.lab_7.get())
            self.Osz = float(self.lab_8.get())
            self.Or = float(self.lab_9.get())
            self.Psz = float(self.lab_10.get())
            self.Pr = float(self.lab_11.get())


            # utworzenie listy argumentów dla wątku obliczeniowego
            self.obliczenia.argumenty = [self.rodzaj, self.Um, self.Un, self.C, self.Im, self.Isz, self.m, self.Osz, self.Or, self.Psz, self.Pr]

            # wywolanie watku obliczeniowego
            self.obliczenia.start()

            while self.obliczenia.wyniki_gotowe is False:
                time.sleep(0.1)

            self.obliczenia.join()

            # przypisanie wartości obliczonych do odpowiednich zmiennych
            self.N_ogn = self.obliczenia.wyniki[0]
            self.U_max = self.obliczenia.wyniki[1]
            self.U_nom = self.obliczenia.wyniki[2]
            self.I_max = self.obliczenia.wyniki[3]
            self.I_pik = self.obliczenia.wyniki[4]
            self.P_max = self.obliczenia.wyniki[5]
            self.P_pik = self.obliczenia.wyniki[6]
            self.E_MJ = self.obliczenia.wyniki[7]
            self.E_Wh = self.obliczenia.wyniki[8]
            self.m_A = self.obliczenia.wyniki[9]
            self.G_e = self.obliczenia.wyniki[10]

            # przypisanie zmiennych do odpowiednich okienek w GUI
            self.gestosc_energii.config(text=str(self.G_e))
            self.masa_ogniw.config(text=str(self.m_A))
            self.energia_Wh.config(text=str(self.E_Wh))
            self.energia_MJ.config(text=str(self.E_MJ))
            self.moc_szczyt.config(text=str(self.P_pik))
            self.moc_max.config(text=str(self.P_max))
            self.prad_szczyt.config(text=str(self.I_pik))
            self.prad_max.config(text=str(self.I_max))
            self.napiecie_nom.config(text=str(self.U_nom))
            self.napiecie_max.config(text=str(self.U_max))
            self.ilosc_ogniw.config(text=str(self.N_ogn))

    # zdefioniowanie wykresu
    def plot(self):
        value = self.lab_1.get()

        # sprawdzenie, jaki typ ogniwa li-ion został wybrany
        if value == 'SonyUS18650_VTC6':
            import Sony
        elif value == 'SamsungINR18650-35E':
            import Samsung
        elif value == 'PanasonicUR18650NSX':
            import Panasonic

        # ostrzeżnie na wypadek braku wybrania ogniwa
        elif value == '-':
            messagebox.showinfo("Warrning", "Nie można wykonać wykresu dla tego typu ogniwa !")

    # zdefiniowanie funckji czyszczącej okienka
    def clear(self):
        # ustawienie okienek wyników na puste
        self.gestosc_energii.config(text='')
        self.masa_ogniw.config(text='')
        self.energia_Wh.config(text='')
        self.energia_MJ.config(text='')
        self.moc_szczyt.config(text='')
        self.moc_max.config(text='')
        self.prad_szczyt.config(text='')
        self.prad_max.config(text='')
        self.napiecie_nom.config(text='')
        self.napiecie_max.config(text='')
        self.ilosc_ogniw.config(text='')

        # usunięcie tekstu z komórek wejściowych
        self.lab_1.delete(0, 'end')
        self.lab_2.delete(0, 'end')
        self.lab_3.delete(0, 'end')
        self.lab_4.delete(0, 'end')
        self.lab_5.delete(0, 'end')
        self.lab_6.delete(0, 'end')
        self.lab_7.delete(0, 'end')
        self.lab_8.delete(0, 'end')
        self.lab_9.delete(0, 'end')
        self.lab_10.delete(0, 'end')
        self.lab_11.delete(0, 'end')

    # zdefiniowanie zapisu wyników do pliku .txt
    def save_result(self):
        result = tk.filedialog.asksaveasfile(defaultextension='.txt')
        if result is None:
            return
        result.write('      DANE \n' +
                     'Rodzaj ogniwa: %s \n' % self.rodzaj +
                     'Napiecie max [V]: %s \n' % self.Um +
                     'Napiecie nominalne [V]: %s \n' % self.Un +
                     'Pojemnosc nominalne [mAh]: %s \n' % self.C +
                     'Max prad rozladowania [A]: %s \n' % self.Im +
                     'Szczytowy prad rozladowania [A]: %s \n' % self.Isz +
                     'Masa ogniwa [g]: %s \n' % self.m +
                     '      PAKIET \n'
                     'Ogniw w szeregu: %s \n' % self.Osz +
                     'Ogniw w rzedzie: %s \n' % self.Or +
                     '    AKUMULATOR \n'
                     'Pakietow w szeregu: %s \n' % self.Psz +
                     'Pakietow w rzedzie: %s \n' % self.Pr +
                     '----------------------------------\n'
                     '      WYNIKI \n'
                     'Ilosz ogniw: %s \n' % self.N_ogn +
                     'Napiecie max [V]: %s  \n' % self.U_max +
                     'Napiecie nominalne [V]: %s  \n' % self.U_nom +
                     'Prad max [A]: %s \n' % self.I_max +
                     'Prad szczytowy [A]: %s \n' % self.I_pik +
                     'Moc max [kW]: %s \n' % self.P_max +
                     'Moc szczytowa [kW]: %s \n' % self.P_pik +
                     'Energia [MJ]: %s \n' % self.E_MJ +
                     'Energia [Wh]: %s \n' % self.E_Wh +
                     'Gestosc energii [kWh/kg]: %s \n' % self.G_e +
                     'Masa ogniw [g]: %s \n' % self.m_A)
        result.close()

    def run(self):

        self.mainwindow.mainloop()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Accumucalculator')
    argumenty = []
    wyniki = []
    watek_obliczeniowy = obliczenia(argumenty, wyniki)
    app = AccuCalcGuiApp(root, watek_obliczeniowy, argumenty, wyniki)
    app.run()
