#----------------------------#
#       Mitzjougraou:        #
#          the game          #
#                            #
#                by Gameroune#
#                            #
#ver:1.0 (sans succès)       #
#----------------------------#

from time import sleep 
        
print("Bienvenue dans")
sleep(1.5)
print("Mitjzougraou: le jeu\n")
sleep(2)

rep="0"
fin=False
a=1

vodk=0

while(fin!=True):
    
    if(a==1):
        rep=-1
        print("""  
    Bienvenue, grand aventurier, tu te trouve dans le royaume de nzomigini: 
Nzomiland!
    tu peux aller en bien des endroits différents, qui vont de la pologne au kentucky, 
en passent par la mères patrie
""")
        sleep(3)
        print("""
Que voulez-vous faire?
>1:Aller à Nzocity
>2:Aller à Gasparville
>3:Aller en Pologne
>4:Aller dans le Kentucky
""")
        rep=input(">")
        
        if(int(rep)==1): a=2
        if(int(rep)==2): a=10
        if(int(rep)==3): a=13
        if(int(rep)==4): a=25
    
    if(a==2):
        rep=-1
        print(""" 
    Tu te trouve dans la ville d'Nzocity, c'est un endroit plein
de merveilles, telles que la grande academie du théorem de thales
et de la translation. On peut aussis prendre le train pour la Mère
Patrie, et visité la maison du grand Nzomignin.
        """)
        sleep(3)
        print("""
Que voulez-vous tu faire?
>1:Prendre le train pour la Mère Patrie
>2:Visiter la maison de nzomigni
>3:Retournez a Nzomiland
""")
        rep=input(">")
        
        if(int(rep)==1): a=3
        if(int(rep)==2): a=8
        if(int(rep)==3): a=1
        if(int(rep)==4): a=9
        
    if(a==3):
        rep=-1
        print("""
    Tu es arrivé a ta destination, La Mère Patrie! La patrie des
plus grands. Tu peux y faire tout pleins de trucs, boire de la vodka,
où aller au grand marchée. Mais fais attentions, car la mafia russe
rode.
        """)
        sleep(3)
        print(""" 
Que veux tu faire?
>1:Boire de la vodka
>2:Aller au grand marché
>3:Rentré a Nzocity
        """)
        rep=input(">")
        
        if(int(rep)==1): a=4
        if(int(rep)==2): a=5
        if(int(rep)==3): a=2
        if(int(rep)==4): a=6
        if(int(rep)==5): a=7

    if(a==4):
        rep=-1
        (""" 
vous buvez de la vodka, beaucoup de vodka.
         """)
        sleep(2)
        a=3
        
    if(a==5):
        rep=-1
        print("""
    vous voila au Grand Marché de la Mère Patrie, on y trouve tout
pleins de choses, telle que du Pangolin, des Haricots ou la
dépouille de Fukuoka Rhuim
""")
        sleep(3)
        print("""
qu'achetez vous?
>1:du pangolin
>2:des haricots
>3:la dépouilles de Fukuoka Rhuim
        """)
        
        rep=input(">")
        
        if(int(rep)==1):
            print("Vous avez acheté du pangolin")
            sleep(1.5)
            a=3
        if(int(rep)==2):
            print("vous avez acheté des haricots")
            sleep(1.5)
            a=3
        if(int(rep)==3): 
            print("vous avez acheté la dépouilles de Fukuoka Rhuim")
            sleep(1.5)
            a=3

    if(a==6):
        rep=-1
        print("""
    Vous vous retrouvez face a la mafia russe, vous avez très peur.
Elle vous encercle et vous menace, mais dans un elan de courage,
vous dite:" Bon, bah moi jee vais def la mafia russe", et vous faite
un triple mawashigeri circulaire-carée, suivi d'un zizicoptère enflamé
pour terminée sur un spinjusu qui vous donne le tournis. 
    Vous venez de detruire la mafia russe, en un rien de temps. Toutes
le mère patrie vous admire.
        """)
        sleep(8)
        a=3
        
    if(a==7):
        rep=-1
        print(""" 
    Vous  avez décider de mettre gaspard en prison, car...Vous l'avez décider.
vous prenez donc gaspard, et le jetez dans la prison comme un vulgaire sac
de pomme de terre de la glorieuse mère patrie.
        """)
        sleep(5)
        a=3
        
    if(a==8):
        rep=-1
        print("Vous visitez la bellle et grande maison de nzomigni.")
        sleep(2)
        a=2
    
    if(a==9):
        rep=-1
        print("""
    Vous entrez dans la grande académies du théorem de thales
et de la translation. Le grand Nzomigni y fait cours et vous apprend
la translation:
"oui, don, don, la translationn, c qd on passe  point 'a' au point 'b' 
en passant par le poin... je crois que je le suis trompé ouiii.. ha non
c Joachim qui c'est trompé, ouii" 
        """)
        sleep(7)
        a=2
    if(a==10):
        rep=-1
        print("""
    Vous voici a Gasparville, une ville a la reputation pas fameuse et 
connu pour ses nombreux lieux de débauches, sa population exclusivement
masculine et beauf et a son concours annuelle de blague de beauf, dont 
le dernier et seul gagnant est le fameux gaspard.
        """)
        sleep(5)
        print("""
Que voulez-vous faire?
>1:Ecoutez une blague de Gaspard
>2:Acheter un god de combat
>3:Retournez a Nzomiland
        """)
        rep=input(">")
        
        if(int(rep)==1): a=11
        if(int(rep)==2): a=12
        if(int(rep)==3): a=1
        
    if(a==11):
        rep=-1
        print("""
    Gaspard, le grand beauf, vous raconte l'une de ses nombreuses blagues:
"Alors tu vois mon lit? Bah c'est là où je dors, mais aussi là où je baise!
AHAHAHAHAHAH!!!"
    Vos oreilles se metent a saigner, e vous perdez 10 pv. Vous vous enfuyez
de cette endroit pire que l'enfer, et retournez a Nzomiland.
             """)
        sleep(6)
        a=1
        
    if(a==12):
        rep=-1
        print("""
    Vous allez au sexshop le plus proche, entrez, et demmandez un god de combat.
Le vendeur vous indique le prix, soit 69 sesk (la monaie de gasparville). Vous
debourssez cette modique somme, et vous emparez, tout joyeux, de votre nouvelle
arme.
             """)
        sleep(6)
        a=10        
        
    if(a==13):
        rep=-1
        print("""
    vous vous rendez en Pologne, le pays de la polish cow, du zapomiel, un merveilleux
pay quoi. Il a un magnifique drapeau rouge, blanc, rouge a l'horizontale, et puis que
dire d'autre de ce merveill...euuh, jme repetrais pas un peu là? bref vous êtes en Pologne 
quoi.
                """)
        sleep(6)
        print("""
        Que voulez-vous faire?
        >1:recoltez du zapomiel
        >2:Aller sur 5 flemmards
        >3:Retournez a Nzomiland
        """)
        
        rep=input(">")
        
        if(int(rep)==1): a=14
        if(int(rep)==2): a=15
        if(int(rep)==3): a=1
    
   
    if(a==14):
        rep=-1
        print("""
    Vous recoltez du zapomiel, cette boisson magique qui restaure votre vie, et qui 
est produit par la glorieuse polish cow, mondialement connu en pologne... euh dans
Nzomiland je voulais dire, vs savez avec ce squema là, c très très fatiguant, bon je 
m'égare-là... Bref, vous recoltez du zapomiel, et récuperez 10 vie (surement celles
enlevez par les blagues ou la mauvaise fois de gaspard)

                """)
        sleep(6)
        a=13
    
    if(a==15):
        rep=-1
        print("""
    Vous vous trouvez sur 5 flemmard, cette petite ile très connu pour ses loisir,
son petit village, son aquarium, son metro, son port... c'est un peu le paradis
terrestre. Je vous laisse le loisir de de tout découvrire, hé ho, pas de spoil ici!
                    """)
        sleep(6)
            
        print("""
Que voulez-vous faire?
>1:Faire un tour en metro
>2:Visiter la muraille
>3:Achetez le journal
>4:Allez a jojo&co
>5:Retournez en pologne
            """)
            
        rep=input(">")
            
        if(int(rep)==1): a=16
        if(int(rep)==2): a=17
        if(int(rep)==3): a=18
        if(int(rep)==4): a=19
        if(int(rep)==5): a=13
        if(int(rep)==6): a=23
        if(int(rep)==7): a=24
            
    if(a==16):
        rep=-1
        print("""
    Vous prenez le tout nouveau metro de 5 flemmard, tellement nouveau, qu'il
est meme pas terminé, incroyable non? Vous vous propulsez donc a la force de
vos jambe et des quelques rails autopropulseur (ta vu la technologie), et finissez
votre tour, tellement fatigué que vous perdez 10 vies.
                    """)
        sleep(4)
        a=15
        
    if(a==17):
        rep=-1
        print("""
    Vous visitez la grande muraille de chi... euh de  jojo&co, construite en pas très
longtemps, mais un peu quand même. Cette belle murailles qui fait le tour du centre ville,
et border de champs de blé (faut bien nourrir le peuple hein).
                    """)
        sleep(4)
        a=15
        
    if(a==18):
        rep=-1
        print("""
    Vous achetez le journal je jojo&co, pour la modique somme de 5 sous...
COMBIEN? Mais c'est du vol a ce prix là!!! Je vais faire la grève pendant 15
seconde moi!
                    """)
        sleep(15)
        a=15
        
    if(a==19):
        rep=-1
        print("""
    Vous vous rendez dans jojo&co ce petit pay indépendant, ou se trament de
nombreuses choses... Et ou beaucoup de nom doux et de nom gentils sont echangé
(comprenez des insultes) dans la joie et la bonne humeure
                    """)
        sleep(6)
            
        print("""
Que voulez-vous faire?
>1:Faire un rite satanique avec mikasa
>2:debatre avec gaspard
>3:Retournez sur 5 flemmards
            """)
            
        rep=input(">")
            
        if(int(rep)==1): a=20
        if(int(rep)==2): a=21
        if(int(rep)==3): a=15
        if(int(rep)==4): a=22
            
    if(a==20):
        rep=-1
        print("""
    Vous faite un rite satanique avec mikasa, et invoquer le diable grace a votre rituel
de soumission pedosatanique, et à la vision de l'aigle et du vers de terre. Etrangement
le diable ressemble fortement a gaspard, fait des blagues de beauf et est borné (coincidence,
je ne crois pas).
                    """)
        sleep(8)
        a=19
    
    if(a==21):
        rep=-1
        print("""
    Vous decidez de débattre avec gaspard, et de le convaincre que le Vatican n'est
pas un pay. Mal vous en prends, cette mule, ne change pas d'avis et vous fait perdre
10 vie a cause de votre grande fatigue après avoir passé des heures, des jours, des 
mois même!
                    """)
        sleep(6)
        a=19
        
    if(a==22):
        rep=-1
        print("""
    Vous bannez ambroise, chose que vous vouliez faire depuis des années, halala, que
c'est beau d'accomplir ses rêves... Bref, vous bannez Ambroise, ce spammeurs de mentions 
inutile. Vous recuperez 10 vie du faites de la satifaction que vous ressentez a ce moment.                
        """)
        sleep(6)
        a=19
        
    if(a==23):
        rep=-1
        print("""
    Vous explosez la maison de Lucas avec un peu (beaucoup) de tnt trouver par terre.
                    """)
        sleep(15)
        
    if(a==24):
        rep=-1
        print("""
    Vous visitez la "Muraille de kéké" un morceau perdu de murraille, construit tout en
diamant. Vous comprennez maintenant pourquoi les gens mourrait de faim, et était vetu de
haillons, et pourquoi le si connus et fameux port était a l'arret. Mais dans votre
extrèmes bienveillance et gentillese inexistante, vous vous emparrez de tout ce diamant
et faite fortune sans plus repensez a c'est puavre gens.
                    """)
        sleep(8)
        a=15
        
    if(a==25):
        rep=-1
        print("""
    Vous vous rendez au kentucky, cette petite régions de Nzomiland, pleine de truand et
de cow-boy du farwest, mais vous pouvez aussis y manger du Kentucky Fried Chickens.
                    """)
        sleep(5)
        print("""
Que voulez-vous faire?
>1:Manger du KFC
>2:Retourné a Nzomiland
""")
        rep=input(">")
        
        if(int(rep)==1): a=26
        if(int(rep)==2): a=1
        if(int(rep)==3): a=27
        
    if(a==26):
        rep=-1
        print("""
    Vous vous mangez du KFC.
        sleep(3)
        """)
        a=25
        
    if(a==27):
        rep=-1
        print("""
    Vous voulez vanger el mojadas, c'était un si grand et fier cheval, en plus c'etait un pur
sang arabe, très TRES beau. Vous combatez donc les chasseurs de primes qui l'on tué a coup de
gode de combats ( si vous en evz un), sinon vous placez quelque mawashi-geri (on vous avait pas
dit que vous le maitrisiez?), puis vous fouillez les lieux. Quand vous vient a l'idée de resucitez
el-mojadas.
                    """)
        sleep(7)
        print("""
Que voulez-vous faire?
>1:Resucité el mojadas
>2:Continuer votre route
""")
        rep=input(">")
        
        if(int(rep)==1): a=28
        if(int(rep)==2): a=29
        
    if(a==28):
        rep=-1
        print("""
    Vous resucitez el-mojadas, grace a votre grand savoir faire de grand pratre du mitzjougraou
(on vous avait pas dit ca aussis, satané squema). Vous obtenez donc le grand el-mojadas. Quand
soudain la poulice arrive.
                    """)
        sleep(6)
        print("""
Que voulez-vous faire?
>1:Se cacher
>2:Affronter la poulice
""")
        rep=input(">")
        
        if(int(rep)==1):a=30
        if(int(rep)==2):a=31
        
    if(a==29):
        rep=-1
        print("""
    Vous entendez soudain la poulice arrivez, suite a votre combat avec les
chasseurs de primes.
            """)
        sleep(5)
        print("""
Que voulez-vous faire?
>1:Se caher
>2:Affronter la poulice
""")
        rep=input(">")
        
        if(int(rep)==1):a=30
        if(int(rep)==2):a=31
        
    if(a==30):
        rep=-1
        print("""
    Vous vous cachez dans le batiment, derriere un caisse de poudre a canon.
Heureusement la poulice est un peu flemmarde, et ne va pas trop fouiller le
batiment. Vous décidez de quiter cette regions de fous et retournez en Nzomiland
                    """)
        sleep(5)
        a=1
        
    if(a==31):
        rep=-1
        print("""
    Vous affrontez la poulice a coup de mawashi-geri (encore), et au bout d'un long
personne n'a pris le dessus, vous etes extremement fatigué, et deux choix s'offre a
vous: se rendre, ou continuer le combat.
                    """)
        sleep(5)
        print("""
Que voulez-vous faire?
>1:Se rendre
>2:Continuer le combat
""")
        rep=input(">")
        
        if(int(rep)==1): a=32
        if(int(rep)==2): a=33
    
    if(a==32):
        rep=-1
        print("""
    Vous vous rende donc et vous faite emprisonez par les poulicier. Ils vous envoie
a la prison de Nzocity, et cotoyer gaspard (seulement ssi  vous l'avez emprisonner,
et Ambroise (seulement si vous l'avez ban). Vous arrivez tant bien que mal a vous echapez
de cette prison pleine de trous et de failles de securité, et vous retrouvez a Nzocity.
                    """)
        sleep(5)
        a=2
        
    if(a==33):
        rep=-1
        print("""
    Vous 
    continuez ce combat et arrivez a battre les 69 pouliciers envoyer a vos trousse (comme
quoi, c'est puissant un mawashi-geri), par contre il ont reussis a vous enlevez 10 vie. Vous
decidez donc de fuir cette region de fou et de vous rendre a Nzomiland
                    """)
        sleep(5)
        a=1
    
        
    
    