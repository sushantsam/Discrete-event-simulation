#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 11:48:53 2021

@author: sushantsamvarghese
"""


import VBASim
import Basic_Classes as bc
import RNG
import numpy as np
import math


TheQueues = []
TheResources = []
TheDTStats = []
TheCTStats = []

ParkingLot = bc.FIFOQueue()
MaxCars = 0
TimeSpent = bc.DTStat()
Calendar = bc.EventCalendar()


TheQueues.append(ParkingLot)
TheDTStats.append(TimeSpent)

AllAverageQueues = []
AllMaxCars = []
AllTimeSpent = []

print("Rep","Average Number","Max Number","Average Time Spent")

MeanTBA = 0.1
MeanPT = 1.0

def Arrival():
    global MaxCars
    NewCar = bc.Entity(Clock)
    ParkingLot.Add(NewCar,Clock)
    VBASim.Schedule(Calendar,"Arrival", RNG.Expon(MeanTBA,1), Clock)
    VBASim.Schedule(Calendar,"Departure", RNG.Expon(MeanPT,2), Clock)
    if ParkingLot.NumQueue()>MaxCars:
        MaxCars = ParkingLot.NumQueue()
    
def Departure():
    DepartingCar = ParkingLot.Remove(Clock)
    TimeSpent.Record(Clock - DepartingCar.CreateTime)
    


for reps in range(0,10,1):
     Clock = 0.0
     MaxCars = 0
     
     
     VBASim.VBASimInit(Calendar,TheQueues,TheCTStats,TheDTStats,TheResources,Clock)

     # This section was added
     # It adds 10 cars in the system and then schedules the departure for those 10 cars as well
     MaxCars = 10
     for i in range(0,10):
         NewCar = bc.Entity(Clock)
         ParkingLot.Add(NewCar,Clock)
         VBASim.Schedule(Calendar,"Departure", RNG.Expon(MeanPT,2), Clock)
         
         #Print to ensure code is working correctly 
         #print(ParkingLot.NumQueue())
         #print(Clock)
     
     VBASim.Schedule(Calendar,"Arrival",RNG.Expon(MeanTBA,1),Clock)
     VBASim.Schedule(Calendar,"EndSimulation",24,Clock)

     
     NextEvent = Calendar.Remove()
     Clock = NextEvent.EventTime
     if NextEvent.EventType == "Arrival":
         Arrival()
     elif NextEvent.EventType == "Departure":
         Departure()
         
     while NextEvent.EventType != "EndSimulation":
           NextEvent = Calendar.Remove()
           Clock = NextEvent.EventTime
           if NextEvent.EventType == "Arrival":
                Arrival()
           elif NextEvent.EventType == "Departure":
               Departure()
               
     AllAverageQueues.append(ParkingLot.Mean(Clock))
     AllMaxCars.append(MaxCars)
     AllTimeSpent.append(TimeSpent.Mean())
     print(reps+1,ParkingLot.Mean(Clock),MaxCars,TimeSpent.Mean())
     
     
     
print("Results")     
print(np.mean(AllAverageQueues))
print(np.std(AllAverageQueues)*math.sqrt(10))
print(np.mean(AllMaxCars))
print(np.std(AllMaxCars))
print(np.mean(AllTimeSpent))
print(np.std(AllTimeSpent))


        
        
        
     
     
     
     
     
     
     
     
     
     
     
     
     
     
