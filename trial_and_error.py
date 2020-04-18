# Suite of python procedures to help implement trial-and-error
# decryption of ciphertext
#
# >>> from trial_and_error import *
#
# decrypt_with_partial_key( ciphertext , partial_key ) -> plaintext
# add_substitution_to_key( key , plainchar , cipherchar ) -> new_key
#
# A substitution key is a list of length 26, where the index
# represents the plaintext letter (0-25) and the value at each index
# represents the ciphertext letter (0-25). A partial key does not
# contain a substitution for each plaintext letter; it carries the
# value 26 at indices that represent plaintext letters that have not
# yet been deciphered.
#
# Written by Nela Brockington, 18th April 2020, London UK.


# The empty key which will not decipher anything as no character
# subsitutions are specified:

empty_key = ( [ 26 , 26 , 26 , 26 , 26 , 26 , 26 , 26 , 
                26 , 26 , 26 , 26 , 26 , 26 , 26 , 26 , 
                26 , 26 , 26 , 26 , 26 , 26 , 26 , 26 , 26 , 26 ] )



# Procedure to decrypt a ciphertext given a (potentially partial) key
# that specifies letter subsitutions to be made. NB. In the output,
# subsitutions to plaintext are represented with lowercase letters,
# while original ciphertext letters are represented with uppercase
# letters:

def decrypt_with_partial_key( ciphertext , partial_key ):

   plaintext_list = []

   for c in ciphertext:

      if ( ord( c ) in range( 65 , 91 ) 
           and ( ord( c ) - 65 ) in partial_key ):

         decrypted_c = chr( partial_key.index( ord( c ) - 65 ) + 97 )

         plaintext_list.append( decrypted_c )

      else:

         plaintext_list.append( c )


   plaintext = ''.join( map( str , plaintext_list ) )

   print( ciphertext + "\n")

   print( plaintext )

   return plaintext;


# Procedure to add a subsitution to a key, where plainchar is the
# (capital) letter in plain text and cipherchar is the (capital)
# substituted letter in the ciphertext. NB. To remove a subsitution
# for a given plainchar, let cipherchar = '' (empty string):

def add_subsitution_to_key( key , plainchar , cipherchar ):

   del key[ ord( plainchar ) - 65 ]

   if cipherchar:

      key.insert( ord( plainchar ) - 65 , ord( cipherchar ) - 65 )

   else: 

      key.insert( ord( plainchar ) - 65, 26 )

   return key

