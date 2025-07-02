

### 🧭 Section 1: Terminal Basics & File Management

1. **Navigate to your home directory, then list all hidden files. Which ones are commonly used for configuration?**

   * *Hint: Use `cd`, `ls -a`.*

2. **Create a directory named `projects`, then create a file called `README.md` inside it with the text “My Projects”.**

   * *Use `mkdir`, `echo`, `>`.*

3. **Change the permissions of a file `script.sh` to make it executable only by the owner.**

   * *Use `chmod` with numeric mode.*

4. **Copy all `.txt` files from the current directory into a folder named `backup`. If it doesn’t exist, create it.**

   * *Use `mkdir -p`, `cp` with globbing.*

5. **Write a one-liner that finds all `.log` files under the `/var/log` directory and outputs their filenames and sizes.**

   * *Use `find`, `du`, `-exec`, or `xargs`.*

---

### 🔍 Section 2: Text Processing & Command Composition

6. **Write a command that counts the number of times the word “error” appears in a file called `server.log`.**

   * *Use `grep` and `wc`.*

7. **Print the third column from a CSV file named `data.csv`, assuming it’s comma-delimited.**

   * *Use `cut` or `awk`.*

8. **Write a pipeline that shows the 10 most used commands from your Bash history.**

   * *Use `history`, `awk`, `sort`, `uniq`.*

9. **Tail a growing log file (`/var/log/syslog`) but also highlight lines that contain the word “failed”.**

   * *Use `tail -f` and `grep --color`.*

10. **Replace all occurrences of the word "foo" with "bar" in all `.txt` files in the current directory.**

    * *Use `sed` in-place editing with globbing.*

---

### 🧠 Section 3: Bash Scripting Foundations

11. **Write a script that accepts a filename as an argument and prints how many lines it contains.**

    ```bash
    #!/bin/bash
    # Your logic here
    ```

12. **Create a script that checks if a directory exists; if not, it creates it and echoes “Created!”.**

13. **Write a script that takes two numbers from user input and prints their sum.**

    * *Use `read`, `expr`, or arithmetic expansion.*

14. **Modify a script so it logs all output (both stdout and stderr) into a log file named `run.log`.**

    * *Use redirection: `>`, `2>&1`.*

15. **Write a script that loops over a list of filenames and prints their line count.**

---

### 🌀 Section 4: Conditionals, Loops, and Parameters

16. **Write a script that accepts one argument (a filename). If the file exists and is writable, append “Hello” to it. Otherwise, print an error.**

17. **Create a `for` loop in a script that prints numbers 1 through 10, but skips 5.**

18. **Using a `while` loop, create a countdown from 10 to 0, printing one number per second.**

19. **Write a script that loops through all `.sh` files in a directory and checks whether each one is executable.**

20. **Write a function inside a script that returns the square of a given number. Call the function with input 4.**

---

### 🧰 Section 5: System and Process Management

21. **Find and kill all running processes named `node`.**

    * *Use `ps`, `grep`, `awk`, `kill`.*

22. **Write a one-liner to check disk usage and alert if it exceeds 90%.**

    * *Use `df`, `awk`, `if`.*

23. **Create a script that backs up a directory (e.g., `~/projects`) to `~/backup` with a timestamp.**

24. **Write a cron expression that runs a script every weekday at 7:30 AM.**

    * *Use `crontab -e`.*

25. **Monitor CPU and memory usage for the top 5 processes every 5 seconds.**

    * *Use `watch`, `top`, or `ps`.*

---

### 🌐 Section 6: Environment & Advanced Use

26. **Temporarily change the value of the `PATH` variable in your terminal session to include a folder `~/scripts`.**

    * *Use `export`.*

27. **Explain what `.bashrc` and `.bash_profile` do, and make a small change that aliases `ll` to `ls -alF`.**

28. **Write a script that downloads a file from a given URL and checks if the download was successful.**

    * *Use `curl` or `wget`, test exit codes.*

29. **What’s the difference between running `source script.sh` and `./script.sh`? When would you use each?**
