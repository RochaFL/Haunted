
define e = Character("[name]")

label start:

$ name = renpy.input("Escolha seu nome por favor")
$ name = name.strip()

show bg street day
with fade
"Após a escola era o costume  de dois amigos sairem para conversar."
" Até que um dia em uma de suas caminhadas, a dupla achou uma casa bem grande, era quase uma mansão."
"Aparentemente, estava vazia e com toda certeza abandonada, então resolveram olhar."
show nick happy open

play music "audio/happybgm.mp3" fadein 1.0 volume 0.5
"nick" "Ei [name] bora dar uma olhada? Eu sempre fico curioso pra saber"
"nick" "como essas casas  abandonadas são por dentro. O que você acha?"
label choices1:

menu:
  "Vamos lá !":
    jump choices1_a
  "Melhor não...":
    jump choices1_b
label choices1_a:
  "nick" "Isso aí, sabia que você também ficava curioso com essas coisas. "
  "nick" "Sem contar que não é todo dia que se vê uma casa desse tamanho."
  jump choices1_common
  label choices1_b:
  show nick smug
  "nick" "Você tá com medo da casa? Sério?"
  "nick" "Deixa disso, não é todo dia que a gente vê uma casa dessas abandonada. Parece até coisa de filme. "
  jump choices1_common

  label choices1_common:

scene bg mansão
with fade
"Então os dois amigos entraram na mansão, ela era realmente muito grande"
"Então, depois de chegarem perto do telhado eles ficaram ali observando a vista da cidade"
"Até o anoitecer onde eles tomaram uma decisão"
show bg janela
with fade
show nick happy close
"nick" "Ei [name], vamos voltar aqui amanhã ? Esse é um ótimo lugar. "
show nick happy open
"nick" "Não acho que alguém vá se incomodar afinal está abandonado mesmo."
e "Não tenho certeza, mas tenho que admitir que a vista e o vento que bate aqui é muito bom. "
scene bg dark
with fade
"Mesmo não tendo concordado completamente com a ideia, [name] e nick continuaram a ir na mansão."
"Fizeram pequenas alterações e a casa estava começando a, realmente, ficar parecendo um lugar deles."
"Porém, após um semana, um evento estranho aconteceu. "
show bg janela
with fade
show nick half
"nick" "Eu tinha te falado cara,que com pouca arrumação esse lugar ficaria novo."
e "Eu adoro discordar de você, porém é verdade, o lugar está completamente diferente."
show nick happy close
"nick" "Eu tinha dito."
play sound "audio/smash.mp3" fadein 1.0 volume 0.5
play music "audio/creppybgm.mp3" fadein 1.0 volume 0.5
"nick" "Você escutou isso?"
show nick worried
e "Deve ser um gato."
"nick" "Acho que eu vou conferir.Quer ir junto?"

label choices2:

menu:
  "Deve ser um gato,ignora.":
    jump choices1_c
  "Ta vamo olhar":
    jump choices1_d
label choices1_c:
show nick half
"nick" "Ok, ok. Eu vou sozinho. Preguiçoso."
scene bg janela
play sound "audio/escada.mp3" fadein 1.0 volume 0.5
"ficou um silêncio por alguns segundos, até que ..."
"nick" "[name] VEM CÁ, AGORA ! EU NÃO ACHO QUE ISSO SEJÁ UM GATO."

jump choices2_common
label choices1_d:

show nick half

"nick" "Vamos lá então."
play sound "audio/escada.mp3" fadein 1.0 volume 0.5
"Quando terminam de descer a escada, o que eles veem os impressiona"
show bg sala
with fade 
show nick scared neutral
"nick" "Falei que não era um gato."
jump choices2_common

label choices2_common:

show bg sala
with fade 
play music "audio/misterio.mp3" fadein 1.0 volume 0.5

