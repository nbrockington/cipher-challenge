# cipher-scripts
Suite of python procedures to analyse and decrypt simple ciphers.


# Tools and usage:

# Caesar and affine shift ciphers

To decrypt a putative Caesar cipher with a given "shift":

`>>> plaintext = decrypt_caesar( ciphertext , shift )`

To decrypt a putative affine shift cipher x -> ax + b mod 26 with given coefficients "a" and "b":

`>>> plaintext = decrypt_affine( ciphertext , a , b )`

# Frequency analysis and trial-and-error monoalphabetic substitution decryption

To perform a frequency analysis on a ciphertext, returning a list of most common letters, bigrams, and trigrams with their percentage frequencies and up to "n" suggestions for possible Caesar cipher shift and/or affine shift coefficients:

`>>> frequencies = decrypt_suggestions( ciphertext , n )`

To find the "k" most frequent "n"-grams in a given text, along with their percentage frequencies:

`>>> ranked_ngrams = k_most_frequent_ngrams( text , n , k )`

For example, to find the 10 most frequent 4-grams in "ciphertext":

`>>> ranked_ngrams = k_most_frequent_ngrams( ciphertext , 4 , 10 )`

To partially decrypt plaintext with a "partial" key where only some letter substitutions are known/guessed:

`>>> plaintext = decrypt_with_partial_key( ciphertext , partial_key )`

(NB. A key is a length-26 list of integers 0-25 representing letters A-Z. Each ciphertext letter is in the index position of the plaintext letter it is substituting. For an empty substitution, use 26.)

To update a key with a new (or no) substitution from plaintext letter "plainchar" to ciphertext letter "cipherchar":

`>>> new_key = add_substitution_to_key( key , plainchar , cipherchar )`

# Transposition ciphers

To decrypt a write-by-row, read-by-row transposition cipher with a given permutation list "perm":

`>>> plaintext = decrypt_transposition_with_perm( ciphertext , perm , "row" )`

To decrypt a write-by-row, read-by-column transposition cipher with a given permutation list "perm":

`>>> plaintext = decrypt_transposition_with_perm( ciphertext , perm , "column")`

For brute-force decryption of a putative transposition cipher:

`>>> all_ranked_perms = brute_force_decrypt_transposition( ciphertext , ["THE", "TH", "ER"] , read-by )`

(NB. This will cycle through all possible permutations of all putative key lengths that are factors of ciphertext length, and rank them by number of ngrams (in this case, "THE", "TH", and "ER") found in the resulting text. It will print the text from the top-ranked permutation of each key length and return a nested list of ranked permutations for all putative key lengths.)

# Known issues

-- The ciphertext inputs must have all newlines removed before being passed as arguments. Ideally they should all be in uppercase letters as some of the transposition and frequency analysis procedures depend on this.

