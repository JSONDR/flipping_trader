import csv
import numpy as num

# load_data() defintion: load .csv data from a file and return data
def load_data(name):
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        data = []

        #used to convert minutely data to daily data
        prev_day = 0
        day = 0

        for row in csv_reader:
            if(line_count == 0):
                line_count += 1
                continue
            time_stamp = row[0]
            day = int(time_stamp.split('/')[2])

            if(prev_day != day):
                data.append((float(row[1]), float(row[2]), float(row[3]), float(row[4]), float(row[6])))
                prev_day = day
            # just load the open price
            if(row[1] == ''):
                break
    return data

# compute_ROI() definition: for day_i < day_j, computes return on investment 
def compute_ROI(day_i, day_j):
    ROI = ((day_j - day_i) / day_i ) * 100 #as a percentage
    return ROI


# Data in memory is in the format of a 6-tuple such as: (Date, Open, High, Low, Close, Adj Close, Volume)
def run_selected(month_index, starting_balance):
    data = load_data("BTC_2020_data/{}.csv".format(month_index))
    balance = starting_balance
    _len = len(data)

    i = 0
    while(i < _len - 1):
        #flip a coin, 1 corresponds to heads and 0 corresponds to tails
        outcome = num.random.randint(0, 2)
        #print(outcome)
        data_x = data[i][0]
        data_y = data[i + 1][0]
        ROI = compute_ROI(data_x, data_y)
        ROI = ROI * 0.01 #adjust from percentage to 
        if(outcome == 0):
            fee = balance * 0.0004
            balance = balance + balance * (-ROI) - fee
        elif(outcome == 1):
            fee = balance * 0.0004
            balance = balance + balance * ROI - fee
        else:
            pass
        i += 1
    
    hold_balance = starting_balance
    ROI_hold = compute_ROI(data[0][0], data[_len - 1][0]) * 0.01
    hold_balance = hold_balance + hold_balance * ROI_hold
    if(balance > hold_balance):
        return 1, balance, hold_balance
    return 0, balance, hold_balance

if __name__ == '__main__':
    n_traders = int(input("Select number of traders: "))
    starting_balance = int(input("Specify starting balances for all traders: $"))
    balances = []
    hold_balance = 0
    k = 0   
    if(n_traders > 100):
        print("Simulation is running, please be patient. If a very large number of traders was specified, it will take a very long time, so it is recommended to input a number less than equal to 100.")
    else:
        print("Simulation is running, this may take a minute")
    while(k < n_traders):
        i = 1
        while(i <= 12):
            ret, balance, hold_balance = run_selected(i, starting_balance)
            balances.append(int(balance))
            i += 1
        k += 1
    print("Trader Bob who bought Bitcoin at the start of each month, then sold at the end each month turned his ${} into ${} in 2020.".format(starting_balance, int(hold_balance)))
    print("Trader Minny who was one of the {} traders performed the worst and turned her ${} into ${} in 2020.".format(n_traders, starting_balance, min(balances)))
    print("Trader Max who was one of the {} traders performed the best and turned his ${} into ${} in 2020.".format(n_traders, starting_balance, max(balances)))
    print("Conclusion in the form of a question: did Max perform better than Minny, or was Max lucky and Minny was unlucky?")