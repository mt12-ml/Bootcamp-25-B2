## Todays Progress /  Learning
### find all the names of users
	grep -r "" | awk '/User=/ {print $4}'

### find all the errors
	grep -r "ERROR"

### Print Your Name
### Write a script that stores your name in a variable and prints:
### "Hello, [YourName]!"

	name="Hamza"
	echo "Hello $name"
	Hello Hamza

### Create and Navigate
### Create a directory named practice, move into it, and create a file named notes.txt.

	mkdir practice
	cd practice
	touch notes.txt

### Find .txt Files:
### List all .txt files in the current directory and subdirectories.

	 find . -name '*.txt'

### Create a script that copies all .log files from /var/log (or a mock folder) to a backup/ directory with a timestamp.

	 cp -r logs/ backup/

### 🧭 Section 1: Terminal Basics & File Management

### 1. Navigate to your home directory, then list all hidden files. Which ones are commonly used for configuration?

	cd c:/users/dell    # (Home directory for Windows)
	
	ls -a

### 2. Create a directory named `projects`, then create a file called `README.md` inside it with the text “My Projects”.

	mkdir projects
	cd projects
	echo "My Projects" >> readme.md

### 3. Change the permissions of a file `script.sh` to make it executable only by the owner.

	sudo chmod 700 script.sh

### Copy all `.txt` files from the current directory into a folder named `backup`. If it doesn’t exist, create it.

	mkdir -p backup
	touch text1.txt
	touch text2.txt
	ls backup/
	#Output: logs/  text1.txt  text2.txt

### 5. Write a one-liner that finds all `.log` files under the `/var/log` directory and outputs their filenames and sizes.

	cd /var/log
	du -h *.log


### 6. Write a command that counts the number of times the word “error” appears in a file called `server.log`.

	grep "ERROR" server.log | wc -l

### 7. Print the third column from a CSV file named `data.csv`, assuming it’s comma-delimited.

	cut -d ',' -f 3 AmesHousing.csv

### 8. Write a pipeline that shows the 10 most used commands from your Bash history.

	history |  cut -c7- | uniq -c | sort -nr | head -n 10
 ```
	OUTPUT:
      2  nano script2.sh
      2  nano readme.md
      2  ls
      2  ls
      2  history | cut -d' ' -f4- | uniq -c | sort -n
      2  history | cut -d' ' -f4- 10 | uniq -c | sort -n
      2  history |  cut -c7- | sort  | uniq -c | sort -n | head -n 10
      2  cd ..
      1 ET_LOG=${LOG_FILES[$RANDOM % ${#LOG_FILES[@]}]};   echo "$MESSAGE" >> "$TARGET_LOG"; done
      1  git add readme.md

```
### 9. Tail a growing log file (`/var/log/syslog`) but also highlight lines that contain the word “failed”.

	tail -f system.log | grep --color=always "FAILED"

### 10. Replace all occurrences of the word "foo" with "bar" in all `.txt` files in the current directory.

	sed -i 's/foo/bar/g' *.txt

### 11. Write a script that accepts a filename as an argument and prints how many lines it contains.

    ```bash
    #!/bin/bash
	echo "Number of lines in $1 `wc -l < $1`"
    ```
	Command:
	```
	bash -i lines.sh text1.txt
	```

### 12. **Create a script that checks if a directory exists; if not, it creates it and echoes “Created!”.**
	```bash
	#!/bin/bash
	if [[-e "$1"]]; then
		echo "Directory already exists"
	else
		mkdir "$1"
		echo "Created"

    ```

	```
	bash -i create.sh "logs"
	# Output: Directory already exists

	bash -i create.sh "new"
	#Output: Created
	```
### 13. Write a script that takes two numbers from user input and prints their sum.

    ```bash
	#!/bin/bash
	read -p "Enter the first number: " num1
	read -p "Enter the second number: " num2
	sum=$((num1 + num2))
	echo "The sum is: $sum"
	```
USAGE:
```
	bash -i add.sh
	# Enter the first number: 21
	# Enter the second number: 2
	# The sum is: 23

```

### 14. Modify a script so it logs all output (both stdout and stderr) into a log file named `run.log`.**
	```bash
	#!/bin/bash
	"$1 $2" > run.log 2>&1
	```

### 15. Write a script that loops over a list of filenames and prints their line count.
	```bash	
	#!/bin/bash
	for file in "$@"; do
		wc -l "${file}"

	```

	```
	bash -i all_lines.sh "text1.txt" "text2.txt"
	# 5 text1.txt
	# 0 text2.txt

	```

### 16. Write a script that accepts one argument (a filename). If the file exists and is writable, append “Hello” to it. Otherwise, print an error.
```bash
	# append.sh
	#!/bin/bash
	if [[ -e "$1" && -w "$1" ]]; then
        echo "Hello" >> "$1"
        echo "Appended hello"
	else
        echo "ERROR"
	fi
```

### 17. Create a `for` loop in a script that prints numbers 1 through 10, but skips 5.
```bash
	# print10.sh
	#!/bin/bash
	for i in {1..10}; do
        if [[ "${i}" -ne 5 ]]; then
                echo "${i}"
        fi
	done


```
### 18. Using a `while` loop, create a countdown from 10 to 0, printing one number per second.
```bash
	#!/bin/bash
	c = 10
	while [[ c -ge 1 ]]; do
		echo "${i}"
		c=$((c-1))
		sleep 1
	done

```

### 20. Write a function inside a script that returns the square of a given number. Call the function with input 4.
	
```bash	
	# square.sh
	#!/bin/bash

	echo $(($1 * $1))

```


