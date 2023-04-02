import time
import os

def compareTime(starttime, file="timelog"):
    """
    set this at the end of the program and pass through a starttime from the beginning
    :param starttime: float: using import time, set a starttime = time.time() at the beginning of the program
    :param file: str: file path for the txt file to store time records
    :return: Prints a representation of how fast the program ran compared to previous best times
    """
    newtime = time.time() - starttime
    timeslist = []

    if os.path.exists(file):
        with open(file, "r+") as f:
            for times in f:
                timeslist.append(float(times))
            f.writelines(str(newtime) + "\n")
        try:
            oldtimerecord = sorted(timeslist)[0]
        except Exception as e:
            print(e)
        percentage_difference = abs((newtime - oldtimerecord) / oldtimerecord) * 100

        # if new time is worse than best time
        if oldtimerecord < newtime:
            print("newest iteration is: ", newtime, " Seconds: ", percentage_difference, "% worse than best time of", oldtimerecord)
        else:
            print("newest iteration is: ", newtime, " Seconds: ", percentage_difference,
                  "% better than best time of ", oldtimerecord)

    # create a new file if none exists and add the first time
    else:
        with open(file, "w") as f:
            f.writelines(str(newtime) + "\n")

        print("current iteration: ", newtime)



