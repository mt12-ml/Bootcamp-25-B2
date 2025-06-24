----------Bash documentation---------
bash task:


### �� Section 1: Terminal Basics & File Management

1. **Navigate to your home directory, then list all hidden files. Which ones are commonly used for configuration?**

   * *Hint: Use `cd`, `ls -a`.*

Solution:  'cd ~ && ls -a'
    ** for navigation we use, "cd ~", to list all the hidden files we use 'ls -a'. '.bashrc','.gitconfig','bash_profile' are commonly used for configuration.

2. **Create a directory named `projects`, then create a file called `README.md` inside it with the text “My Projects”.**

   * *Use `mkdir`, `echo`, `>`.*
Solutionn :    mkdir projects              # create a directory
               touch README.md             # touch is used to create an empty file
               echo "My Projects" << README.md            #echo write/print the text in file '<<' is used to append the text in specified file

3. **Change the permissions of a file `script.sh` to make it executable only by the owner.**

   * *Use `chmod` with numeric mode.*
Solution:     we used 'chmod 700 script.sh'      # 7 -> - 7 (owner): Read (4) + Write (2) + Execute (1) = 7 
                                               #  0 (group): No permissions
                                               #  0 (others): No permissions



4. **Copy all `.txt` files from the current directory into a folder named `backup`. If it doesn’t exist, create it.**

   * *Use `mkdir -p`, `cp` with globbing.*

solution:    ' mkdir -p backup && cp *.txt backup/'


5. **Write a one-liner that finds all `.log` files under the `/var/log` directory and outputs their filenames and sizes.**

   * *Use `find`, `du`, `-exec`, or `xargs`.*
Solution:

        find /var/log -type f -name "*.log" -exec du -h {} + 
        find /var/log -type f -name '*.log' -exec du -h {} +          # -type f means only files , -name *.log  -exec du(disk usage) -h (human readable)

### �� Section 2: Text Processing & Command Composition

6. **Write a command that counts the number of times the word “error” appears in a file called `server.log`.**

   * *Use `grep` and `wc`.*
SOLUTION:  ' grep -o  "ERROR" auth.log | wc -1 '      ####- grep -o "error": Finds every individual occurrence of the word "error" and prints each on a new line.
                                                      ####- wc -l: Counts how many lines of output there are—each line corresponds to one match.


7. **Print the third column from a CSV file named `data.csv`, assuming it’s comma-delimited.**

   * *Use `cut` or `awk`.*
solution:   'cut -d ',' -f3 data.csv' ### -d -> deleimer,   -f3 -> third column

8. **Write a pipeline that shows the 10 most used commands from your Bash history.**

   * *Use `history`, `awk`, `sort`, `uniq`.*

solution:   ' history | awk '{print $2}' | sort | uniq  -c | sort -nr | head -10 '   
            ####- history: Lists all previously used commands.
                - awk '{print $2}': Extracts the actual command (ignores line numbers).
                - sort: Sorts them alphabetically to group identical commands together.
                - uniq -c: Counts how many times each command appears.
                - sort -nr: Sorts the results numerically in reverse (most used first).
                - head -10: Displays just the top 10

  

9. **Tail a growing log file (`/var/log/syslog`) but also highlight lines that contain the word “failed”.**

   * *Use `tail -f` and `grep --color`.*
SOLUTION:    $ tail -f app.log | grep --color=auto --line-buffered "DEBUG"


10. **Replace all occurrences of the word "foo" with "bar" in all `.txt` files in the current directory.**

    * *Use `sed` in-place editing with globbing.*


SOLUTION:   sed -i 's/foo/bar/g' *.txt                 #####- sed: Stream editor for filtering and transforming text -i -> INPLACE, 's/foo/bar/g -> s-> sibtitute,
                                                               foo-> word to be replaced, bar-> replace, g-> for all instances 

----------------------------------------------------------------------------------------------------------------------

### �� Section 3: Bash Scripting Foundations

11. **Write a script that accepts a filename as an argument and prints how many lines it contains.**

    ```bash
    #!/bin/bash
    # Your logic here
    ```

12. **Create a script that checks if a directory exists; if not, it creates it and echoes “Created!”.**
 solution:   write doen the script and execute onn bash
13. **Write a script that takes two numbers from user input and prints their sum.**
solution:   write doen the script and execute onn bash
    * *Use `read`, `expr`, or arithmetic expansion.*
solution:   write doen the script and execute onn bash
14. **Modify a script so it logs all output (both stdout and stderr) into a log file named `run.log`.**

    * *Use redirection: `>`, `2>&1`.*

15. **Write a script that loops over a list of filenames and prints their line count.**
solution:   write doen the script and execute onn bash
---

### �� Section 4: Conditionals, Loops, and Parameters

16. **Write a script that accepts one argument (a filename). If the file exists and is writable, append “Hello” to it. Otherwise, print an error.**

solution:   write doen the script and execute onn bash

17. **Create a `for` loop in a script that prints numbers 1 through 10, but skips 5.**
solution:   write doen the script and execute onn bash
18. **Using a `while` loop, create a countdown from 10 to 0, printing one number per second.**
solution:   write doen the script and execute onn bash
19. **Write a script that loops through all `.sh` files in a directory and checks whether each one is executable.**
solution:   write doen the script and execute onn bash
20. **Write a function inside a script that returns the square of a given number. Call the function with input 4.**
solution:   write doen the script and execute onn bash
---

### �� Section 5: System and Process Management


21. **Find and kill all running processes named `node`.**

    * *Use `ps`, `grep`, `awk`, `kill`.*

------------------------------------------------

solution: ps aux | grep '[n]ode' | awk '{print $2}' | xargs kill


22. **Write a one-liner to check disk usage and alert if it exceeds 90%.**

    * *Use `df`, `awk`, `if`.*

solution:         [ $(df -hP | awk 'NR>1 && int($5) > 90 {print $0}' | wc -l) -gt 0 ] && echo "⚠️ Disk usage exceeds 90%!" || echo "✅ Disk usage is under control."

-------------------------------------------------
23. **Create a script that backs up a directory (e.g., `~/projects`) to `~/backup` with a timestamp.**
solution:   
-------------------------
24. **Write a cron expression that runs a script every weekday at 7:30 AM.**

    * *Use `crontab -e`.*
solution:     30 7 * * 1-5 /path/to/your/script.sh  
              crontab -e
              

25. **Monitor CPU and memory usage for the top 5 processes every 5 seconds.**

    * *Use `watch`, `top`, or `ps`.*


solution:    watch -n 5 "ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head -n 6"
---

### �� Section 6: Environment & Advanced Use

26. **Temporarily change the value of the `PATH` variable in your terminal session to include a folder `~/scripts`.**

    * *Use `export`.*

27. **Explain what `.bashrc` and `.bash_profile` do, and make a small change that aliases `ll` to `ls -alF`.**

         - .bashrc
- Runs every time you start a new interactive non-login shell (like opening a new terminal tab).
          - .bash_profile
- Runs when you start a login shell (like when logging in via SSH or a terminal login).
          

28. **Write a script that downloads a file from a given URL and checks if the download was successful.**

    * *Use `curl` or `wget`, test exit codes.*
solution:   write doen the script and execute onn bash

29. **What’s the difference between running `source script.sh` and `./script.sh`? When would you use each?** 
source script.sh (or . script.sh)
- Runs the script within the current shell.uused when You want the script to modify your current shell session.


 ./script.sh
- Executes the script in a new subshell (a separate shell process). used when You're executing a program or automation task.






