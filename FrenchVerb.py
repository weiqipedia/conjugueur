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
irregular = {
    'aller':{
        'present': ['vais','vas','va','allons','allez','vont'],
        'future': ['irai','iras','ira','irons','irez','iront']
    },
    'avoir':{
        'present': ['ai','as','a','avons','avez','ont'],
        'future': ['aurai','auras','aura','aurons','aurez','auront']
    }
}

class FrenchVerb:
    def __init__ (self, verb_in,tense):
        self.verb_in = verb_in
        verb_stem = verb_in[:-2]
        verb_group = verb_in[-2:]
        if verb_in[0] in ['a','i','e','o','u','h']:
                pronouns[0]="J'"
        for p in pronouns:
            if verb_in in irregular:
                verb_conjugated = irregular[verb_in][tense][pronouns.index(p)]
            else:
                verb_conjugated = verb_stem + endings[verb_group][tense][pronouns.index(p)]
            print(p + ' ' + verb_conjugated)

verb_in = input('Tapez un verbe francais svp: ')
tense = input('Choisissez entre present et future: ')
conj = FrenchVerb(verb_in,tense)
