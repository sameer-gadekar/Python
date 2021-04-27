
from tkinter import *
root = Tk()
Variable1 = StringVar(root)
Variable2 = StringVar(root)
Variable1.set("Currency")
Variable2.set("Currency")
def RealTimeCurrencyConversion():
    import requests, json
    from_currency = Variable1.get()
    to_currency = Variable2.get()
    api_key = "M8V0HP5QPH3NJYVZ"
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"
    main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency + "&apikey=" + api_key 
    req_ob = requests.get(main_url)
    result = req_ob.json()
    Exchange_Rate = float(result['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    amount = float(Amount1_field.get())
    new_amount = round(amount*Exchange_Rate,3)
    Amount2_field.insert(0,str(new_amount))
def clear_all():
    Amount1_field.delete(0,END)
    Amount2_field.delete(0,END)
if __name__ == '__main__':
    root.configure(background='Light green')
    root.geometry("400x175")
    headlable =Label(root,text = "Welcome to Real Time Currency Conversion",fg = 'Black',bg = 'red')
    label1 = Label(root,text = "Amount :",fg = 'black', bg = 'dark green')
    label2 = Label(root,text = "From Currency :",fg = 'black', bg = 'dark green')
    label3 = Label(root,text = "To Currency :",fg = 'black', bg = 'dark green')
    label4 = Label(root,text = "Converted Amount :",fg = 'black', bg = 'dark green')
    headlable.grid(row = 0,column = 1)
    label1.grid(row = 1,column = 0)
    label2.grid(row = 2,column = 0)
    label3.grid(row = 3,column = 0)
    label4.grid(row = 5,column = 0)
    Amount1_field = Entry(root)
    Amount2_field = Entry(root)
    Amount1_field.grid(row = 1,column = 1,ipadx = '25')
    Amount2_field.grid(row = 5,column = 1,ipadx = '25')
    currencyCode_list = ['INR', 'USD', 'CAD', 'CNY', 'DKK', 'EUR']
    FromCurrency_Options = OptionMenu(root,Variable1,*currencyCode_list)
    ToCurrency_Options = OptionMenu(root,Variable2,*currencyCode_list)
    FromCurrency_Options.grid(row = 2, column = 1, ipadx = 10)
    ToCurrency_Options.grid(row = 3, column = 1, ipadx = 10)
    button1 = Button(root, text = 'Convert', bg = 'red', fg = 'black', command = RealTimeCurrencyConversion)
    button1.grid(row = 4, column = 1)
    button2 = Button(root, text = 'Clear', bg = 'red', fg = 'black', command = clear_all)
    button2.grid(row = 6, column = 1)
    root.mainloop()