"Então quando [name] olha pra frente, o que ele vê não era um gato e sim um homem."
show dg closed closed at right
"Ele tinha um rosto calmo  e estava bem vestido"
show dg closed open at right
"Desconhecido" "Posso saber quem são vocês?"
"Nick pula na sua frente e responde"
show nick half
"nick" "Eu quem deveria perguntar isso. Estamos aqui primeiro."
"Desconhecido" "Hahahaha os jovens de hoje são realmente estranhos"
"Desconhecido"  "Pode parecer que ela está abandonada, mas ela é minha."
show nick scared neutral at left
"nick" ".  .  ."
e "Nos desculpe, ele não fez por mal."
show nick worried
"nick" "Sim, sim... desculpa... eu... errr... achei que estava abandonada, sem dono, completamente vazia."
"nick" "Não imaginei que o dono ia aparecer ha..ha.."
"Desconhecido" "Não tem problema, eu sabia que estavam aqui."
e "Sabia?"
"Desconhecido" "Sim, mas não parecia que estavam fazendo nada de errado, até deram uma geral na casa. Então, resolvi não interferir."
e "Se me permite a pergunta, por que então você veio aqui, agora, depois de todo esse tempo?"
"Desconhecido" "Porque tenho um trabalho."
stop music
show nick happy open
"nick" "Um trabalho?A gente pode ajudar você com isso ?"
"Desconhecido" "Vocês não deviam ter vindo aqui. . . mas agora é tarde."
play music "audio/terror.mp3" fadein 1.0 volume 0.5
"Subitamente um silêncio profundo se apossou da sala, ninguém sabia o que dizer ou fazer, depois da última frase."
e "Não devia ter vindo ?Como assim ?"
"Então, finalmente, o homem faz um movimento."
show dg open closed at right
"Quando ele abriu os olhos, eles viram um olho vermelho de um jeito como nunca antes eles haviam visto."
"E junto com o olho sua expressão serena ficou séria, quase assutadora e um sentimento de terror"
"aparecia toda vez que seus olhos se encontravam com os dele."
show dg open open at right

"Desconhecido" "Só quero lembrar que, entrar aqui foi escolha de vocês."
show nick scared neutral
"Uma voz distorcida e assustadora saía de sua boca. Enquanto isso, os dois tentavam desviar o olhar"
"Ou fugir, mas as pernas de ambos estavam fixas no mesmo lugar."
"Ambos não conseguiam falar ou se mover só observar."
"Desconhecido" "Vou acabar com isso rápido."
"Em questão de segundos, o corpo antes humano, agora, havia se transformado em um ser sem forma e com garras."
scene bg demon
with fade 
" Desesperado [name] tentou correr, mas suas pernas não se moviam."
show bg sala
with fade 
show nick scared open
"nick" "AAAAAAAAAAAAAAAAAAAAAAAAAAA"
"O grito de nick conseguiu me acordar, me tirar do transe e foi quando agarrei o braço de nick "
"E saí correndo em direção da porta, enquanto ouvia os passos atrás de nós dois. "
play music "audio/Aggressor.mp3" fadein 1.0 volume 0.5
scene bg corredor
"Você começa a procurar pela porta, mas não importa o quanto você anda os corredores nunca acabam."
"E nenhuma porta parece estar levando a algum lugar, ou estão trancadas. E com os passos ficando cada vez mais próximos"
"Você acaba decidindo arriscar a sorte e entrar em um  dos quartos,tentando buscar um esconderijo seguro. "
show bg quarto
show nick scared neutral
play music "audio/calm.mp3" fadein 1.0 volume 0.5
e "Eu não sei pra onde a gente pode ir, por mais que a gente corra a gente não sai desses corredores."
"nick" ".  .  ."
e "Se essa coisa achar a gente, acabou. A gente morre! "
"você escuta nick respirar fundo."
show nick half
"nick" "Tem que ter uma saída, se ele não matou a gente naquela hora, quer dizer que a gente pode correr e ter uma chance."
e "Obrigado pelo óbvio!"
"nick" "A gente precisa pensar em uma maneira de sair dessa juntos."

label choices3:

menu:
  "Deve ter um jeito":
    jump choices1_e
  "Pode ficar aí pensando, eu to caindo fora daqui.":
    jump choices1_f
label choices1_e:
"[name] controla seu medo e fala."
e "Sim, realmente, eu só não tenho ideia de como sair daqui."
"nick" "Eu também não, afinal a gente correu a casa inteira e não saímos dos corredores."
e "Não consigo entender como estamos nos perdendo nessa casa? A gente vem aqui todo dia..."
show nick sad half
"nick" "É irônico..."

jump choices3_common

label choices1_f:
  "[name] furioso e pertubado pela situaçao, se recusa a trabalhar em equipe com quem colocou ele nessa furada."
  scene bg corredor
"ent [name] sai da sala  e começa a olhar quarto  por quarto em busca de uma saída."

"Sem sucesso [name] continua sua procura, até que ele sente algo em suas costas."

