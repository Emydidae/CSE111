"""
Code by Peter Solis
CSE 111 Section 20
Instructor - William Clements
Assignment: W04 Teach - Can Sizes
"""

import math as m

def main():
    # setting data
    can_name = ['#1 Picnic', '#1 Tall', '#2', '#2.5', "#3 Cylinder", "#5", '#6Z', '#8Z Short', '#10', '#211', '#300', '#303']
    can_rad = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    can_height = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    can_cost = [.28, .43, .45, .61, .86, .83, .22, .26, 1.53, .34, .38, .42]

    # print values
    for i in range(12):
        print(f'{can_name[i]}:\n\
Storage Efficiency: {compute_storage_efficiency(can_rad[i],can_height[i])}\n\
Cost Efficiency: {compute_cost_efficiency(can_rad[i],can_height[i],can_cost[i])}\n')
    pass

def compute_volume(r, h):
    """
    Find the volume of a cylinder
    Parameters:
        r = radius of cylinder
        h = height of cylinder
    """
    vol = m.pi * (r ** 2) * h
    return vol

def compute_surface_area(r, h):
    """
    Find the surface areas of a cylinder
    Parameters:
        r = radius of cylinder
        h = height of cylinder
    """
    s_area = 2 * m.pi * r * (r + h)
    return s_area

def compute_storage_efficiency(r, h):
    """
    Find the storage efficiency of a can
    Parameters:
        r = radius of cylinder
        h = height of cylinder
    """
    store_eff = compute_volume(r, h) / compute_surface_area(r, h)
    return round(store_eff,2)

def compute_cost_efficiency(r, h, cost):
    """
    Find the cost efficiency of a can
    Parameters:
        r = radius of cylinder
        h = height of cylinder
        cost = cost per can
    """
    cost_eff = compute_volume(r, h) / cost
    return round(cost_eff,2)

main()
