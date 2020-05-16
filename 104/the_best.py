
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n9908544
#    Student name: Arin Kim
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).  81023PT
#
#--------------------------------------------------------------------#



#-----Assignment Description-----------------------------------------#
#
#  The Best, Then and Now
#
#  In this assignment you will combine your knowledge of HTMl/XML
#  mark-up languages with your skills in Python scripting, pattern
#  matching, and Graphical User Interface design to produce a useful
#  application that allows the user to preview and print lists of
#  top-ten rankings.  See the specification document accompanying this
#  file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements for helpful functions.  You
# should be able to complete this assignment using these
# functions only.  Note that not all of these functions are
# needed to successfully complete this assignment.
# YOU MAY NOT USE ANY OTHER MODULES WITHOUT PRIOR APPROVAL.

# The function for opening a web document given its URL.
# (You WILL need to use this function in your solution,
# either directly or via our "download" function.)
from urllib.request import urlopen

# Import the standard Tkinter functions. (You WILL need to use
# these functions in your solution.)
from tkinter import *

# Functions for finding all occurrences of a pattern
# defined via a regular expression, as well as
# the "multiline" and "dotall" flags.  (You do NOT need to
# use these functions in your solution, because the problem
# can be solved with the string "find" function, but it will
# be difficult to produce a concise and robust solution
# without using regular expressions.)
from re import findall, finditer, MULTILINE, DOTALL

#
#--------------------------------------------------------------------#



#-----Downloader Function--------------------------------------------#
#
# This is our function for downloading a web page's content and both
# saving it on a local file and returning its source code
# as a Unicode string. The function tries to produce a
# meaningful error message if the attempt fails.  WARNING: This
# function will silently overwrite the target file if it
# already exists!  NB: You should change the filename extension to
# "xhtml" when downloading an XML document.  (You do NOT need to use
# this function in your solution if you choose to call "urlopen"
# directly, but it is provided for your convenience.)
#
def download(url = 'http://www.wikipedia.org/',
             target_filename = 'download',
             filename_extension = 'html'):

    # Import an exception raised when a web server denies access
    # to a document
    from urllib.error import HTTPError

    # Open the web document for reading
    try:
        web_page = urlopen(url)
    except ValueError:
        raise Exception("Download error - Cannot find document at URL '" + url + "'")
    except HTTPError:
        raise Exception("Download error - Access denied to document at URL '" + url + "'")
    except:
        raise Exception("Download error - Something went wrong when trying to download " + \
                        "the document at URL '" + url + "'")

    # Read its contents as a Unicode string
    try:
        web_page_contents = web_page.read().decode('UTF-8')
    except UnicodeDecodeError:
        raise Exception("Download error - Unable to decode document at URL '" + \
                        url + "' as Unicode text")

    # Write the contents to a local text file as Unicode
    # characters (overwriting the file if it
    # already exists!)
    try:
        text_file = open(target_filename + '.' + filename_extension,
                         'w', encoding = 'UTF-8')
        text_file.write(web_page_contents)
        text_file.close()
    except:
        raise Exception("Download error - Unable to write to file '" + \
                        target_file + "'")

    # Return the downloaded document to the caller
    return web_page_contents

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

##### DEVELOP YOUR SOLUTION HERE #####



# Defind lists for preveiw and export buttons
# old html file address

html_address = ['SoundCloud this week.html', 'Official Singles Chart.html']

# current url address

url_address = ['https://soundcloud.com/charts/top',
               'https://www.officialcharts.com/charts/singles-chart-update/']

# Html image address

image_address = ['http://icons.iconarchive.com/icons/designbolts/ios8-style-social/512/Soundcloud-icon.png',
                 'https://d38v16rqg5mb6e.cloudfront.net/wp-content/uploads/2015/01/playmusiclogo-1024x632.jpg']

# Pop up image file names

pop_up_image = ['soundcloud.gif', 'music logo.gif']

# Defind every single regex for preveiw and export buttons
# soundcloud regular expression
soundcloud_title_regex = '<a itemprop="url" href=".*?">(.*?)</a>'
soundcloud_singer_regex = 'by <a href=".*?">(.*?)</a>'

