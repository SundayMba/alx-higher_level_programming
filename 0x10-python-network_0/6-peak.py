#!/usr/bin/python3
"""Defines a peak-finding algorithm."""


def find_peak(list_of_integers):
    #Return a peak in a list of unsorted integers.
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    mid = int(size / 2)
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])

"""
def find_peak(list_of_integers):
    peaks = []
    if list_of_integers == []:
        return None
    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)
    else:
        for i, n in enumerate(list_of_integers):
            if i == 0 and n >= list_of_integers[i+1]:
                peaks.append(n)
            elif i == size - 1 and n > list_of_integers[i-1]:
                peaks.append(n)
            elif i != 0 and i != size - 1:
                if n >= list_of_integers[i+1] and n >= list_of_integers[i-1]:
                    peaks.append(n)
        if len(peaks) > 1:
            return max(peaks)
        else:
            return peaks[0]
            """