"Desconhecido" "Acabou o tempo, você ficará aqui por toda a eternidade."
"[name] sente algo atravessando seu corpo e rapidamente tudo fica preto."
scene bg dark
with fade
label bad_end5:
    call screen bad_end5_screen
    return

screen bad_end5_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("bad end 5: eternidade")
        textbutton _("Return to Main Menu") action Return()
  

label choices3_common:

"nick" "Eu acho que a gente tem que se armar, ele não deve ser invulnerável. Mesmo que a gente não consigua acabar com ele"
"nick" "se conseguirmos atrapalhar seus movimentos talvez a gente consiga tempo pra poder fugir."
e "Fugir pra onde? Tudo é um corredor."
"nick" "O lugar que a gente encontrou ele, não era corredor e tinha a porta principal da mansão. Deve ser o único jeito de sair."
e "Tem razão, mas pra isso..."
"nick" "Talvez a gente tenha que passar por ele, por isso que eu quero armas ou qualquer coisa que possa ser usada."
e "Vamos procurar nesse quarto, ele está cheio de entulho talvez tenha algo, que possa nos ajudar"
"nick" "Vamos tentar."

label choices4:

menu:
  "pegar um cano com ponta quebrada":
    jump choices1_g
  "pegar um pedaço de madeira do chao":
    jump choices1_h
  "pegar uma flecha do chão":
    jump choices1_i

label choices1_g:
e "Isso foi a coisa mais parecida com uma arma que eu achei e essa ponta quebrada daria até pra perfurar."

jump choices4_common

label choices1_h:
  "Essa coisa parece que machuca, uma porrada disso derruba qualquer um."
jump choices4_common

label choices1_i:
  "[name] Com muita confiança pega a fecha e a enfia em seu peito..."
  "Porém a única coisa que acontece é que ele morre por sangramento."
"talvez ele não tivesse determinação suficiente ou essa era somente uma flecha normal."
"Nunca saberemos."
scene bg dark
with fade
label bad_end777:
    call screen bad_end777_screen
    return

screen bad_end777_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("bad end 47: não custava tentar")
        textbutton _("Return to Main Menu") action Return()



label choices4_common:

e "nick vou usar esse aqui."
"nick" "um bastão é uma boa ideia, ataca de longe, vou pegar um também. "
e "agora só falta ir lá."
show nick half
show bg corredor
with fade 
play music "audio/misterio.mp3" fadein 1.0 volume 0.5

"Lentamente para não fazer barulho, os dois se aproximam da sala abandonada, onde estavam anteriormente."
"Chegando perto, eles ouvem um barulho e lá estava ele.A criatura estava parada perto da porta."
"Era impossível passar de maneiras normais."
show nick sad
"nick" "Como vamos passar por ele? Olha o tamanho dele, não importa o quanto a gente tente, ele vai pegar a gente antes da gente conseguir sair."
e "a gente precisa de algo pra chamar a atenção dele."
"nick" "Talvez isso dê certo."
label choices5:


menu:
  "Sugerir que nick seja a isca. ":
    jump parte3
  "sugerir que você seja a isca. ":
    jump choices1_l
  "Pensar em outra alternativa.":
    jump choices1_m
label choices1_l:
e "Eu corro na frente depois você corre e tenta sair, se alguém conseguir sair pode chamar ajuda."
"nick" "Isso é suicídio !"
e "A gente já despistou ele uma vez eu consigo de novo."
scene bg sala
with fade
show dg demon
"nick" "Não morra. Então vamos tentar."
"Nessa hora os dois contam até três e [name] sai correndo e rapidamente é avistado pela criatura."
"Que sem esperar sai da porta e vai atrás dele e nesse momento nick aproveita a chance e começa a correr até a porta."
"Porém, dessa vez, em um piscar de olhos a critura  o perfura antes de sequer chegar novamente no corredor."
"Enquanto sua visão escurece você escuta um grito de fundo, mas antes de você reconhecer sua consciência apaga."
scene bg dark
with fade
label bad_end4:
    call screen bad_end4_screen
    return

screen bad_end4_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("bad end 4: Morrer juntos")
        textbutton _("Return to Main Menu") action Return()

jump choices5_common

label choices1_j:


e "Você deveria sair correndo na frente que eu fujo por trás."
show nick realangry
"nick" "Que?"
e "É culpa sua a gente estar nessa, pra começo de conversa."
"nick" "Aí eu tenho que me matar por causa disso?"
"Em silêncio os dois se encaram até que [name] quebra o gelo."
e "Ok desculpa, esquece isso, vamos pensar em outra coisa."
show nick half
"nick" "Não me dá um susto desses."


