# ctf_wordlist
> This is a basic friendly wordlist with basic entries like first middle last name . This will create combination of not all possible wordlist but *practical or readable wordlist*
> There is a option to append numbers at the end of every words. This will join all possible numbers with in your given range to all the words,
> This wordlist contain both Capitalised and Normal First charater of all First Middle Last Name

## USAGE

```
python wordlist_generator -(arguments)
```

```python
python wordlist_generator -fname -mname -lname -f
```

### based on user input 

```python
python wordlist_generator -fname -mname -lname
```
>available arguments 

`-fname` : first name (required) <br/>
`-mname` : middle name (optional) <br/>
`-lname`  : last name (optional) <br/>

### CAPITALIZE first character in already existing wordlist
`python wordlist_generator -f <path to your wordlist>`

### DEVELOPMENT
There is `-r` argument which will delete already generated wordlists by this tool.




