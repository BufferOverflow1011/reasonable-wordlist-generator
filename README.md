# ctf_wordlist
> This is a basic friendly wordlist with basic entries like first middle last name . This will create combination of not all possible wordlist but *practical or readable wordlist*.</br>
> There is a option to append numbers at the end of every words. This will join all possible numbers with in your given range to all the words.</br
> This wordlist contain both Capitalised and Normal First charater of all First Middle Last Name.</br>

## USAGE
>_PYTHON 3 preferred_
```
python wordlist_generator.py -(arguments)
```
This will create alphabets only wordlist:
```python
python wordlist_generator.py -fname -mname -lname
```
This will create alpha numeric wordlist:
```python
python wordlist_generator.py -fname -mname -lname -n
````
>the paramerts of `-n` will be asked later


### based on user input 

```python
python wordlist_generator.py -fname -mname -lname
```
>available arguments 

`-fname` : first name (required): <br/>
`-mname` : middle name (optional) <br/>
`-lname` : last name (optional) <br/>
`-n`     : append digits(optional

### CAPITALIZE first character in already existing wordlist
`python wordlist_generator.py -f <path to your wordlist>`

### DEVELOPMENT
There is `-r` argument which will delete already generated wordlists by this tool.




