This repo is specify for BootCamp at ML1.





### 🧭 Section 1: Terminal Basics & File Management

1. **Navigate to your home directory, then list all hidden files. Which ones are commonly used for configuration?**

   * *Hint: Use `cd`, `ls -a`.*
   
    cd ~
    ls -a

2. **Create a directory named `projects`, then create a file called `README.md` inside it with the text “My Projects”.**

   * *Use `mkdir`, `echo`, `>`.*

    mkdir projects
    echo "My Projects" > projects/README.md

3. **Change the permissions of a file `script.sh` to make it executable only by the owner.**

   * *Use `chmod` with numeric mode.*
    
    chmod 700 script.sh
    
4. **Copy all `.txt` files from the current directory into a folder named `backup`. If it doesn’t exist, create it.**

   * *Use `mkdir -p`, `cp` with globbing.*

    mkdir -p backup && cp *.txt backup/

5. **Write a one-liner that finds all `.log` files under the `/var/log` directory and outputs their filenames and sizes.**

   * *Use `find`, `du`, `-exec`, or `xargs`.*

    find /var/log -name "*.log" -exec du -h {} +

---

### 🔍 Section 2: Text Processing & Command Composition

6. **Write a command that counts the number of times the word “error” appears in a file called `server.log`.**

   * *Use `grep` and `wc`.*
   
    grep -o "error" server.log | wc -l

7. **Print the third column from a CSV file named `data.csv`, assuming it’s comma-delimited.**

   * *Use `cut` or `awk`.*

8. **Write a pipeline that shows the 10 most used commands from your Bash history.**

   * *Use `history`, `awk`, `sort`, `uniq`.*
   
   history | awk '{print $2}' | sort | uniq -c | sort -nr | head -10

9. **Tail a growing log file (`/var/log/syslog`) but also highlight lines that contain the word “failed”.**

   * *Use `tail -f` and `grep --color`.*

    tail -f /var/log/syslog | grep "failed"

10. **Replace all occurrences of the word "foo" with "bar" in all `.txt` files in the current directory.**

    * *Use `sed` in-place editing with globbing.*
    
    sed -i 's/foo/bar/g' *.txt
    
11. **Write a script that accepts a filename as an argument and prints how many lines it contains.**

    #!/bin/bash
if [ -f "$1" ]; then
    lines=$(wc -l < "$1")
    echo "The file $1 has $lines lines."
else
    echo "File not found!"
fi

12. **Create a script that checks if a directory exists; if not, it creates it and echoes “Created!”.**

    #!/bin/bash
if [ ! -d "$1" ]; then
    mkdir -p "$1"
    echo "Created!"
fi

13. **Write a script that takes two numbers from user input and prints their sum.**

    #!/bin/bash
read -p "Enter first number: " num1
read -p "Enter second number: " num2
sum=$((num1 + num2))
echo "Sum: $sum"

14. **Modify a script so it logs all output (both stdout and stderr) into a log file named `run.log`.**

    #!/bin/bash
exec > run.log 2>&1
# Rest of the script...

15. **Write a script that loops over a list of filenames and prints their line count.**

#!/bin/bash
for file in "$@"; do
    lines=$(wc -l < "$file")
    echo "$file: $lines lines"
done
    
### 🌀 Section 4: Conditionals, Loops, and Parameters

16. **Write a script that accepts one argument (a filename). If the file exists and is writable, append “Hello” to it. Otherwise, print an error.**

#!/bin/bash
if [ -w "$1" ]; then
    echo "Hello" >> "$1"
else
    echo "Error: File does not exist or is not writable."
fi

17. **Create a `for` loop in a script that prints numbers 1 through 10, but skips 5.**

#!/bin/bash
for i in {1..10}; do
    if [ "$i" -ne 5 ]; then
        echo "$i"
    fi
done

18. **Using a `while` loop, create a countdown from 10 to 0, printing one number per second.**

#!/bin/bash
count=10
while [ $count -ge 0 ]; do
    echo "$count"
    sleep 1
    ((count--))
done

19. **Write a script that loops through all `.sh` files in a directory and checks whether each one is executable.**

#!/bin/bash
for file in *.sh; do
    if [ -x "$file" ]; then
        echo "$file is executable."
    else
        echo "$file is not executable."
    fi
done

20. **Write a function inside a script that returns the square of a given number. Call the function with input 4.**

#!/bin/bash
square() {
    echo $(( $1 * $1 ))
}
square 4
    

### 🧰 Section 5: System and Process Management

21. **Find and kill all running processes named `node`.**

    * *Use `ps`, `grep`, `awk`, `kill`.*
    
    kill $(ps aux | grep '[n]ode' | awk '{print $2}')
    
