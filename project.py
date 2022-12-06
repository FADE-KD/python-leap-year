'''Your task to create a functionality in which when user will input a range of two dates. Then your module will find and print all years in the range of given dates
those are leap years separately and rest of the years those are non-leap separately.
For example:
Input date range in the format dd/mm/yy
(12/01/200) to (13/12/2025)
Leaps years are:
2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048.
Non leap years are:
2001,2002,2005,2006,2007,...........'''



Starting_date = input("Enter starting date in dd/mm/yyyy format: ")
Ending_date = input("Enter ending date in dd/mm/yyyy format: ")
empty_list1 = []
empty_list2 = []

#---------------------------------------------------------------------------------------->

day1,month1,year1 = Starting_date.split("/")
day2,month2,year2 = Ending_date.split("/")

#                                             <----------converting string to integer------------->

day1 = int(day1)
month1 = int(month1)
year1 = int(year1)


day2 = int(day2)
month2 = int(month2)
year2 = int(year2)



#                                   <-----------program for finding leap year and non leap year------------>
if year1 < year2:
    print("Leap year are: ")
    for i in range(year1 , year2 + 1):
        if (i % 4 == 0 and i%100 !=0 or i % 400 ==0):
            empty_list1.append(str(i))
    print(", ".join(empty_list1))
        
        #break

    
    print("Non leap years are: ")
    for j in range(year1 , year2 + 1):
        if (j % 4 == 0 and j%100 !=0 or j % 400 == 0):
            pass
        else:
            empty_list2.append(str(j))
    print(", ".join(empty_list2))
else:
    print("Check your year input")
