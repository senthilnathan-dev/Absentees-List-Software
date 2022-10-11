# ALS-(Absentees listing software)

<!-- Lastly updated for the version v2022.1.2
on 16-01-2022 -->
**Table of content:**  

* [Summary](#Summary).  
* [Installation](#Installation)
  * [Guide to install](#Guide-to-install)
* [Usage](#Usage)
* [Roadmap](#Roadmap)

---

## Summary

This project aims to develop a desktop application that determines the absentees list from a given text file which contains the usernames of the students. This software is specifically developed for '[canvas instruture][1]'.

---

## Installation

For installing the latest version see '[Releases][2]'. This software is built for windows OS in mind, So it may or may not be compatible on Mac or Linux OS. since this software wasn't tested on these environments.

### Guide to install

* Download the installer from the [Realeases][2].  
  * If any warning message is thrown. Don't worry just download the file.

* Open the file once installed. By default windows defender throws a window indicating `Don't run`.

![windows defender][3]  

* Just click `more info` and click on the `Run anyway`  

* Then choose the location to be installed and click away the install button.  

---

## Usage

**For use by Command Line Interface(CLI):**

Open the application's  `ALS.exe` file. it will show optionns
 type the appropriate options to perform the desired task.
 for more help on CLI options refer [help][help.txt].

<!-- **For use by Graphical User Interface(GUI):** -->
---
<!-- ## Support -->

## Roadmap

- [ ] Create a Graphical User Interface.  
- [ ] adding a functionality for relative absentees list generation which will be useful for absentees for periods in a row.  

## Project status

Currently active for development.

<!-- ## License -->

[1]: https://www.instructure.com/en-au 'Canvas'
[2]: https://github.com/libertarian-senthil/Absentees-List-Software/releases 'Git-Hub Releases'
[3]: Src/Data/Windows_defender.jpg 'windows defender'
[help.txt]: Src/Data/help.txt 'help'
