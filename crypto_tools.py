# Suite of python procedures to help crack cipher challenges
#
# >>> from crypto_tools import *
#
# num_key_to_char( num_key ) -> char_key
# make_caesar_key( shift )   -> caesar_key
# make_affine_key( a , b )   -> affine_key
# invertible_key_p( key )    -> bool
# decrypt_with_key( ciphertext , key ) -> plaintext
# decrypt_caesar( ciphertext , shift ) -> plaintext
# decrypt_affine( ciphertext , a , b ) -> plaintext
# load_ciphertext_from_file( path_and_filename ) -> ciphertext
#
# Convention: keys are lists that represent letters numerically (0 to
# 25). The index of each key represents the plaintext letter (0 to 25)
# and the element at that index represents the corresponding
# ciphertext letter.
# 


# Procedure to load ciphertext from a *.txt file (NB. new lines and
# punctuation must be removed)

def load_ciphertext_fom_file( path_and_filename ):

   f = open( path_and_filename , "r" )

   ciphertext = f.read()

   return ciphertext;



# Procedure to decrypt a ciphertext with a given affine shift cipher
# specified by a, b such that x -> ax + b (mod 26):

def decrypt_affine( ciphertext , a , b ):

   key = make_affine_key( a , b )

   plaintext = decrypt_with_key( ciphertext , key )

   return plaintext;


# Procedure to decrypt a ciphertext with a given Caesar cipher
# "shift":

def decrypt_caesar( ciphertext , shift ):

   key = make_caesar_key( shift )

   plaintext = decrypt_with_key( ciphertext , key )

   return plaintext;


# Procedure to decrypt a ciphertext given a key that specifies
# letter substitutions to be made:

def decrypt_with_key( ciphertext , key ):

   plaintext_list = []

   for c in ciphertext:

      if ord( c ) in range( 65 , 91 ):

         decrypted_c = chr( key.index( ord( c ) - 65 ) + 65 )

         plaintext_list.append( decrypted_c )

      else:

         plaintext_list.append( c )

   plaintext = ''.join( map ( str , plaintext_list ) )

   print( plaintext )

   return plaintext;


# Procedure to convert a numeric key into a character key, that is, a
# list of characters where the index of the character represents the
# plaintext character that is encoded.

def num_key_to_char( num_key ):

   char_key = []

   for n in num_key:

      char_key.append( chr( n + 65 ) )

   print( char_key )

   return char_key;


# Procedure to generate a Caesar cipher table x -> x + shift, based on
# argument shift

def make_caesar_key( shift ):

   caesar_key = [ ( ( x + shift ) % 26 ) for x in range( 26 ) ]

   print( caesar_key )

   return caesar_key;


# Procedure to generate an affine shift table x -> ax + b mod 26, based
# on arguments a and b

def make_affine_key( a , b ):

   affine_key = [ ( (a * x + b ) % 26 ) for x in range( 26 ) ]

   if invertible_key_p( affine_key ):

      print( affine_key )

      return affine_key;

   else:

      print( "ERROR: Cipher from this affine shift is not decodable." )

      return;


# Procedure to check whether a given key is "invertible", that is,
# the mapping from the alphabet to the key is injective:

def invertible_key_p( key ):

   return set( key ) == set( [ x for x in range( 26 ) ] );