jump choices5_common

label choices1_m:
e "Esquece o que eu disse é perigoso demais."
"nick" "A gente pode acabar morrendo desse jeito."
jump choices5_common

label choices5_common:

"Então, subitamente vocês percebem que a criatura está olhando na direçao de vocês."
play music "audio/terror.mp3" fadein 1.0 volume 0.5
show nick worried
" Vocês tentam fazer silêncio, mas estão com uma sensaçao estranha, o pânico está tomando conta de vocês."
"Então lentamente a coisa começa a se aproximar."
"Então juntando toda sua coragem você olha pra porta e vê que a criatura não está mais lá."
"Quando vocês olham pra trás, veem ela parada, olhando pra vocês e rapidamente ambos tentam sair correndo."
hide nick
show dg demon
"Em meio ao desespero cada um correu para um lado, separando os dois."
hide dg demon
play music "audio/creppybgm.mp3" fadein 1.0 volume 0.5
e "Que merda, me separei do nick !"
scene bg corredor janela
with fade 
e "Será que ele está bem?"
e "Eu não tenho ideia de que lugar é esse, que eu estou."
e "Mas eu tenho que voltar, eu não ganho nada ficando aqui!"
"Então, antes mesmo que você possa se mover uma figura humanóide, completamente preta, com olhos vermelhos aparece."
"Ela bota a mão no seu pescoço, como se fosse estrangular. Porém, calmamente a criatura diz:"
scene bg trade
"Desconhecido" "Se você aceitar meu acordo, você sai vivo. Agora, se rejeitar terá que enfrentar as consequências."
"[name] paralizado pelo medo, mal consegue pensar direito."
"Desconhecido" "Abandone nick aqui e eu te deixo fugir."

label choices6:

menu:
  "Aproveitar a oportunidade que ele está dando ou por estar tão perto, para tentar atordoá-lo":
    jump choices1_n
  "... eu... eu aceito":
    jump choices1_o
  "nunca vou fazer isso":
    jump choices1_p
label choices1_n:

"[name] estica seu braço e tentar atacar a criatura."
"Porém antes mesmo que ele consiga erguer seu braço as garras da criatura perfuram seu pescoço."
"Antes que sua consciência suma você escuta."
"Desconhecido" "Foi um erro tentar me comunicar com você."
"Desconhecido" "Você é burro!"
scene bg dark
with fade 
label bad_end3:
    call screen bad_end3_screen
    return

screen bad_end3_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("bad end 3: Erro")
        textbutton _("Return to Main Menu") action Return()

jump choices6_common

label choices1_o:
  e "Eu aceito."
"Desconhecido" "Uma resposta rápida."
show bg corredor janela
with fade 
show dg dark
play music "audio/calm.mp3" fadein 1.0 volume 0.5
e "Foi ele que me colocou aqui, pra começo de conversa não quero morrer por causa dele."

"Desconhecido" "hahahahahahahahahahahahahaha"
"Depois da risada a criatura fez um sinal, dando a entender que era pra seguí- lo."
"Juntos eles andam até a porta principal onde nick está amarrado."
show bg sala
show nick sad half at right
"nick" "[name] me ajuda! Ele me pegou !"
e "..."
"Instantaneamente ao ver a cena da criatura ao lado de [name], Nick parece entender a situação."

"nick" "Você... você me traiu?!?!"
show nick realangry
e "..."
show nick angry open
"Então em meio a fúria de Nick"
"nick"  "SEU DESGRAÇADO!!! NÃO OUSE SAIR DAQUI"
"nick" "TRAIDOR DE MERDA!!"
"nick" "SEU ME..."
"Antes de nick sequer terminar a frase, a critura enfia sua garra em seu pescoço o matando."
hide nick
show bg porta
with fade 
show dg dark
"Desconhecido" "Essa é a porta pode ir."
play sound "audio/porta.mp3" fadein 1.0 volume 0.5
e "desculpe..."
"Sai da porta em direçao a liberdade e quando sai já esta quase anoitecendo."
scene bg street night
play music "audio/terror.mp3" fadein 1.0 volume 0.5
"Então antes de sair completamente da mansão [name] sente uma presença estranha nas suas costa."
"Dessa vez não era a criatura."

"Era algo pior..."
scene bg dark
with fade

label bad_end:
    call screen bad_end1_screen
    return

screen bad_end1_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("bad end 1: maldição")
        textbutton _("Return to Main Menu") action Return()

