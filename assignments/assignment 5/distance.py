#! /usr/bin/env python3 
# coding=utf-8

'''
write a function that calculates the distance in miles between two cities.

Given the latitude and longitude coordinates of cities, calculate the distance
in miles between them. Then, write a program that prompts for the coordinates of
two cities, uses the function to calculate the distance, and outputs the result.

Charlie Say
Alex Nylund
10:00 AM
Assignment 5

---- PSUEDO ----

def calculation():
    distance in miles between two cities given latitude and longitude

def coordinates():
    input: coordinates for city 1
    input: coordinates for city 2
    (call calculation function)

output: result(distance in miles)

'''

import math


def distance():
    """
    Calculate the Haversine distance.

    Parameters
    ----------
    city_coords_1 : tuple of float
        (lat, long)
    city_coords_2 : tuple of float
        (lat, long)

    Returns
    -------
    distance_in_km : float

    Examples
    --------
    >>> origin = (48.1372, 11.5756)  # Munich
    >>> destination = (52.5186, 13.4083)  # Berlin
    >>> round(distance(origin, destination), 1)
    504.2
    """
    city1_lat = float(input("Enter the latitude for the first location: "))
    city1_lon = float(input("Enter the longitude for the first location: "))
    city2_lat = float(input("Enter the latitude of the second location: "))
    city2_lon = float(input("Enter the longitude for the second location: "))

    

    dlat = math.radians(city2_lat - city1_lat)
    dlon = math.radians(city2_lon - city1_lon)
    a = (math.sin(dlat / 2) * math.sin(dlat / 2) +
         math.cos(math.radians(city1_lat)) * math.cos(math.radians(city2_lat)) *
         math.sin(dlon / 2) * math.sin(dlon / 2))
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = (6371 * c) * 0.621371


 
   

    print(f"the distance is {round(d, 2)}")


distance()