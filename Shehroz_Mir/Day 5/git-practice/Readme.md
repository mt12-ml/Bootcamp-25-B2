1. **Navigate to your home directory, then list all hidden files. Which ones are commonly used for configuration?**

  cd ~
  ls -a

**Write a command that counts the number of times the word “error” appears in a file called `server.log`.**


$ grep -oi "error" app.log | wc -l
8