jump choices6_common

label choices1_p:
e "Eu nunca faria algo assim, se a gente tiver que sair, a gente vai sair junto."
"Com um olhar sinistro a criatura diz:"

"Desconhecido" "A sua escolha está feita então hahahahahahahha"
"Então do mesmo jeito que ela apareceu ela desapareceu, sem deixar rastros. E você não entende o que aconteceu."
show bg corredor janela
"Porém não pode deixar isso te parar, você deve continuar. Então, você finalmente chega novamente ao salão principal."
show bg sala

jump choices6_common

label choices6_common: 

"Você olha para o lado e vê Nick."
show nick half


"No momento em que vocês se veem, vão para perto um do outro."
show nick happy open
"nick" "Ainda bem que você tá vivo!"
e "o mesmo"
"Nesse momento, os dois olham pra porta onde a criatura está encarando eles novamente."
"Dessa vez eles estavam muito próximos, não tinha como correr."
show nick scared neutral
"nick"  "O que vai acontecer agora?"
"Então um silêncio se formou enquanto a criatura quietamente observava os dois, sem fazer nenhum barulho."
"A criatura, após um bom tempo observando os dois estáticos, em um piscar de olhos se transforma em humanóide novamente."
hide nick
show dg closed open
"Desconhecido" "Meu trabalho está pronto."
"Antes mesmo que, os dois possam fazer perguntas ou algo semelhante a criatura desaparece."
"E logo em seguida ambos apagam."
scene bg dark
with fade
play music "audio/happybgm.mp3" fadein 1.0 volume 0.5
"Quando finalmente acordam, eles estão na rua e está anoitecendo."
show bg street night
"Entao quando ambos acordam e veem que não estão mais na mansão,ficam aliviados."
show nick happy close
"nick"  "A gente SAIUUUU!!!!!"
e "FINALMENTEE!!!"
"Os dois se abraçam e logo depois saem de perto da mansão para o mais longe possível."
"E dessa vez para nunca mais voltar naquele lugar."
"Assim como também decidiram nunca mais comentarem sobre essa história novamente."
scene bg dark
with fade
label true_end:
    call screen true_end_screen
    return

screen true_end_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("true ending")
        textbutton _("Return to Main Menu") action Return()

label parte3:
e "Você deveria sair correndo na frente que eu fujo por trás."
show nick realangry
"nick" "q?"
e "É culpa sua a gente estar nessa, pra começo de conversa."
"nick" "Aí eu tenho que me matar por causa disso?"
"Em silêncio os dois se encaram até que [name] quebra o gelo."
e "Ok desculpa, esquece isso. Vamos pensar em outra coisa."
show nick half
"nick" "Não me dá um susto desses!"


jump choices10_common

label choices10_common:

"Então, subitamente vocês percebem que a criatura tá olhando na direção de vocês."
play music "audio/terror.mp3" fadein 1.0 volume 0.5
show nick worried
" Vocês tentam fazer silêncio mas ficam com uma sensaçao estranha."
"Então, lentamente ela começa a se aproximar."
"Então juntando toda sua coragem você olha para porta e vê que a criatura não esta mais lá."
"Quando vocês olham pra trás vocês veem que ela está parada olhando pra vocês e rapidamente ambos tentam sair correndo."
hide nick
show dg demon
"Em meio ao desespero cada um correu para um lado,ficando separados."
hide dg demon
play music "audio/creppybgm.mp3" fadein 1.0 volume 0.5
e "Que merda, me separei do Nick!"
scene bg corredor janela
with fade 
e "Será que ele está bem?"
e "Eu não tenho ideia de que lugar é esse que eu estou."
e "Mas eu tenho que voltar, eu não ganho nada ficando aqui!"
"Então, antes mesmo que você possa se mover uma figura humanóide completamente preta com olhos vermelhos aparece."
"Ela bota a mão no seu pescoço como se fosse estrangular, porém calmamente a criatura diz:"
scene bg trade
"Desconhecido" "Se você aceitar meu acordo, você sai vivo.Se rejeitar terá que enfrentar as consequências."
"[name] paralizado pelo medo, mal consegue pensar direito."
"Desconhecido" "abandone Nick aqui e eu te deixo fugir."

label choices65:

menu:
  "Aproveitar a oportunidade que ele está tão perto para tentar atordoá-lo":
    jump choices1_na
  "... eu... eu aceito":
    jump choices1_ob
  "Nunca vou fazer isso":
    jump choices1_pa