# aussie music chart regular expression
aussie_title_regex = '<a href="/search/singles/.+?/">(.*?)</a>'
aussie_singer_regex = '<a href="/artist/.+?/">(.*?)</a>'

# Define html code for making html
startpoint_html = '''<!DOCTYPE html>
        <!-- Satrt to write html correctly --!>
    <html>
      <head>
          <title>'''

table_style = '''          </title>
      <style>      <!-- Define the style of table --!>
      table { border-collapse: collapse; }
      td { border: 1px solid black; }
      td:nth-child(1){ width:50px; }
      td:nth-child(1){ text-align:center; }
      td:nth-child(2){ width:200px; }
      td:nth-child(3){ width:150px; }
      th { text-align:left; }
      </style>
      </head>
      <body>
      <!-- Put image on centre --!>
      <center><img src="'''
put_image = '''"
       	  alt="music Icon" width=40% ></center>
      <h2 align='center'>'''

table_stytle2 = '''          </h2>
      
      <!-- Display current date and month --!>
        <p align='center'><span id="date"></span></p>
      <script>
	    var dt = new Date();
	    document.getElementById("date").innerHTML = (("0"+dt.getDate()).slice(-2)) +"/"+ (("0"+(dt.getMonth()+1)).slice(-2));
      </script>
      <table border="1"  align='center'>
    '''

header_of_table = '''      <tr bgcolor="gray"> <!-- Make the first row of table with gray background colour --!>
           <th>Rank</th>
           <th id="valign1">Song title</th>
           <th id="valign2">Singer</th>
          </tr>
    '''

endpoint_html = '''
      </body>
    </html> <!-- Close html --!>'''



# Create a TK window
window = Tk()
window.geometry("600x600")
window.configure(bg = 'white')

# Give the window a title
window.title('Best Then and Now')

# Introduce Integer values to make the buttons
# can be selected only one button by once
buttons_status = IntVar()


# Create a Label widget to displays the title and main image
top_ten = Label(window, text = 'The List Of Top Ten',
                font = ('Times', 32), bg = 'white')

topten_image = PhotoImage(file = 'top ten.gif') 

Label(window, image = topten_image).place(x = 160, y = 70)



# Define export button for creating new html file about
# each condition of sites or old html file
def export_html():

    # Get integer value when user hits button
    user_hits = buttons_status.get()

    # if user hits value 1 button
    if user_hits == 1:
        write_old_html('Old soundcloud html', 'Rankig of soundcloud',
                        html_address[0], '04/01',image_address[0],
                       soundcloud_title_regex, soundcloud_singer_regex)

    # if user hits value 2 button
    elif user_hits == 2:
        write_current_html('Current soundcloud', 'Rankig of soundcloud',
                          url_address[0],image_address[0],
                           soundcloud_title_regex, soundcloud_singer_regex)

    # if user hits value 3 button
    elif user_hits == 3:
        write_old_html('Old aussie music chart', 'Rankig of aussie music',
                        html_address[1], '17/01',image_address[1],
                       aussie_title_regex, aussie_singer_regex)

    # if user hits value 4 button
    elif user_hits == 4:
        write_current_html('Current aussie music chart', 'Rankig of aussie music',
                          url_address[1],image_address[1],
                           aussie_title_regex, aussie_singer_regex)


    # Change the export button state to disable after clicking
    export_button['state'] = DISABLED
        

