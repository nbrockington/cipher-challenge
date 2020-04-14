# cipher-scripts
Suite of python procedures to analyse and decrypt simple ciphers.


# Usage

To decrypt a putative Caesar cipher with a given "shift":

`>>> plaintext = decrypt_caesar( ciphertext , shift )`

To decrypt a putative affine shift cipher x -> ax + b mod 26 with given coefficients "a" and "b":

`>>> plaintext = decrypt_affine( ciphertext , a , b )`

To perform a frequency analysis on a ciphertext, returning a list of most common letters, bigrams, and trigrams with their percentage frequencies and up to "n" suggestions for possible Caesar cipher shift and/or affine shift coefficients:

`>>> frequencies = decrypt_suggestions( ciphertext , n )`

To find the "k" most frequent "n"-grams in a given text, along with their percentage frequencies:

`>>> ranked_ngrams = k_most_frequent_ngrams( text , n , k )`

For example, to find the 10 most frequent 4-grams in "ciphertext":

`>>> ranked_ngrams = k_most_frequent_ngrams(ciphertext, 4, 10)`