label choices1_na:

"[name] estica seu braço e tentar atacar a criatura."
"Porém, antes mesmo que ele consiga erguer seu braço as garras da criatura perfuram seu pescoço."
"Antes que sua consciência suma você escuta:"
"Desconhecido" "Foi um erro tentar me comunicar com você."
"Desconhecido" "Você e burro!"
scene bg dark
with fade 
label bad_end35:
    call screen bad_end35_screen
    return

screen bad_end35_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("bad end 3: Erro")
        textbutton _("Return to Main Menu") action Return()

jump choices65_common

label choices1_ob:
  e "Eu aceito"
"Desconhecido" "Uma resposta rápida."
show bg corredor janela
with fade 
show dg dark
play music "audio/calm.mp3" fadein 1.0 volume 0.5
e "Foi ele que me colocou aqui pra começo de conversa.Não quero morrer por causa dele."

"Desconhecido" "hahahahahahahahahahahahahaha"
"Depois da risada a criatura fez um sinal dando a entender que era pra seguí- lo."
"Juntos vocês andam até a porta principal onde Nick está amarrado."
show bg sala
show nick sad half at right
"nick" "[name] me ajuda ele me pegou !"
e "..."
"Instantaneamente ao ver a cena da criatura ao lado de [name] nick parece entender a situaçao."

"nick" "você... você me traiu?!?!"
show nick realangry
e "..."
show nick angry open
"Então em meio a fúria de Nick."
"nick"  "SEU DESGRAÇADO!!! NÃO OUSE SAIR DAQUI!"
"nick" "TRAIDOR DE MERDA!!"
"nick" "SEU ME..."
"Antes de Nick sequer terminar a frase, a critura enfia sua garra em seu pescoço o matando."
hide nick
show bg porta
with fade 
show dg dark
"Desconhecido" "Essa é a porta pode ir."
play sound "audio/porta.mp3" fadein 1.0 volume 0.5
e "Desculpe..."
"Sai da porta em direção a liberdade e quando sai já está quase anoitecendo."
scene bg street night
play music "audio/terror.mp3" fadein 1.0 volume 0.5
"Então, antes de sair completamente da mansão [name] sente uma presença estranha nas suas costa."
"Dessa vez não era a criatura."

"Era algo pior."
scene bg dark
with fade

label bad_end15:
    call screen bad_end15_screen
    return

screen bad_end15_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("bad end 1: maldição")
        textbutton _("Return to Main Menu") action Return()

jump choices65_common

label choices1_pa:
e "Eu nunca faria algo assim, se a gente tiver que sair, a gente vai sair junto."
"Com um olhar sinistro a criatura diz:"

"Desconhecido" "A sua escolha está feita então hahahahahahahha"
"Então do mesmo jeito que ela apareceu, ela desapareceu. Sem deixar rastros... você não entende o que aconteceu."
show bg corredor janela
"Porém não podia deixar isso te parar. Você deve continuar... E então você finalmente chega novamente no salão principal."
show bg sala

jump choices65_common

label choices65_common: 

"Então você olha para o lado e vê nick."
show nick half

"Então assim que você vê o Nick tudo fica preto."
hide nick
play music "audio/misterio.mp3" fadein 1.0 volume 0.5
"Quando você acorda está amarrado em uma cadeira, com Nick ao lado da criatura."
show nick realangry
show dg dark at right
e "O que isso significa?"
"nick" "Você.. você também pretende me trair, você acha que eu não sei?"
e "Do que você está falando?!"
"nick" "Ele me deu uma escolha, eu sabia que se você ganhasse seria eu no seu lugar."
e "O que?! você é maluco?!"
"nick" "Você me culpou por ter chegado aqui."
e "Ele também me deu essa escolha, SEU IDIOTA!"
show nick angry open
"nick"  "CALA A BOCA PARA DE MENTIR ! "
e "Nick... você realmente me largou?"
"nick" "..."
"Entao, antes que [name] possa falar qualquer outra coisa, a criatura olha pra ele..."
"Um olhar quase como de pena."
"Desconhecido" "Pequeno rato traidor, seu tempo acabou."
"Antes mesmo que [name] consiga dizer algo a criatura o mata."
"Em seguida a criatura abre a porta deixando que Nick saia. Assim como havia prometido."
scene bg dark 
with fade
label bad_end2:
    call screen bad_end2_screen
    return

screen bad_end2_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("bad end 2: Traição")
        textbutton _("Return to Main Menu") action Return()
