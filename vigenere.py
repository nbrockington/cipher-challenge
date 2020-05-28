# Suite of python procedures to help decrypt a Vigenere cipher
#
# >> from vigenere import *
#
# decrypt_vigenere( ciphertext , list_of_shifts ) -> plaintext
# convert_case( text , to_case ) -> converted_text
# interleave_substrings( list_of_substrings ) -> text
# vigenere_suggestions( ciphertext , k ) -> Nothing
# print_ioc_analysis( text ) -> Nothing
# average_ioc_for_k( text , k ) -> average_ioc
# extract_substring_m_mod_k( text , m , k ) -> substring
# calculate_ioc( text ) -> ioc
# remove_spaces( input_text ) -> output_text
#
# Written by Nela Brockington, 9th May 2020, London UK. 
# Edited by Nela Brockington, 10th May 2020, London UK.


# Importing procedures from freq_analysis and crypto_tools modules:

import freq_analysis

import crypto_tools

# Alphabet key:

alphabet_key = ([("A", 0), ("B", 1), ("C", 2), ("D", 3), ("E", 4), ("F", 5), 
                 ("G", 6), ("H", 7), ("I", 8), ("J", 9), ("K", 10), ("L", 11), 
                 ("M", 12), ("N", 13), ("O", 14), ("P", 15), ("Q", 16), 
                 ("R", 17), ("S", 18), ("T", 19), ("U", 20), ("V", 21), 
                 ("W", 22), ("X", 23), ("Y", 24), ("Z", 25)])


# Procedure to decrypt a Vigenere cipher by applying Caesar decryption
# to its substrings, given a (potentially partial) list of shifts to
# use: (NB. Decrypted letters are output in lowercase; use a shift of
# 26 for no decryption; input ciphertext can have spaces but no
# punctuation)

def decrypt_vigenere( ciphertext , list_of_shifts ):

   ciphertext = convert_case( ciphertext , "upper" )

   k = len( list_of_shifts )

   plain_substrings = []

   for m in range( k ):

      cipher_substring = extract_substring_m_mod_k( ciphertext , m , k )

      if list_of_shifts[ m ] == 26:

         plain_substrings.append( cipher_substring )

      else:

         plain_substring = crypto_tools.decrypt_caesar( cipher_substring 
                                                   , list_of_shifts[ m ] )

         plain_substrings.append( convert_case( plain_substring , "lower" ) )

   plaintext_list = []

   count = 0

   for c in ciphertext:

      if c == ' ':

         plaintext_list.append( c )

      else:

         plaintext_list.append( plain_substrings[ count % k][ count // k ] )

         count += 1

   plaintext = ''.join( plaintext_list )

   print( "\n" + ciphertext )

   print( "\n" + plaintext )

   return plaintext



# Procedure to convert all lowercase letters in a text to uppercase or
# vice versa:

def convert_case( text , to_case ):

   converted_text_list = []

   for c in text:

      if ord( c ) in range( 97 , 123 ) and to_case == "upper":

         converted_text_list.append( chr( ord( c ) - 32 ) )

      elif ord( c ) in range( 65 , 91 ) and to_case == "lower":

         converted_text_list.append( chr( ord( c ) + 32 ) )

      else:

         converted_text_list.append( c ) 

   return ''.join( converted_text_list )


# Procedure to interleave a set of substrings (provided in a list):

def interleave_substrings( list_of_substrings ):

   n_strings = len( list_of_substrings )

   len_strings = [ len( s ) for s in list_of_substrings ]

   text_list = []

   for i in range( max( len_strings ) ):

      for j in range( n_strings ):

         if i < len_strings[ j ]:

            text_list.append( list_of_substrings[ j ][ i ] )

   return ''.join( text_list )


# Procedure to return most likely Caeser cipher shift decryption for
# each substring of a Vigenere cipher, given key length k:

def vigenere_suggestions( ciphertext , k ):

   for m in range( k ):

      substring = extract_substring_m_mod_k( ciphertext , m , k )

      top_letter = freq_analysis.k_most_frequent_ngrams( substring , 1 , 1 )

      print( "For substring " + str( m ) + ": if E -> " 
             + str( top_letter ) + ", possible Caesar shift of "
             + str( ( ord( top_letter[ 0 ][ 0 ] ) - 69 ) % 26 ) )

   return
      

# Procedure to print the average ioc for each putative length k of key
# used to encrypt Vigenere cipher: (NB. Currently set 0 < k < 13)

def print_ioc_analysis( text ):

   for k in range( 1 , 13 ):

      print( "Keyword length " + str( k ) + ": IOC = " 
             + str( average_ioc_for_k( text , k ) ) + "\n" )

   return


# Procedure to calculate the average index of coincidence (IOC) across
# subsequences of a text defined by periodicity k (where k is putative
# length of encryption key):

def average_ioc_for_k( text , k ):

   text = remove_spaces( text )

   n = len( text )

   iocs = []

   for m in range( k ):

      sub_string = extract_substring_m_mod_k( text , m , k )

      iocs.append( calculate_ioc( sub_string ) )

   return sum( iocs ) / k


# Procedure to extract a particular substring from a putative Vigenere
# ciphertext, where the substring is defined by key length k and index
# modulo value m: (NB. In Python, string and list indices start from
# 0, so to get the first string use m = 0.)

def extract_substring_m_mod_k( text , m , k ):

   text = remove_spaces( text )

   n = len( text )

   sub_indices = list( filter ( ( lambda x: x % k == m ) , range( n ) ) )

   sub_list = [ text[idx] for idx in sub_indices ]

   return ''.join( sub_list )


# Procedure to calculate the index of coincidence (IOC) for a text,
# which should be all upppercase with no punctuation or newlines:

def calculate_ioc( text ):

   text = remove_spaces( text )

   n = len( text )

   return sum( [ ( ( text.count( chr( i ) ) 
                   * ( text.count( chr( i ) ) - 1 ) )
                   / ( n * ( n - 1 ) ) ) 
                 for i in range( 65 , 91 ) ] )


# Procedure to remove spaces in a text:

def remove_spaces( input_text ):

   text_list = []

   for c in input_text:

      if c != ' ':

         text_list.append( c )

   return ''.join( map ( str , text_list ) )
