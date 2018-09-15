#Intro
The detector.py file takes in a couple of arguments to determine if the rate of plagiarism between the control and comparison file.

#Usage Instructions
To run the detector, you'll need:
- synonym file
- control file
- comparing file

Optionally, you can choose your own tuple size. It's defaulted to 3.

The command is:
```bash
python detector.py -s syns.txt -c file1.txt -o file2.txt -t 3
```

For additional help you can run: `python detector.py -h`

#File Structure
I have broken out the majority of the work into their respective Classes. The detector.py file is only used to coordinate between the classes, output results and handle passed in arguments.

**synonym.py**
The Synonym class handles creating a dictionary with a hash value that's used to replace content from the comparison and control files

**file.py**
The File class will get content from the supplied files and sanitize it. Once sanitized, it'll replace the synonyms and provide the method to create tuples to be used to identify the plagiarism rate.

#Algorithm
The synonym file gets converted into a set. Every synonym in a row of the file is sorted and joined to create a hash. For example `[run, sprint, jog]` will become `jogrunsprint`. Each one of those words will get a key in the set with a value of the hashed synonyms.

The contents of the control file and the comparison file are sanatized by lowercasing, removing excess white space and removing punctuation. Once cleaned up, but before tupling, each word that has a key in the synonym dictionary will be replaced by the hash.

Once all synonyms are hashed, the contents of the files are broken out into tuples and then joined into a string. Because the contents have been sanitized, at least rudimentarily for this exercise, it allows us to compare the tuples as string values rather than as arrays of tuple size length. Because the tuple is now a primitive type, we can find the intersection of the two lists.

The intersection count is then divided by the number of tuples in the comparing file to yield the rate of plagiarism.

###Run Time
This algorithm tries to avoid exponential run times. There's a lot of preprocessing that is done before the tupling and comparisons are done.

#Possible Improvements
**Synonyms**
The dictionary could be compiled once for a multitude of comparisons. Synonyms don't change frequently. Having a faster data structure having a precompiled dictionary ready would definitely improve creation time and read times when comparing.

**Set Hashing**
While the synonym width is currently 3, replacing a word with a combination of 3 isn't so bad. When the hashing gets long, then we're replacing one word with a lot more and may be memory intensive. We could create a smarter hash that could be set to a constant length to reduce this problem. We'll just have to avoid collissions. Precompiling a master synonym dictionary would allow us to find collissions and treat them accordingly.

**ARGV Parsing**
The way things are being passed in is very redimentary. The usage of the ArgumentParser package would improve usability and define variables much more clearly.

**Tests**
Due to time constraints and the available languages for this exercise, I wasn't able to build out a testing framework. All the methods have been kept simple in order to supply tests given more time to research the unittest library for python.

#Other Usages
The files that are being passed in are sanitized and standardizes white space. By standardizing whitespace, it opens up the possibility to start comparing text regardless of source. If we wanted to compare websites html content, we could dump the inner html into a large txt document and compare tuples across multiple elements as sections. It would be similar to merging paragraphs into one large string.
