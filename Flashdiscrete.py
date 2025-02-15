# Import Library
import random
import sys
import time
from tkinter import *
from tkinter import messagebox

# ---------------------------------- #

# Code for sub-menu Himpunan
SOAL_HIMPUNAN = [
    'A = (1,2,3,4,5) dan B = (2,4,6,8). \n Berapa nilai A - B?',
    'K = (-2,-1,0,1,2,3) \n K termasuk himpunan apa?',
    'Jika A = (3, 5, 8) & B = (5, 3, 8), \n maka ...',
    'P = (1,2,3,9,12,13). \n Himpunan kelipatan 3 yang terdapat \n di P adalah ...',
    'Banyaknya himpunan bagian dari (1,2) \n adalah ...'
]

JAWABAN_HIMPUNAN = [
    '1,3,5',
    'bilangan bulat',
    'A = B',
    '3,9,12',
    '4'
]

ran_num = random.randrange(0, len(SOAL_HIMPUNAN))
jumbled_rand_word = SOAL_HIMPUNAN[ran_num]
points = 0

def himpunan_main():
    def back():
        my_window.destroy()
        start_main_page()

    def change():
        global ran_num
        ran_num = random.randrange(0, len(SOAL_HIMPUNAN))
        word.configure(text=SOAL_HIMPUNAN[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def check():
        global points, ran_num
        user_word = get_input.get().lower()
        if user_word == JAWABAN_HIMPUNAN[ran_num]:
            points += 5
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('Pesan', "Yippieee..., jawaban kamu benar!")
            ran_num = random.randrange(0, len(SOAL_HIMPUNAN))
            word.configure(text=SOAL_HIMPUNAN[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Pesan", "Yahhh..., jawaban kamu salah!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=JAWABAN_HIMPUNAN[ran_num])
        else:
            ans_lab.configure(text='Poin kamu tidak cukup')

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Flashdiscrete")
    my_window.configure(background="#685268")

    lab_img1 = Button(text="Kembali",
                      bg='#685268',
                      border=0,
                      justify='center',
                      fg="#FFFFFF",
                      font=("Arial", 12),
                      command=back
                      )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(text="Score: ",
                  pady=10,
                  bg="#685268",
                  fg="#FFFFFF",
                  font="Titillium 14 bold"
                  )
    score.pack(anchor="n")

    word = Label(text=jumbled_rand_word,
                 pady=10,
                 bg="#685268",
                 fg="#FFFFFF",
                 font=("Courier", 14),
                 justify='center'
                 )
    word.pack(anchor="n")

    get_input = Entry(font=("Courier", 14),
                      borderwidth=10,
                      justify='center'
                      )
    get_input.pack()

    submit = Button(text="Submit",
                    width=18,
                    borderwidth=8,
                    font=("", 13),
                    fg="#000000",
                    bg="#FCB677",
                    command=check
                    )
    submit.pack(pady=(10, 20))

    change = Button(text="Ganti Soal",
                    width=18,
                    borderwidth=8,
                    fg="#000000",
                    bg="#FCB677",
                    font=("", 13),
                    command=change
                    )
    change.pack()

    ans = Button(text="Hint",
                 width=18,
                 borderwidth=8,
                 fg="#000000",
                 bg="#FCB677",
                 font=("", 13),
                 command=show_answer
                 )
    ans.pack(pady=(20, 10))

    ans_lab = Label(text="",
                    bg="#685268",
                    fg="#FFFFFF",
                    font="Titillium 14 bold"
                    )
    ans_lab.pack()

    my_window.mainloop()

# ---------------------------------- #

# Code for sub-menu Fungsi
SOAL_FUNGSI = [
    'Berapakah hasil dari 25 mod 7?',
    'Berapakah nilai fungsi floor dari 5, 6?',
    'Diberikan fungsi f(x) = x - 1, dan \n g(x) = x^2 + 1. \n Tentukan fog(x)!',
    'Berapa nilai dari log 100?',
    'Berapa nilai dari 2^-3?'
]

JAWABAN_FUNGSI = [
    '4',
    '5',
    'x^2',
    '2',
    '1/8'
]

ran_num = random.randrange(0, len(SOAL_FUNGSI))
jumbled_rand_word = SOAL_FUNGSI[ran_num]
points = 0

def fungsi_main():
    def back():
        my_window.destroy()
        start_main_page()

    def change():
        global ran_num
        ran_num = random.randrange(0, len(SOAL_FUNGSI))
        word.configure(text=SOAL_FUNGSI[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def check():
        global points, ran_num
        user_word = get_input.get().lower()
        if user_word == JAWABAN_FUNGSI[ran_num]:
            points += 5
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('Pesan', "Yippieee..., jawaban kamu benar!")
            ran_num = random.randrange(0, len(SOAL_FUNGSI))
            word.configure(text=SOAL_FUNGSI[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Pesan", "Yahhh..., jawaban kamu salah!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=JAWABAN_FUNGSI[ran_num])
        else:
            ans_lab.configure(text='Poin kamu tidak cukup')

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Flashdiscrete")
    my_window.configure(background="#685268")

    lab_img1 = Button(text="Kembali",
                      bg='#685268',
                      border=0,
                      justify='center',
                      fg="#FFFFFF",
                      font=("Arial", 12),
                      command=back
                      )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(text="Score: ",
                  pady=10,
                  bg="#685268",
                  fg="#FFFFFF",
                  font="Titillium 14 bold"
                  )
    score.pack(anchor="n")

    word = Label(text=jumbled_rand_word,
                 pady=10,
                 bg="#685268",
                 fg="#FFFFFF",
                 font=("Courier", 14),
                 justify='center'
                 )
    word.pack(anchor="n")

    get_input = Entry(font=("Courier", 14),
                        borderwidth=10,
                        justify='center'
                        )
    get_input.pack()

    submit = Button(text="Submit",
                    width=18,
                    borderwidth=8,
                    font=("", 13),
                    fg="#000000",
                    bg="#FCB677",
                    command=check
                    )
    submit.pack(pady=(10, 20))

    change = Button(text="Ganti Soal",
                    width=18,
                    borderwidth=8,
                    fg="#000000",
                    bg="#FCB677",
                    font=("", 13),
                    command=change
                    )
    change.pack()

    ans = Button(text="Hint",
                    width=18,
                    borderwidth=8,
                    fg="#000000",
                    bg="#FCB677",
                    font=("", 13),
                    command=show_answer
                    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(text="",
                    bg="#685268",
                    fg="#FFFFFF",
                    font="Titillium 14 bold"
                    )
    ans_lab.pack()

    my_window.mainloop()

# ---------------------------------- #

# Code for sub-menu Kombinatorika
SOAL_KOMBINATORIAL = [
    'Berapa banyak kata yang terbentuk \n dari kata "DISKRIT"?',
    'Berapakah jumlah kemungkinan membentuk \n 3 angka dari 5 angka berikut: 1,2,3,4,5, \n jika tidak boleh ada pengulangan angka?',
    'Jika bit biner hanya 0 dan 1. \n Berapa banyak string biner yang \n dapat dibentuk jika panjang string 5 bit?',
    'Berapa banyak kata yang dapat \n terbentuk dari kata "HAPUS"?',
    'Tentukan banyaknya cara memilih 4 kaleng cat \n dari 45 kaleng cat yang tersedia?'
]

JAWABAN_KOMBINATORIAL = [
    '5040',
    '60',
    '32',
    '120',
    '148995'
]

ran_num = random.randrange(0, len(SOAL_KOMBINATORIAL))
jumbled_rand_word = SOAL_KOMBINATORIAL[ran_num]
points = 0

def kombinatorial_main():
    def back():
        my_window.destroy()
        start_main_page()

    def change():
        global ran_num
        ran_num = random.randrange(0, len(SOAL_KOMBINATORIAL))
        word.configure(text=SOAL_KOMBINATORIAL[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def check():
        global points, ran_num
        user_word = get_input.get().lower()
        if user_word == JAWABAN_KOMBINATORIAL[ran_num]:
            points += 5
            score.configure(text="Score: " + str(points))
            messagebox.showinfo('Pesan', "Yippieee..., jawaban kamu benar!")
            ran_num = random.randrange(0, len(SOAL_KOMBINATORIAL))
            word.configure(text=SOAL_KOMBINATORIAL[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Pesan", "Yahhh..., jawaban kamu salah!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score: " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=JAWABAN_KOMBINATORIAL[ran_num])
        else:
            ans_lab.configure(text='Poin kamu tidak cukup')

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Flashdiscrete")
    my_window.configure(background="#685268")

    lab_img1 = Button(text="Kembali",
                      bg='#685268',
                      border=0,
                      justify='center',
                      fg="#FFFFFF",
                      font=("Arial", 12),
                      command=back
                      )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(text="Score: ",
                  pady=10,
                  bg="#685268",
                  fg="#FFFFFF",
                  font="Titillium 14 bold"
                  )
    score.pack(anchor="n")

    word = Label(text=jumbled_rand_word,
                 pady=10,
                 bg="#685268",
                 fg="#FFFFFF",
                 font=("Courier", 14),
                 justify='center'
                )
    word.pack(anchor="n")

    get_input = Entry(font=("Courier", 14),
                        borderwidth=10,
                        justify='center'
                        )
    get_input.pack()

    submit = Button(text="Submit",
                    width=18,
                    borderwidth=8,
                    font=("", 13),
                    fg="#000000",
                    bg="#FCB677",
                    command=check
                    )
    submit.pack(pady=(10, 20))

    change = Button(text="Ganti Soal",
                    width=18,
                    borderwidth=8,
                    fg="#000000",
                    bg="#FCB677",
                    font=("", 13),
                    command=change
                    )
    change.pack()

    ans = Button(text="Hint",
                    width=18,
                    borderwidth=8,
                    fg="#000000",
                    bg="#FCB677",
                    font=("", 13),
                    command=show_answer
                    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(text="",
                    bg="#685268",
                    fg="#FFFFFF",
                    font="Titillium 14 bold"
                    )
    ans_lab.pack()

    my_window.mainloop()

# ---------------------------------- #

# Code for About Game
def tentang_game_main():
    def back():
        my_window.destroy()
        start_main_page()

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Flashdiscrete")
    my_window.configure(background="#685268")

    lab_img1 = Button(text="Kembali",
                      bg='#685268',
                      border=0,
                      justify='center',
                      fg="#FFFFFF",
                      font=("Arial", 12),
                      command=back
                      )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    word = Label(pady=10,
                 bg="#685268",
                 fg="#FFFFFF",
                 justify='center',
                 font=("Arial", 12),
                 text="Nama Flashdiscrete diambil dari konsep media pembelajaran \n"
                      "Flashcard. Jadi, aplikasi ini dibuat sebagai media pembelajaran \n"
                      "untuk pelajaran matematika diskrit. Dalam setiap materi, \n"
                      "ada 5 soal uraian singkat yang bisa dikerjakan."
                 )
    word.pack()

    my_window.mainloop()

# ---------------------------------- #

# Code for Main Page
def start_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            himpunan_main()
        elif args == 2:
            fungsi_main()
        elif args == 3:
            kombinatorial_main()

    def option():
        lab_img = Label(
            main_window,
            text="Pilih Soal",
            bg='#685268',
            fg="#FFFFFF",
            font=("Expo", 28)
        )
        lab_img.pack(pady=(50, 0))

        sel_btn1 = Button(
            main_window,
            text="Himpunan",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#FCB677",
            justify='center',
            cursor="hand2",
            command=lambda: start_game(1)
        )
        sel_btn1.pack(pady=(50, 20))

        sel_btn2 = Button(
            main_window,
            text="Fungsi",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#FCB677",
            justify='center',
            cursor="hand2",
            command=lambda: start_game(2)
        )
        sel_btn2.pack(pady=(50, 20))

        sel_btn3 = Button(
            main_window,
            text="Kombinatorial",
            width=18,
            borderwidth=8,
            font=("", 18),
            fg="#000000",
            bg="#FCB677",
            justify='center',
            cursor="hand2",
            command=lambda: start_game(3)
        )
        sel_btn3.pack(pady=(50, 20))

    def pilih_menu(args):
        main_window.destroy()
        if args == 1:
            tentang_game_main()
        elif args == 2:
            sys.exit()

    def show_option():
        start_btn.destroy()
        lab_img.destroy()
        caber_btn.destroy()
        keluar_btn.destroy()
        option()

    main_window = Tk()
    main_window.geometry("500x500+500+150")
    main_window.resizable(0, 0)
    main_window.title("Flashdiscrete")
    main_window.configure(background="#685268")

    lab_img = Label(
        main_window,
        text="FLASHDISCRETE",
        fg="#FFFFFF",
        bg='#685268',
        font=("Expo", 28)
    )
    lab_img.pack(pady=(50, 0))

    start_btn = Button(
        main_window,
        text="Mulai",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#FCB677",
        font=("", 13),
        cursor="hand2",
        command=show_option
    )
    start_btn.pack(pady=(50, 20))

    caber_btn = Button(
        main_window,
        text="Tentang aplikasi ini",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#FCB677",
        font=("", 13),
        cursor="hand2",
        command=lambda: pilih_menu(1)
    )
    caber_btn.pack(pady=(50, 20))

    keluar_btn = Button(
        main_window,
        text="Keluar",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="#FCB677",
        font=("", 13),
        cursor="hand2",
        command=lambda: pilih_menu(2)
    )
    keluar_btn.pack(pady=(50, 20))

    main_window.mainloop()

start_main_page()