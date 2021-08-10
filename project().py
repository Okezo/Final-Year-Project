import requests

# API key
api_key = "*insert API Key here*"

# home address input
origin1 = "*include sample coordinate*"
origin2 = "*include sample coordinate*"
origin3 = "*include sample coordinate*"
#input("Enter a home address\n") 
  
# work address input
destination1 = "*include sample coordinate*"
destination2 = "*include sample coordinate*"
destination3 = "*include sample coordinate*"
#input("Enter a work address\n")
  
# base url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"

a = 1
while a == 1:

    # get response
    l = requests.get(url + "origins=" + origin1 + "&destinations=" + destination1 + "&key=" + api_key) 
    c = requests.get(url + "origins=" + origin2 + "&destinations=" + destination2 + "&key=" + api_key) 
    r = requests.get(url + "origins=" + origin3 + "&destinations=" + destination3 + "&key=" + api_key) 
    
    # return time as text and as seconds; and distance as meters     
    seconds1 = l.json()["rows"][0]["elements"][0]["duration"]["value"]
    distance1 = l.json()["rows"][0]["elements"][0]["distance"]["value"]
     
    seconds2 = c.json()["rows"][0]["elements"][0]["duration"]["value"]
    distance2 = c.json()["rows"][0]["elements"][0]["distance"]["value"]
     
    seconds3 = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    distance3 = r.json()["rows"][0]["elements"][0]["distance"]["value"]
    
    # print the travel time and distance
    print("\nThe total travel time and distance from home to work is", seconds1, "seconds", distance1, "meters")
    print("\nThe total travel time and distance from home to work is", seconds2, "seconds", distance2, "meters")
    print("\nThe total travel time and distance from home to work is", seconds3, "seconds", distance3, "meters")

    t1 = distance1 * 0.072
    t2 = distance2 * 0.045
    t3 = distance3 * 0.072

    if (t1 * 4) < seconds1:
        x = "RED"
    elif (t1 * 2) < seconds1:
        x = "BLUE"
    else:
        x = "GREEN"


    if (t2 * 4) < seconds2:
        y = "RED"
    elif (t2 * 2) < seconds2:
        y = "BLUE"
    else:
        y = "GREEN"


    if (t3 * 4) < seconds3:
        z = "RED"
    elif (t3 * 2) < seconds3:
        z = "BLUE"
    else:
        z = "GREEN"

    print("\nThe standard time of travel is", t1, t2, t3)

   # COLOUR TEST
   # x = "RED"
   # y = "RED"
   # z = "RED"

    print("\nThe LED light should show", x, y, z)

    try:
        from pyfirmata import Arduino, util
    except:
        import pip
        pip.main(['install','pyfirmata'])
        from pyfirmata import Arduino, util
    import time

    board = Arduino('COM4')

    iterator = util.Iterator(board)
    iterator.start()


    if z == "RED":
        board.digital[2].write(1) 
        board.digital[5].write(0)
        board.digital[3].write(0)                
    elif z == "BLUE":
        board.digital[5].write(1)
        board.digital[2].write(0)
        board.digital[3].write(0)
    elif z == "GREEN":
        board.digital[3].write(1)
        board.digital[2].write(0)
        board.digital[5].write(0)

    if y == "RED":
        board.digital[6].write(1)
        board.digital[9].write(0)
        board.digital[7].write(0)               
    elif y == "BLUE":
        board.digital[9].write(1)
        board.digital[6].write(0)
        board.digital[7].write(0)
    elif y == "GREEN":
        board.digital[7].write(1)
        board.digital[6].write(0)
        board.digital[9].write(0)

    if x == "RED":
        board.digital[10].write(1)
        board.digital[12].write(0)
        board.digital[11].write(0)               
    elif x == "BLUE":
        board.digital[12].write(1)
        board.digital[10].write(0)
        board.digital[11].write(0)
    elif x == "GREEN":
        board.digital[11].write(1)
        board.digital[10].write(0)
        board.digital[12].write(0)



    board.exit()

    time.sleep(10.0)