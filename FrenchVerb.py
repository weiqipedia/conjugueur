pronouns = ['Je','Tu','Il/Elle','Nous','Vous','Ils/Elles']
tenses = ['present','future']
endings = {
    'er':{
        'present':['e','es','e','ons','ez','ent'],
        'future':['erai','eras','era','erons','erez','eront']
    },
    'ir':{
        'present':['is','is','it','issons','issez','issent'],
        'future':['irai','iras','ira','irons','irez','iront']
    },
    're':{
        'present':['s','s','','ons','ez','ent'],
        'future':['rai','ras','ra','rons','rez','ront']
    }
}

class FrenchVerb:
    def __init__ (self, verb_in,tense):
        self.verb_in = verb_in
        verb_stem = verb_in[:-2]
        verb_group = verb_in[-2:]
        if verb_in[0]=='a' or 'e' or 'i' or 'o' or 'u' or 'h':
                pronouns[0]="J'"
        for p in pronouns:
            verb_conjugated = verb_stem + endings[verb_group][tense][pronouns.index(p)]
            print(p + ' ' + verb_conjugated)

verb_in = input('Tapez un verbe francais svp: ')
tense = input('Choisissez entre present et future: ')
conj = FrenchVerb(verb_in,tense)
