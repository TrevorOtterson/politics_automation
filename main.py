"""
Trevor Otterson
Was Clinton Right?
Data Automation
"""

def main():
    
    csv_file=open('BLS_private.csv','r')
    
    """Program starts"""
    
    republican = []
    democrat = []
    rep_total = 0
    dem_total = 0


    for line in csv_file:
        line = csv_file.readline()
        line = line.split(',')
        if line[0] == "republican":
            republican.append(line)
            rep_total += int(line[2])*2
        elif line[0] == "democrat":
            democrat.append(line)
            dem_total += int(line[2])*2


    f=open("presidents.txt", "w")
    
    f.write("Democrat: " + str(dem_total))
    f.write("\nRepublican: " + str(rep_total))
    f.write("""\n\nClintons claims were actually false.
Republicans produced 5,301,878 more jobs
than Democrats during this data selcection.""")
    f.write("""\n\nThere is no sure data showing what is actually true.
Jobs come from many things besides just presidents, whos to say who
is responsible for making the most jobs besides corporations.""")
    f.close()


if __name__ == "__main__":
    main()