# Define the function for creating html file from old file with 7 parameter for making them changable
# even if the information of html is changed.
def write_old_html(window_title, table_title, html_name, date, address, title_regex, artist_regex):

    # Open html file which is already downloaded
    html_source = open(html_name, encoding = 'UTF-8').read()

    # Create html file to write
    html_file = open(window_title + '.html','w', encoding = 'UTF-8')

    # Start to write html code with titles with old date and month
    # and provide the style for table with suitable image
    html_file.write(startpoint_html)
    html_file.write('''          ''' + window_title)
    html_file.write(table_style + address)
    html_file.write(put_image)
    html_file.write('''          ''' + table_title)
    html_file.write('''          </h2>
      
      <!-- Display date and month of this html file --!>
        <p align='center'>''')
    html_file.write('''       '''+ date + '''</p>
      <table border="1"  align='center'>
    ''')

    html_file.write(header_of_table)

    # find all of information about title and artist from html source
    title_list = findall(title_regex, html_source)
    singer_list = findall(artist_regex, html_source)

    # Write the title and artist with each ranking into table
    for names in range(10):
        rank_num = names + 1
        html_file.write('       <tr><td>'+ str(rank_num) + '</td><td>'
                              + title_list[names]+'</td><td>'
                              + singer_list[names] +'</td></tr>\n')


    # Write local address to connect original html file
    html_file.write('''      </table>
                 <p align='center'><a href="''' + html_name +'''" >'''+
                    html_name +'''</a></p>''')

    # Write end point of html
    html_file.write(endpoint_html)

    # Close html
    html_file.close()


# Define the function for creating html file from url with 6 parameter for making them changable
# even if the information of html is changed.
def write_current_html(window_title, table_title, site_name, address, title_regex, artist_regex):

    
    # Create html file to write
    html_file = open(window_title + '.html','w', encoding = 'UTF-8')

    # Open the url for taking information
    url_open = urlopen(site_name)
    html_source = url_open.read().decode('UTF-8')

    # Start to write html code with titles wiht current date and month
    # and provide the style for table with suitable image
    html_file.write(startpoint_html)
    html_file.write('''          ''' + window_title)
    html_file.write(table_style + address)
    html_file.write(put_image)
    html_file.write('''          ''' + table_title)
    html_file.write(table_stytle2)

    html_file.write(header_of_table)

    # find all of information about title and artist from html source
    title_list = findall(title_regex, html_source)
    singer_list = findall(artist_regex, html_source)

    # Write the title and artist with each ranking into table
    for names in range(10):
        rank_num = names + 1
        html_file.write('       <tr><td>'+ str(rank_num) + '</td><td>'
                              + title_list[names]+'</td><td>'
                              + singer_list[names] +'</td></tr>\n')

    html_file.write('''      </table>
                 <p align='center'><a href="''' + site_name +'''" >'''+
                    site_name +'''</a></p>''')

    # Write end point of html
    html_file.write(endpoint_html)

    # Close html
    html_file.close()



# Define the function for opening preview pop up
def open_preview():
    user_hits = buttons_status.get()

    # if user hits value 1 button
    if user_hits == 1:
        old_preview(html_address[0], 'Old top ten list of soundcloud',
                    pop_up_image[0], soundcloud_title_regex, soundcloud_singer_regex)

    # if user hits value 2 button
    elif user_hits == 2:
        current_preview(url_address[0], 'Current top ten list of soundcloud',
                    pop_up_image[0], soundcloud_title_regex, soundcloud_singer_regex)

    # if user hits value 3 button
    elif user_hits == 3:
        old_preview(html_address[1], 'Old top ten list of aussie top10',
                    pop_up_image[1], aussie_title_regex, aussie_singer_regex)

    # if user hits value 4 button
    elif user_hits == 4:
        current_preview(url_address[1], 'Current top ten list of aussie top10',
                    pop_up_image[1], aussie_title_regex, aussie_singer_regex)

    # After clicking preview button, the export button's state will be changed to active
    export_button['state'] = ACTIVE



# Define the old preview button with 5 parameter for making them changable
# even if the information of html is changed.
def old_preview(html_file_name, window_title, image_file, title_regex, artist_regex):
    global popup_image
    
    # Open the html file for old list
    html_source = open(html_file_name, encoding = 'UTF-8').read()

    # Make the window for preview wiht white background colour
    preview_window = Toplevel()
    preview_window.geometry("570x600")
    preview_window.configure(bg = 'white')

    # Open and add a image in preview window

    popup_image = PhotoImage(file = image_file)    
    Label(preview_window, image = popup_image).place(x = 80, y = 10)
    
    # add the title
    Label(preview_window, text = window_title, font = ('Arial', 20), bg = 'white').place(x =100, y = 320)

    # Make the list of top ten

    listbox = Listbox(preview_window, width=50, font = ('Times', 13))
    listbox.place(x=50, y=350)


    # find the title list and singer list from html source
    title_list = findall(title_regex, html_source)
    singer_list = findall(artist_regex, html_source)

    # Input the every single items from list in to the box
    for names in range(10):
        rank_num = names + 1
        listbox.insert(END, '#'+str(rank_num)+'  '+ title_list[names]+'   ' + singer_list[names])



