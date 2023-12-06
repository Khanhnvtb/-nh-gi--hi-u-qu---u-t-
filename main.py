from fuzzy import *
import tkinter

def is_decimal(num):
    try:
        return num.replace('.', '', 1).isnumeric()
    except:
        return num.isnumeric()
    
def calculate_fuzzy():
    _profit = profitEntry.get()
    _cost = costEntry.get()
    _time = timeEntry.get()

    if _profit and _cost and _time:
        if is_decimal(_profit) and is_decimal(_cost) and is_decimal(_time):
            print(_profit, _cost, _time)

            my_fuzzy = Fuzzy(float(_profit), float(_cost), float(_time))
            my_fuzzy.inference()
            my_fuzzy.defuzzifier()

            errorLabel.config(text="")
            resultLabel.config(text=f"Hiệu quả đầu tư: {my_fuzzy}")
            print(my_fuzzy)
        else:
            errorLabel.config(text="Dữ liệu nhập vào phải là số thực")
    else:
        errorLabel.config(text="Bạn cần phải nhập thông tin trước khi xem kết quả")





window = tkinter.Tk()
window.title("Đánh giá hiệu quả đầu tư")

frame = tkinter.Frame(window)
frame.pack()

fuzzyFrame = tkinter.LabelFrame(frame, text="Hiệu quả đầu tư")
fuzzyFrame.grid(row=0, column=0, padx=20, pady=20)

profitLabel = tkinter.Label(fuzzyFrame, text="Tỷ suất lợi nhuận")
profitLabel.grid(row=0, column=0)

costLabel = tkinter.Label(fuzzyFrame, text="Chi phí đầu tư")
costLabel.grid(row=0, column=1)

timeLabel = tkinter.Label(fuzzyFrame, text="Thời gian hoàn vốn")
timeLabel.grid(row=0, column=2)

profitEntry = tkinter.Entry(fuzzyFrame)
costEntry = tkinter.Entry(fuzzyFrame)
timeEntry = tkinter.Entry(fuzzyFrame)

profitEntry.grid(row=1, column=0)
costEntry.grid(row=1, column=1)
timeEntry.grid(row=1, column=2)

resultLabel = tkinter.Label(frame)
resultLabel.grid(row=1, column=0)

errorLabel = tkinter.Label(frame)
errorLabel.grid(row=2, column=0)

button = tkinter.Button(frame, text="Xem kết quả", command=calculate_fuzzy)
button.grid(row=3, column=0, sticky="news", padx=20, pady=20)

window.mainloop()
