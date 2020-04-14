# Suite of python procedures to analyse a ciphertext
#
# >>> from freq_analysis import *
#
# decrypt_suggestions( ciphertext , n )    -> frequencies
# get_first_elems_of_tuples( tup_list )    -> list_of_elements
# rank_tuples_by_second_value( list )      -> ranked_tuples
# k_most_frequent_ngrams( text , n , k )   -> k_ranked_ngrams
# split_into_ngrams( text , n )            -> list_of_ngrams
# is_AtoZ_p( char )                        -> bool
# solve_affine_shift_eq( cipher1 , plain1 , cipher2 , plain2 ) -> coeff
#
# Written by Nela Brockington, 13th April 2020, London UK.



# Procedure to suggest up to n decryption strategies for a ciphertext
# based on letter, bigram and trigram frequency analyses:

def decrypt_suggestions( ciphertext , n ):

   letter_freq = k_most_frequent_ngrams( ciphertext , 1 , 8 )

   bigram_freq = k_most_frequent_ngrams( ciphertext , 2 , 3 )

   trigram_freq = k_most_frequent_ngrams( ciphertext , 3 , 3 )

   frequencies = [ letter_freq , bigram_freq , trigram_freq ]

   # Printing most frequent letters, bigrams and trigrams along with
   # their percentage frequencies:

   for list in frequencies:

      for x in list:

         print( x )


   # LETTERS
   # Suggestions based on frequencies of single letters:

   top_letters = get_first_elems_of_tuples( letter_freq , n )

   for c in top_letters:

      print( "If E -> " + c + ", possible Caesar shift of "
             + str( ( ord( c ) - 69 ) % 26 ) )


   # BIGRAMS
   # Suggestions based on frequencies of bigrams and single letter E:

   top_bigrams = get_first_elems_of_tuples( bigram_freq , n )


   # Checking whether most common bigram is consistent with a Caesar shift:

   if ( ( ( ord( top_bigrams[ 0 ][ 1 ] ) - ord( top_bigrams[ 0 ][ 0 ] ) )
        % 26 ) == 14 ):

      s = ""

   else:

      s = "in"         

   print( "Most common bigram is " + s + "consistent with a Caesar shift" )


   # Using putative T in most common bigrams with putative E from most
   # common letter to set up simultaneous equations mod 26 calculate
   # possible affine shift coefficients for decryption:

   for b in top_bigrams:

      coeff = ( solve_affine_shift_eq( 19 , ord( b[ 0 ] ) - 65, 
                              4 , ord( top_letters[ 0 ] ) - 65 ) )

      if ( coeff[ 0 ] % 2 ) != 0 and ( coeff[ 0 ] % 13 ) != 0:

         print( "If TH -> " + b + ", possible affine shift of a = " 
                + str( coeff[ 0 ] ) + ", b = " + str( coeff[ 1 ] ) )


   # TRIGRAMS
   # Suggestions based on frequencies of trigrams:

   top_trigrams = get_first_elems_of_tuples( trigram_freq , n )


   # Checking whether most common trigram is consistent with a Caesar
   # shift:

   if ( ( ( ( ord( top_trigrams[ 0 ][ 1 ] ) - ord( top_trigrams[ 0 ][ 0 ] ) )
        % 26 ) == 14 )
    and ( ( ( ord( top_trigrams[ 0 ][ 2 ] ) - ord( top_trigrams[ 0 ][ 1 ] ) )
        % 26 ) == 23 ) ):

      s = ""

   else:

      s = "in"         

   print( "Most common trigram is " + s + "consistent with a Caesar shift" )


   # Using putative T, H and E in most common trigram to set up
   # simultaneous equations mod 26 and calculate possible affine shift
   # coefficients for decryption:

   for t in top_trigrams:

      coeff = ( solve_affine_shift_eq( 19 , ord( t[ 0 ] ) - 65, 
                                        4 , ord( t[ 2 ] ) - 65 ) )

      if ( coeff[ 0 ] % 2 ) != 0 and ( coeff[ 0 ] % 13 ) != 0:

         print( "If THE -> " + t + ", possible affine shift of a = "
                + str( coeff[ 0 ] ) + ", b = " + str( coeff[ 1 ] ) )


   # Return list of lists of most common leters, bigrams and trigrams
   # along with percentage frequencies:

   return frequencies;



# Procedure to solve a pair of simultaneous equations of the form
# "a(cipher) + b = plain mod 26" and return coefficients a and
# b. Arguments are numbers 0-25 to represent A-Z.

def solve_affine_shift_eq( cipher1 , plain1 , cipher2 , plain2 ):

   mult_inv = ( [ 0 , 1 , 0 , 9 , 0 , 21 , 0 , 15 , 0 , 3 , 0 , 19 , 0 , 
              0 , 0 , 7 , 0 , 23 , 0 , 11 , 0 , 5 , 0 , 17 , 0 , 25 ] )

   a = ( mult_inv[ ( cipher1 - cipher2 ) % 26 ] 
         * ( ( plain1 - plain2 ) % 26 ) % 26 )

   b =  ( plain1 - cipher1 * a ) % 26

   return [ a , b ];



# Procedure to get the first elements from the first n tuples in a
# list of tuples:

def get_first_elems_of_tuples( tup_list , n ):

   return [ t[0] for t in tup_list[ 0 : n ] ]; 


# Procedure to return the k most frequent ngrams in a text:

def k_most_frequent_ngrams( text , n , k ):

   list_of_ngrams = split_into_ngrams( text , n )

   total_freq = len( list_of_ngrams )

   unique_list = list( set( list_of_ngrams ) )

   ngram_freq_tuples = ( [ ( ngram , 
                       round( list_of_ngrams.count( ngram ) * 100 / total_freq , 1 ) )
                       for ngram in unique_list ] )

   ranked_ngrams = rank_tuples_by_second_value( ngram_freq_tuples )

   return ranked_ngrams[ : k ];


   
# Procedure to parse text into a list of its consecutive ngrams::

def split_into_ngrams( text , n ):

   text = ''.join( filter( is_AtoZ_p , text ) )

   list_of_ngrams = ( [ text[ i : i + n ] 
                        for i in range( len( text ) - ( n - 1 ) ) ] )

   return list_of_ngrams;



# Predicate to check whether a character is a letter A-Z:

def is_AtoZ_p( char ):

   return ( ord( char ) - 65 ) in range( 26 );



# Procedure to rank a list of 2-tuples by the second value of each tuple:

def rank_tuples_by_second_value( list_of_tuples ):

   ranked_tuples = ( sorted( list_of_tuples, key = lambda x: x[ 1 ] ,
                     reverse = True ) )

   return ranked_tuples;



