a = ("""0.0, 0.0, 0.0, 0.01840490797546012, 0.03987730061349693, 0.07975460122699386, 0.12269938650306748, 0.1687116564417178, 0.22392638036809814, 0.26993865030674846, 0.3343558282208589, 0.3987730061349693, 0.4662576687116564, 0.5950920245398772, 0.6717791411042944, 0.763803680981595, 0.7975460122699386, 0.8343558282208589, 0.8466257668711656, 0.8282208588957055, 0.7822085889570551, 0.6993865030674846, 0.6349693251533742, 0.5429447852760736, 0.48773006134969327, 0.4662576687116564, 0.352760736196319, 0.2791411042944785, 0.20552147239263804, 0.14723926380368096, 0.09815950920245399, 0.05521472392638037, 0.024539877300613498, 0.006134969325153374, 0.0, 0.0, 0.0, 0.0""")
a = a.replace(",","%")
a = a.replace(".",",")
a = a.replace("%","\n")
print(a.split())

print(a)