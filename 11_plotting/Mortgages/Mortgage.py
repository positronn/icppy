# Mortgage.py
import numpy as np
import matplotlib.pyplot as plt

def find_payment(loan, r, m):
    '''
    Assumes: loan and r are floats, m an int.
    Returns the monthly paument for a mortgage of size
        loan at a monthly eate of r for m months.
    '''
    return loan*((r * (1 + r) ** m) / ((1 + r) ** m - 1))


class Mortgage:
    '''
    Abstract class for building different kinds of mortgages.
    '''
    def __init__(self, loan, annual_rate, months):
        '''
        Assumes: loan and annual_rate are floats, months an int
        Creates a new mortgage of size loan, duration months and
        annual rate annual_rate.
        '''
        self.loan = loan
        self.rate = annual_rate / 12
        self.months = months
        self.paid = [0.0]
        self.outstanding = [loan]
        self.payment = find_payment(loan, self.rate, months)
        self.legend = None
    
    def make_payment(self):
        '''Make a payment'''
        self.paid.append(self.payment)
        reduction = self.payment - self.outstanding[-1] * self.rate
        self.outstanding.append(self.outstanding[-1] - reduction)

    def get_total_paid(self):
        '''Returmn the total amoun paid so far'''
        return sum(self.paid)
    
    def __str__(self):
        return self.legend
    
    def plot_payments(self, style):
        plt.plot(self.paid[1:], style, label = self.legend)
    
    def plot_balance(self, style):
        plt.plot(self.outstanding, style, label = self.legend)
    
    def plot_to_pd(self, style):
        total_pd = [self.paid[0]]
        for i in range(1, len(self.paid)):
            total_pd.append(total_pd[-1] + self.paid[i])
        plt.plot(total_pd, style, label = self.legend)
    
    def plot_net(self, style):
        total_pd =[self.paid[0]]
        for i in range(1, len(self.paid)):
            total_pd.append(total_pd[-1] + self.paid[i])
        equity_acquired = np.array([self.loan] * len(self.outstanding))
        equity_acquired = equity_acquired - np.array(self.outstanding)
        net = np.array(total_pd) - equity_acquired
        plt.plot(net, style, label = self.legend)