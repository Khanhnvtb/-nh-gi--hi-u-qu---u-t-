from fuzzy import *
import tkinter

def calculate_fuzzy():
    _profit = float(profitEntry.get())
    _cost = float(costEntry.get())
    _time = float(timeEntry.get())

    my_fuzzy = Fuzzy(_profit, _cost, _time)
    my_fuzzy.inference()
    my_fuzzy.defuzzifier()

    resultLabel.config(text=f"Hiệu quả đầu tư: {my_fuzzy}")
    print(my_fuzzy)

window = tkinter.Tk()
window.title("Đánh giá hiệu quả đầu tư")

frame = tkinter.Frame(window)
frame.pack()

fuzzyFrame = tkinter.LabelFrame(frame, text="Hiệu quả đầu tư")
fuzzyFrame.grid(row=0, column=0, padx=20, pady=20)

profitLabel = tkinter.Label(fuzzyFrame, text="Tỷ suất lợi nhuận")
profitLabel.grid(row=0, column=0)

costLabel = tkinter.Label(fuzzyFrame, text="Chi phí")
costLabel.grid(row=0, column=1)

timeLabel = tkinter.Label(fuzzyFrame, text="Thời gian")
timeLabel.grid(row=0, column=2)

profitEntry = tkinter.Entry(fuzzyFrame)
costEntry = tkinter.Entry(fuzzyFrame)
timeEntry = tkinter.Entry(fuzzyFrame)

profitEntry.grid(row=1, column=0)
costEntry.grid(row=1, column=1)
timeEntry.grid(row=1, column=2)

resultLabel = tkinter.Label(frame)
resultLabel.grid(row=1, column=0)

button = tkinter.Button(frame, text="Enter", command=calculate_fuzzy)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

window.mainloop()