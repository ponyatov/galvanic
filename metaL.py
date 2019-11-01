## @package metaL
## 


import os,sys

## @defgroup frame
## @brief Marvin Minsky's **extended frame model**
## @{

## @brief base Frame class extended with ordered container = stack
## @ingroup frame
class Frame:

    ## @param V[in] scalar value / object name
    def __init__(self,V):
        ## type/class tag (required for @ref PLY parser)
        self.type = self.__class__.__name__.lower()
        ## object name or scalar value in implementation language type (string, number)
        self.val  = V
        ## slots = attributes = named edges of the @ref eog
        self.slot = {}
        self.nest = []
