#!/usr/bin/env python

from ConceptNet import conceptNet

cn = conceptNet()

language = "en"
rel = "RelatedTo" #more info at: https://github.com/commonsense/conceptnet5/wiki/Relations
origin = "chaos"
destiny = "order"

if __name__ == "__main__":
	cn.termsAssociation(origin, destiny, 20, "en", True)
	#cn.lookup(language, origin, True)
	#cn.relation(rel, origin, True)