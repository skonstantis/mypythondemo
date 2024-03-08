from tkinter import *
import urllib.request
import json
import urllib.parse
import tkinter as tk

serviceurl    =    'https://maps.googleapis.com/maps/api/place/textsearch/json?' 

def func(event=False):
    text.delete("1.0", tk.END)
    place = E1text.get()
    E1text.set('')
    url    =    serviceurl    +    urllib.parse.urlencode({'query': place, 'key': 'ΚΕΥ'}) #PLACES API KEY HERE TO WORK
    print    ('Retrieving',    url) 
    uh    =    urllib.request.urlopen(url) 
    data    =    uh.read()
    print('Retrieved',len(data),'characters')
    try:    
        js    =    json.loads(data.decode())
        print(str(data))
    except:    
        print("JSONConversionError is raised")
        js    =    None
 
    if    js == None or 'status'    not    in    js    or    js['status']    !=    'OK':
        text.insert(INSERT, 'No results found or API key missing or error occurred') 
        return
 
    
    
    results = js['results']
    text.insert(INSERT, str(len(results)) + " results found\n") 
 
    j = 1
    for i in results:
        text.insert(INSERT, "\n\nResult " + str(j) + ":\n") 
        try:
            name = js['results'][j - 1]['name']
        except:
            name = '-'  
        text.insert(INSERT, "Name: " + name + "\n") 
        
        try:
            location    =    js['results'][j - 1]['formatted_address']
        except:
            location = '-'  
        text.insert(INSERT, "Address: " + location + "\n") 
        
        try:
            open    =    js['results'][j - 1]['opening_hours']['open_now']
        except:
            open = 'No info'  
        if open == True:
            open = "Yes"
        elif open == False:
            open = "No"
        text.insert(INSERT, "Open now : " + str(open) + "\n") 
        
        try:
            lat = js['results'][j - 1]['geometry']['location']['lat'] 
            lng = js['results'][j - 1]['geometry']['location']['lng']
        except:
            lat = '-'  
            lng = '-'
        text.insert(INSERT, 'Latitude: ' + str(lat) + '\nLongitude: ' + str(lng) + '\n')
        j += 1
    

def clear(event):
    E1text.set('')
    
top = Tk() 
top.title('Google Places API Search')
L1 = Label(top, text="Place") 
L1.pack(side = LEFT) 

E1text=StringVar()

text = Text(top) 
vertical_scrollbar = tk.Scrollbar(top, command=text.yview)
text.config(yscrollcommand=vertical_scrollbar.set)
vertical_scrollbar.pack( side = RIGHT, fill=Y )
text.pack(side = RIGHT) 

E1 = Entry(top, bd =5, text=E1text)
E1.bind('<Return>', func)
E1.bind('<Escape>', clear)

E1.pack(side = LEFT) 

B = Button(top, text ="Search", command = func)
B.pack(side = LEFT)

top.mainloop()


if __name__ == '__main__':
    pass
