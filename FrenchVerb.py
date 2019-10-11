class FrenchVerb:
    def __init__ (self, verb_in):
        self.verb_in = verb_in

        if verb_in[-2:] == 'er':
            if verb_in == 'aller':
                fpc = 'vais'
                spc = 'vas'
                tpc = 'va'
                fppc = 'allons'
                sppc = 'allez'
                tppc = 'vont'

            else:
                verb_stem = verb_in[:-2]
                fpc = verb_stem + 'e'
                spc = verb_stem + 'es'
                tpc = verb_stem + 'e'
                fppc = verb_stem + 'ons'
                sppc = verb_stem + 'ez'
                tppc = verb_stem + 'ent'

        elif verb_in[-2:] == 'ir':
            verb_stem = verb_in[:-2]
            fpc = verb_stem + 'is'
            spc = verb_stem + 'is'
            tpc = verb_stem + 'it'
            fppc = verb_stem + 'issons'
            sppc = verb_stem + 'issez'
            tppc = verb_stem + 'issent'

        else:
            verb_stem = verb_in[:-2]
            fpc = verb_stem + 's'
            spc = verb_stem + 's'
            tpc = verb_stem  
            fppc = verb_stem + 'ons'
            sppc = verb_stem + 'ez'
            tppc = verb_stem + 'ent'

        if verb_in[0] == 'a' or 'e' or 'i' or 'o' or 'u':
            print ("J'" + fpc)
        else:
            print("Je " + fpc)

        print("Tu " + spc)
        print("Il/Elle " + tpc)
        print("Nous " + fppc)
        print("Vous " + sppc)
        print("Ils " + tppc)

verb_in = input('Tapez un verbe francais svp: ')
conj = FrenchVerb(verb_in)