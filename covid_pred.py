import csv
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.configure(bg="lightblue")
window.geometry("500x500")
window.resizable(False,False) # x ,y
window.title("Naive Bayes")

# Frame Input
input_frame = ttk.Frame(window)

# penempatan (grid , pack , place)
input_frame.pack(padx=10,pady=10,fill="x",expand=True)

# komponen - komponen
# 1 . label input1
label_depan = ttk.Label(input_frame,text="Total Case : ")
label_depan.pack(padx=10,pady=10,fill="x",expand=True)
# 2 . entry input1
INPUT1 = tk.IntVar()
entry_depan = ttk.Entry(input_frame,textvariable=INPUT1 )
entry_depan.pack(padx=10,fill="x",expand=True)

# 3 . label input2
label_belakang = ttk.Label(input_frame,text="Probability Case : ")
label_belakang.pack(padx=10,pady=10,fill="x",expand=True)
# 4 . entry input2
INPUT2 = tk.IntVar()
entry_belakang = ttk.Entry(input_frame,textvariable=INPUT2)
entry_belakang.pack(padx=10,fill="x",expand=True)

# 3 . label input3
label_belakang = ttk.Label(input_frame,text="New Case : ")
label_belakang.pack(padx=10,pady=10,fill="x",expand=True)
# 4 . entry input3
INPUT3 = tk.IntVar()
entry_belakang = ttk.Entry(input_frame,textvariable=INPUT3)
entry_belakang.pack(padx=10,fill="x",expand=True)

# 5 . Tombol
def tombol_click():
    pairs = [("tot_cases", "tot_death"), ("prob_cases", "tot_death"), ('new_case', "tot_death")]

    results00 = []
    results01 = []
    results10 = []
    results11 = []
    results02 = []
    results12 = []

    for pair in pairs:
        count_00 = 0
        count_01 = 0
        count_10 = 0
        count_11 = 0
        count_02 = 0
        count_12 = 0
        count_zero = 0
        count_one = 0
        count_two = 0

        with open('Datatrain2.csv') as file:
            baca = csv.DictReader(file)
            for row in baca:
                if int(row[pair[0]]) == 0 and int(row[pair[1]]) == 0:
                    count_00 += 1
                elif int(row[pair[0]]) == 1 and int(row[pair[1]]) == 0:
                    count_10 += 1
                elif int(row[pair[0]]) == 0 and int(row[pair[1]]) == 1:
                    count_01 += 1
                elif int(row[pair[0]]) == 1 and int(row[pair[1]]) == 1:
                    count_11 += 1
                elif int(row[pair[0]]) == 0 and int(row[pair[1]]) == 2:
                    count_02 += 1
                elif int(row[pair[0]]) == 1 and int(row[pair[1]]) == 2:
                    count_12 += 1
                if int(row[pair[1]]) == 0:
                    count_zero += 1
                if int(row[pair[1]]) == 1:
                    count_one += 1
                if int(row[pair[1]]) == 2:
                    count_two += 1

        result_00 = count_00 / count_zero
        result_01 = count_01 / count_one
        result_10 = count_10 / count_zero
        result_11 = count_11 / count_one
        result_02 = count_02 / count_two
        result_12 = count_12 / count_two

        results00.append(result_00)
        results01.append(result_01)
        results10.append(result_10)
        results11.append(result_11)
        results02.append(result_02)
        results12.append(result_12)

    result00 = 1
    for r in results00:
        result00 *= r
        
    result01 = 1
    for r in results01:
        result01 *= r
        
    result10 = 1
    for r in results10:
        result10 *= r
        
    result11 = 1
    for r in results11:
        result11 *= r
        
    result02 = 1
    for r in results02:
        result02 *= r
        
    result12 = 1
    for r in results12:
        result12 *= r

    def convert_tot_cases(x):
        if x > 1500000:
            return 1
        else:
            return 0

    def convert_prob_cases(x):
        if x > 120000:
            return 1
        else:
            return 0

    def convert_new_case(x):
        if x > 2500:
            return 1
        else:
            return 0
        

    tot_cases = INPUT1
    prob_cases = INPUT2
    new_case = INPUT3

    tot_cases = convert_tot_cases(tot_cases.get())
    prob_cases = convert_prob_cases(prob_cases.get())
    new_case = convert_new_case(new_case.get())

    user_group = ''.join([str(i) for i in [tot_cases, prob_cases, new_case]])

    print(user_group)

    hasil = 0 

    if user_group == '000' :
        hasil = max(result00, result01, result02)
    if user_group == '001' :
        hasil = max(result00, result01, result12)
    if user_group == '010' :
        hasil = max(result00, result11, result02)
    if user_group == '011' :
        hasil = max(result00, result11, result12)
    if user_group == '100' :
        hasil = max(result10, result01, result02)
    if user_group == '101' :
        hasil = max(result10, result01, result12)
    if user_group == '110' :
        hasil = max(result10, result11, result02)
    if user_group == '111' :
        hasil = max(result10, result11, result12)


    with open('Datatrain2.csv', newline='') as csvfile:

        baca = csv.DictReader(csvfile)
        total_group_count = 0
        total_group_count1 = 0
        total_group_count2 = 0
        row_count = 0
        count_group = 0
        count_group1 = 0
        count_group2 = 0
        count_group0 = 0
        count2 = 0
        count1 = 0
        count0 = 0

        for row in baca:
            group = row['tot_cases'] + row['prob_cases'] + row['new_case']
            group1 = row['tot_cases'] + row['prob_cases'] + row['new_case'] + row['tot_death']
            group2 = row['tot_death']
            values = group.split('+')
            values1 = group1.split('+')
            values2 = group2.split('+')
            group_count = len(values)
            group_count1 = len(values1)
            group_count2 = len(values2)

            total_group_count = total_group_count + group_count
            total_group_count1 = total_group_count1 + group_count1
            total_group_count2 = total_group_count2 + group_count2

            row_count += 1

            if group == user_group:
                count_group += 1

            if group2 == '1':
                count2 += 1

            if group2 == '2':
                count1 += 1

            if group2 == '0':
                count0 += 1

            if group1 == user_group + '2':
                count_group2 += 1

            if group1 == user_group + '1':
                count_group1 += 1

            if group1 == user_group + '0':
                count_group0 += 1

    # Calculate the ratio of rows where group is 111 to total rows
    
    pengali1 = count_group / row_count
    pengali2 = count_group2 / count1   
    hasilpengali = pengali2 * pengali1
    pengali3 = count_group1 / count2
    hasilpengali1 = pengali3 * pengali1
    pengali4 = count_group0 / count0
    hasilpengali2 = pengali4 * pengali1
    if hasilpengali1 > 0 or hasilpengali > 0 or hasilpengali2 > 0:
        hasilakhir = hasilpengali / (hasilpengali + hasilpengali1 + hasilpengali2)
    else:
        hasilakhir = "0"
    showinfo(message=hasilakhir)

    with open('hasil.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([tot_cases, prob_cases, new_case, hasil])

sapa_button = ttk.Button(input_frame,text='Calculate',command=tombol_click)
sapa_button.pack(padx=10,pady=10, fill="x",expand=True)


window.mainloop()




