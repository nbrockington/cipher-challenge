# Suite of python procedures to implement brute force decryption of
# transposition ciphers
#
# >>> from brute_force import *
#
# brute_force_decrypt_transposition( ciphertext 
#                                  , ngrams_to_count
#                                  , read_by ) -> all_ranked_perms
#
# rank_transposition_decryptions( ciphertext
#                               , ngrams_to_count
#                               , n
#                               , read_by ) -> ranked_perms
#
# NB. Argument read_by = "rows" | "columns"
#
# count_common_ngrams_in_text( text , ngrams_to_count ) -> count
# count_ngram_occurance( text , ngram ) -> count
#
# Additional helper scripts from transposition.py, freq_analysis.py
# are copied in ebelow.
#
# NB. Ciphertext can have spaces but must not have punctuation or
# newlines and all letters must be uppercase.
#
#
# Written by Nela Brockington, 9th May 2020, London UK. 


# Loading itertools module for permutations functionality:

import itertools


# Procedure to attack a transposition cipher by brute force, trying
# all permutations for all values of n between 2 and 10 that are
# factors of the ciphertext length, returning a list of top-ranked
# permutations for each such n: (NB. Recommended ngrams to count are
# ["TH", "ER", "THE"]

def brute_force_decrypt_transposition( ciphertext , ngrams_to_count , read_by ):

   n_char = len( remove_spaces( ciphertext ) )

   poss_key_lengths = ( list ( filter( ( lambda x: n_char % x == 0 ) 
                                       , range( 2 , 9 ) ) ) )

   all_ranked_perms = []

   for n in poss_key_lengths: 

      ranked_perms = rank_transposition_decryptions( ciphertext 
                                                   , ngrams_to_count
                                                   , n
                                                   , read_by )

      print( "Top permutation for key length " + str( n ) + " is "
            + str( ranked_perms[ 0 ][ 0 ] ) + " with ngram count of "
            + str( ranked_perms[ 0 ][ 1 ] ) + ".\n\n" )

      all_ranked_perms.append( ranked_perms ) 

   return all_ranked_perms



# Procedure to rank the results of transposition decryptions under
# each permutations of the set {1,...,n} (except for the identity) by
# the count of specified ngrams in each, returning a ranked list of
# permutations and their ngram counts, and printing the text obtained
# from the top-ranked decryption:

def rank_transposition_decryptions( ciphertext 
                                  , ngrams_to_count 
                                  , n 
                                  , read_by ):

   perms_list = list( itertools.permutations( list( range( 1 , n + 1 ) ) ) )

   perms_and_counts =  ( [ [ list( p ) 
                           , count_common_ngrams_in_text( 
                                 decrypt_transposition_with_perm( ciphertext
                                                                , list( p ) 
                                                                , read_by )
                               , ngrams_to_count ) ] 
                         for p in perms_list ] )   

   ranked_perms =  rank_tuples_by_second_value( perms_and_counts )

   print( decrypt_transposition_with_perm( ciphertext 
                                         , ranked_perms[ 0 ][ 0 ]
                                         , read_by ) )

   return ranked_perms
 


# Procedure to count the number of occurances of specified ngram(s) in
# a text, where ngrams are specified as elements of a list in the
# second argument:

def count_common_ngrams_in_text( text , ngrams_to_count ):

   counts = [ count_ngram_occurance( text , ngram ) for ngram in ngrams_to_count]

   return sum( counts )


# Procedure to count the number of occurances of a specific ngram in a
# text:

def count_ngram_occurance( text , ngram ):

   list_of_ngrams = split_into_ngrams( text , len( ngram ) )

   return list_of_ngrams.count( ngram )



# Procedure to parse text into a list of its consecutive ngrams:

def split_into_ngrams( text , n ):

   text = ''.join( filter( is_AtoZ_p , text ) )

   list_of_ngrams = ( [ text[ i : i + n ]
                        for i in range( len( text ) - ( n - 1 ) ) ] )

   return list_of_ngrams;


# Predicate to check whether a character is a letter A-Z:

def is_AtoZ_p( char ):

   return ( ord( char ) - 65 ) in range( 26 );
      


# Procedure to rank a list of 2-tuples by the second value of each
# tuple:

def rank_tuples_by_second_value( list_of_tuples ):

   ranked_tuples = ( sorted( list_of_tuples, key = lambda x: x[ 1 ] ,
                     reverse = True ) )

   return ranked_tuples;      



# Suite of python procedures to decrypt transposition ciphers
#
# >>> from transposition import *
#
# decrypt_transposition_with_perm( ciphertext 
#                                , perm 
#                                , read_by ) -> plaintext


# Procedure to decrypt a transposition cipher with a given encryption
# permutation and a given "read_by" parameter, which can be "row" or
# "column": (NB. Any spaces will be removed from the ciphertext in the
# first step)

def decrypt_transposition_with_perm( ciphertext , perm , read_by ):

   ciphertext = remove_spaces( ciphertext )

   if read_by == "row":

      cipher_matrix = text_to_ncolumn_matrix_by_row( ciphertext , len( perm ) )

   else:

      cipher_matrix = text_to_ncolumn_matrix_by_column( ciphertext , len( perm ) )

   depermuted_matrix = depermute_matrix_columns( cipher_matrix , perm ) 

   plaintext = read_matrix_by_rows( depermuted_matrix )

   return plaintext


# Procedure to read characters from a matrix by rows and convert to a
# string:

def read_matrix_by_rows( matrix ):

   text_list = [ char for row in matrix for char in row ]

   return ''.join( map ( str , text_list ) )


# Procedure to depermute a matrix by columns, given the permutation
# that was used to permute it:
  
def depermute_matrix_columns( matrix , perm ):

   inv_perm = [ perm.index( i + 1 ) for i in range( len( perm ) ) ]

   return [ [ row[ i ] for i in inv_perm ] for row in matrix ]


# Procedure to construct an n-column matrix row-by-row from a string,
# treating each row as a list and nesting the rows into a nested list:

def text_to_ncolumn_matrix_by_row( text , n ):

   text = list( text )

   m = len( text ) // n

   return [ text[ i * n : ( i + 1 ) * n ] for i in range( m ) ]


# Procedure to construct an n-column matrix column-by-column from a
# string, by first filling an n-row matrix row-by-row and then
# transposing it:

def text_to_ncolumn_matrix_by_column( text , n ):

   m = len( text ) // n

   matrix = text_to_ncolumn_matrix_by_row( text , m )

   return [ [ row[ i ] for row in matrix ] for i in range( m ) ]


# Procedure to remove spaces in a text: 

def remove_spaces( input_text ):

   text_list = []

   for c in input_text:

      if ord( c ) != 32:

         text_list.append( c )

   return ''.join( map ( str , text_list ) )


# Procedure to reverse the order of letters in a text:

def reverse_text( text ):

   reversed_list = []

   for c in text:

      reversed_list.insert( 0 , c )

   reversed_text = ''.join( map ( str , reversed_list ) )

   return reversed_text



# Procedure to create an m-by-n matrix of zeros:

def create_matrix_of_zeros( m , n ):

   mat = []

   row = [ 0 ] * n

   for i in range( m ):

      mat.append( row )

   return mat
