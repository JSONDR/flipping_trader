# flipping_trader
Description: a simulation about some number of cryptocurrency traders who trade Bitcoin each day throughout 2020, each base their decision process on the outcome of flipping a coin each day. Do some of the traders outperform a holding strategy? 

Steps to run this simulation:

  1. in a terminal with Python 3 installed, execute:  
            python3 flipping_trader.py
  2. follow the prompts by inputting some numbers;
  3. observe the output.


For sake of time on your behalf, here are some sample outputs of the simulation:

<img width="904" alt="10_traders" src="https://user-images.githubusercontent.com/35650788/155052213-67fd976d-a63d-40fe-a14e-9b12aa71ec15.png">

<img width="905" alt="100_traders" src="https://user-images.githubusercontent.com/35650788/155052221-f0b44b1b-8904-4ec5-ad0d-540f74c3d0f5.png">

<img width="941" alt="1000_traders" src="https://user-images.githubusercontent.com/35650788/155052227-d4464b89-4080-4682-b407-c7674b5a92bd.png">

The data contained in BTC_2020_data is Bitcoin futures data which was downloaded through python-binance. Each data point is a measurement taken every minute on a futures platform. The data is labelled
using integers from 1 through to 12 where each integer maps to a month like:

			1 -> January, 2 -> Feburary, ..., 12 -> December


The data contained in the BTC_2020_data folder was collected using the python-binance Python module. More information about python-binance can be found here: https://python-binance.readthedocs.io/en/latest/
