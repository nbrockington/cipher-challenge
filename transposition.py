# Suite of python procedures to decrypt transposition ciphers
#
# >>> from transposition import *
#
# decrypt_transposition_with_perm( ciphertext 
#                                , perm 
#                                , read_by ) -> plaintext
#
# E.g. for a write-by-row, read-by-column transposition cipher, use
# read_by = "column"; for a write-by-row, read-by-row cipher, use
# read_by = "row".
#
# text_to_ncolumn_matrix_by_row( text , n ) -> matrix
# text_to_ncolumn_matrix_by_column( text , n ) -> matrix
# depermute_matrix_columns( matrix , perm ) -> depermuted_matrix
# read_matrix_by_rows( matrix ) -> text
# remove_spaces( input_text ) -> text
# reverse_text( text ) -> reversed_text
# create_matrix_of_zeros( m , n ) -> matrix
#
# Written by Nela Brockington, 8th May 2020, London UK.


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

