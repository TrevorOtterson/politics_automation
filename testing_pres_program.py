def main():
    
    import csv
    from itertools import islice
    
    reptotal=0
    demtotal=0
    
    demlist=(1961,1962,1963,1964,1965,1966,1967,1968,1977,1978,1979,1980,1993,1994,1995,1996,1997,1998,1999,2000,2009,2010,2011,2012,2013)
    replist=(1969,1970,1971,1972,1973,1974,1975,1976,1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,2001,2002,2003,2004,2005,2006,2007,2008)
    
    p = open('presidents.txt', 'w')

    
    with open('BLS_private.csv') as d:
        for line in islice(csv.reader(d), 6, None):
            yeartotal=0
            year=float(line[0])
            yeartotal+=float(line[1])
            yeartotal+=float(line[2])
            yeartotal+=float(line[3])
            yeartotal+=float(line[4])
            yeartotal+=float(line[5])
            yeartotal+=float(line[6])
            yeartotal+=float(line[7])
            yeartotal+=float(line[8])
            yeartotal+=float(line[9])
            yeartotal+=float(line[10])
            if line[11]<str(10):
                line[11]=0
                line[12]=0
            yeartotal+=float(line[11])
            yeartotal+=float(line[12])
            for i in demlist:
                if i==year:
                    demtotal+=yeartotal
                    
            for i in replist:
                if i==year:
                    reptotal+=yeartotal
                    
    p.write('\n%s: %s\n'%("Democrat",demtotal))
    p.write('\n%s: %s\n'%("Republican",reptotal))
    
if __name__ == "__main__":
    main()