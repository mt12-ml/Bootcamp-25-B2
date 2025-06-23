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
    
    
### 🧰 Section 5: System and Process Management

21. **Find and kill all running processes named `node`.**

    * *Use `ps`, `grep`, `awk`, `kill`.*
    
    kill $(ps aux | grep '[n]ode' | awk '{print $2}')
