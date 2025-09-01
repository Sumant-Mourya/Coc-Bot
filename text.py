import pyautogui



def deploy_spell(x=15,y=15):
    pyautogui.click(1101,994) #Select Clone

    pyautogui.click(240-x,525-y)
    pyautogui.click(913-x,10-y)
    pyautogui.click(1708-x,520-y)

    pyautogui.click(240,525)
    pyautogui.click(913,10)
    pyautogui.click(1708,520)

    pyautogui.click(240+x,525+y)
    pyautogui.click(913+x,10+y)
    pyautogui.click(1708+x,520+y)

def deploy_ed(x=15,y=15):
    pyautogui.click(332,994) #Select Ed

    pyautogui.click(683-x,876-y)
    pyautogui.click(491-x,714-y)
    pyautogui.click(240-x,525-y)
    pyautogui.click(515-x,312-y)
    pyautogui.click(751-x,137-y)
    pyautogui.click(913-x,10-y)
    pyautogui.click(1177-x,125-y)
    pyautogui.click(1438-x,306-y)
    pyautogui.click(1708-x,520-y)
    pyautogui.click(1539-x,675-y)
    pyautogui.click(1298-x,848-y)
    
    pyautogui.click(683,876)
    pyautogui.click(491,714)
    pyautogui.click(240,525)
    pyautogui.click(515,312)
    pyautogui.click(751,137)
    pyautogui.click(913,10)
    pyautogui.click(1177,125)
    pyautogui.click(1438,306)
    pyautogui.click(1708,520)
    pyautogui.click(1539,675)
    pyautogui.click(1298,848)
    
    pyautogui.click(683+x,8766+y)
    pyautogui.click(491+x,7146+y)
    pyautogui.click(240+x,5256+y)
    pyautogui.click(515+x,3126+y)
    pyautogui.click(751+x,1376+y)
    pyautogui.click(913+x,106+y)
    pyautogui.click(1177+x,1256+y)
    pyautogui.click(1438+x,3066+y)
    pyautogui.click(1708+x,5206+y)
    pyautogui.click(1539+x,6756+y)
    pyautogui.click(1298+x,8486+y)

def deploy_hero(x=15,y=15):
    pyautogui.click(594,994) #King
    pyautogui.click(491+x,714-y)
    pyautogui.click(491,714)
    pyautogui.click(491-x,714+y)

    pyautogui.click(714,987) #Queen
    pyautogui.click(751-x,137-y)
    pyautogui.click(751,137)
    pyautogui.click(751+x,137+y)

    pyautogui.click(836,994) #Warden
    pyautogui.click(1438+x,306-y)
    pyautogui.click(1438,306)
    pyautogui.click(1438-x,306+y)

    pyautogui.click(958,991) #Queen
    pyautogui.click(1298-x,848-y)
    pyautogui.click(1298,848)
    pyautogui.click(1298+x,848+y)

def deploy_cc(x=15,y=15):
    pyautogui.click(466,994)
    pyautogui.click(751-x,137-y)
    pyautogui.click(751,137)
    pyautogui.click(751+x,137+y)

def deployTroop():
    deploy_spell()
    deploy_ed()
    deploy_hero()
    deploy_cc()

deployTroop()