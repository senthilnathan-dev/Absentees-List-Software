# ALS Absentees list software 

__**Specifications and procedures for version v1.0.0**__

**Table of contents:**  

* [FAQ's](#FAQ's)  

* [Language and tools preferred to develop this software](#Language-and-tools-preferred-to-develop-this-software)  

* [Procedure in developing this software](#Procedure-in-developing-this-software)  
  * [Start](#Start)
  * [Name List, User Names, Absentees namelist](#NameList,-User-Names,-Absentees-namelist)
  * [Generate absentees](#Generate-absentees)
  * [GUI](#GUI)
  * [Stop](#Stop)

---

## FAQ's

1 What is the purpose of developing this software?  

* To generate absentees list from given text file(i.e. Canvas generated text files).  

2 Who are the target users?  

* Users can be anyone who uses '[Canvas instructure][canvas]' software as learning platform.  

3 How it will be useful to the users:  

* It will reduce the time to create a separate absentees list thereby comparing with the students namelist list.  

---

## Language and tools preferred to develop this software

| Description | Tools |
|:---:|:---:|
| Language | Python |
| Storage | JSON,txt files |
| Extract Data | Web sraping |
| VCS | git |
|remote repo | [GitHub][GitHub] |

---

## Procedure in developing this software

### Start

Setup the development environment and create a basic project structure.

### Name List, User Names, Absentees namelist

* Collect the `namelist` from any source that must be sorted accordingly and it must be an `UTF-8` encoded text file.  

* Collect the `Usernames` from Canvas site using web scrapping methods.  

* Store the `Usernames` with their respective Names from the `Namelist` in a JSON file.  

* Collect the `present` namelist from any source but it must be an [`UTF-8`][^1] encoded text file.  

### Generate absentees

* Extract the data from the present namelist, filter out the unwanted details and remove the other class students names incase if they're included.  

* Remove the duplicates since users can join from multiple sources that causes multiple usernames in the present list.  
* store the filtered namelist in a JSON file.

* Compare the filtered namelist with the the JSON file encompassing both usernames and students names.  

* Generate absentees list and store it in a list temporarily.  

### GUI

* Create a GUI for use in desktop.  

* It must contain the following widgets:
 1 A main frame that contains text box which shows the absentees list(located upper left side).  
 2 A secondary frame contained few buttons for added functionality(located full right side).  
 3 A text box in the main frame shows the status of the other process running at background.  

### Stop

Once after generated the absentees list ask wait for the termination of the process(i.e. users exits the application).  

---

<!-- Links and references -->  
[canvas]: https://canvas.instructure.com/ 'Canvas login page'  
[GitHub]: https://github.com/libertarian-senthil/Absentees-List-Software.git 'GitHub page'
[^1]: https://blog.hubspot.com/website/what-is-utf-8 'UTF-8'