# Define the current preview button with 5 parameter for making them changable
# even if the information of html is changed.
def current_preview(site_name, window_title, image_file, title_regex, artist_regex):

    global popup_image
    
    # Open the url for current list
    url_open = urlopen(site_name)
    html_source = url_open.read().decode('UTF-8')

    # Make the window for preview
    preview_window = Toplevel()
    preview_window.geometry("570x600")
    preview_window.configure(bg = 'white')
    
    # Open and add a image in preview window

    popup_image = PhotoImage(file = image_file)    
    Label(preview_window, image = popup_image).place(x = 80, y = 10)
    
    # add the title
    Label(preview_window, text = window_title, font = ('Arial', 20), bg = 'white').place(x =100, y = 320)

    # Make the list of top ten

    listbox = Listbox(preview_window, width=50, font = ('Times', 13))
    listbox.place(x=50, y=350)
    
    # find the title list and singer list from html source
    title_list = findall(title_regex, html_source)
    singer_list = findall(artist_regex, html_source)

    # Input the every single items from list in to the box
    for names in range(10):
        rank_num = names + 1
        listbox.insert(END, '#'+str(rank_num)+'  '+ title_list[names]+'   ' + singer_list[names])





# Create two LabelFrame widgets to pack the pairs of radiobuttons
Soundcloud_buttons = LabelFrame(window, relief = 'groove',
                                font = ('Arial', 20), bg = 'white',
                                borderwidth = 2, text = 'Sound Cloud')

Aussie_top10_buttons = LabelFrame(window, relief = 'groove',
                                font = ('Arial', 20), bg = 'white',
                                borderwidth = 2, text = 'Aussie music')


# Make radio buttons for old list and current list of
# sound cloud top ten.

soundcloud_old_button = Radiobutton(Soundcloud_buttons, text = 'Old', bg = 'white',
                                    variable = buttons_status, value = 1,
                                    font = ('Arial', 15))
soundcloud_current_button = Radiobutton(Soundcloud_buttons, text = 'Current', bg = 'white',
                                    variable = buttons_status, value = 2,
                                    font = ('Arial', 15))
                                    

# Make radio buttons for old list and current list of
# bilboard top ten.

aussie_top10_old_button = Radiobutton(Aussie_top10_buttons, text = 'Old', bg = 'white',
                                    variable = buttons_status, value = 3,
                                    font = ('Arial', 15))
aussie_top10_current_button = Radiobutton(Aussie_top10_buttons, text = 'Current', bg = 'white',
                                    variable = buttons_status, value = 4,
                                    font = ('Arial', 15))

# Make usual buttons for Preview and Export


preview_button = Button(window, text = 'Preview', font = ('Arial', 15),
                        command = open_preview, state = ACTIVE)
export_button = Button(window, text = 'Export', font = ('Arial', 15),
                        command = export_html, state = DISABLED)


# Use the grid function to pack each buttons into label frame

soundcloud_old_button.grid(row = 1, sticky = 'w')
soundcloud_current_button.grid(row = 2, sticky = 'w')
aussie_top10_old_button.grid(row = 1 , sticky = 'w')
aussie_top10_current_button.grid(row = 2, sticky = 'w')


# Use the x coordinate and y coordinate to put the main widgets
# into the root window

top_ten.place(x = 130, y = 0)
Soundcloud_buttons.place(x = 100, y = 400)
Aussie_top10_buttons.place(x = 370, y = 400)
preview_button.place(x = 100, y = 550)
export_button.place(x = 400, y = 550)

window.mainloop()
