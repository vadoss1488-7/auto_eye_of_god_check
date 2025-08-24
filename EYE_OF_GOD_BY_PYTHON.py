from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import PySimpleGUI as sg
import openpyxl

sg.theme('DarkTeal12')

layout = [
    [sg.T('find in EYE OF GOD', justification='center')],
    [sg.HorizontalSeparator()],
    [sg.T('введите название документа exel')],
    [sg.Input('123.xlsx', key='xlsx')],
    [sg.Button('начать')]
    ]

window = sg.Window('TGspamer', layout, finalize=True, size=(600,400), resizable=True)

window.set_min_size((600, 400))

window.finalize()

def working(exel):
    with open('people.txt', 'r', encoding='UTF-8') as p:
        people = p.readlines()
        print(len(people))
    with open('rezult.txt', 'w', encoding='UTF-8') as re:
        driver = webdriver.Chrome()
        driver.get('https://web.telegram.org/a/')
        sg.popup('нажми когда отсканируешь и войдёшь в аккаунт')
        try:
            driver.find_element(By.CSS_SELECTOR, '#sign-in-password').send_keys('8841')
            driver.find_element(By.CSS_SELECTOR, '#auth-password-form > div > form > button > div').click()
        except Exception:
            pass
        sleep(10)
        driver.find_element(By.CSS_SELECTOR, '#LeftColumn-main > div.Transition > div > div > div > div > div:nth-child(2) > div:nth-child(2)').click()
        sleep(15)
        for req in people + 1:
            driver.find_element(By.CSS_SELECTOR, '#editable-message-text').send_keys(req)
            sleep(18)
            rez = driver.find_element(By.CSS_SELECTOR, '#MiddleColumn > div.messages-layout > div.Transition > div > div.MessageList.custom-scroll.no-avatars.with-default-bg.scrolled > div > div.message-date-group').text
            rez2 = rez.split(req)
            print('\n1\n')
            rez1 = rez2[-1]
            re.write(f'\n {rez1} \n')
    window.close()
    wb = openpyxl.load_workbook(exel)
    ws = wb.active
    ws.delete_rows(1, ws.max_row)

    with open('rezult.txt', 'r', encoding='UTF-8') as a:
        inform = a.readlines()
    print(inform)
    print('\n')
    print('\n')
    print('\n')
    links = None
    num = None
    number = 1
    region = None
    mobile_number = None
    cantry = None
    operator = None
    date_of_born = None
    vk = None
    ok = None
    tg = None
    fb = None
    inst = None
    email = None
    fio = None
    book_name = None
    whatsapp = None
    viber = None
    car = None
    ip = None
    snils = None
    inn = None
    adress = None
    pasport = None
    fam = None
    im = None
    oth = None
    town = None
    count = 0
    imena = 0
    adr = 0
    num_fam = 0
    adr1 = list()
    fio1 = list()
    head = ('порядковый номер', 'номер телефона', 'дополниьельные номера', 'страна', 'регион', 'город', 'оператор', 'возможные имена', 'фамилия', 'имя', 'отчество', 'возможные адреса', 'дата рождения', 'vk', 'ok', 'tg', 'fb', 'inst', 'ссылки', 'email', 'whatsapp', 'viber', 'транспорт', 'ip', 'СНИЛС', 'ИНН', 'паспорт')
    ws.append(head)
    for i in inform:
        counter = 0
        try:
            a = list(i.split(':'))
            print(a)
            if 'Дата рождения' in a[0]:
                print(1)
                if ',' in a[1]:
                    date_of_born = 'несколько'
                else:
                    date_of_born = a[1].split('(')[0]
                    print(date_of_born)
                
            else:
                pass
            if 'СНИЛС' in a[0]:
                print(1)
                snils = a[1]
                print(snils)
            else:
                pass
            if 'ИНН' in a[0]:
                print(1)
                inn = a[1]
                print(inn)
            else:
                pass
            if 'Паспорт' in a[0]:
                print(1)
                pasport = a[1]
                print(pasport)
            else:
                pass

            if 'Вконтакте' in a[0]:
                print(1)
                vk1 = list(i.split('('))[1]
                vk = list(vk1.split(')'))[0]
                print(vk)
                counter += 1
            else:
                pass
            if 'Одноклассники' in a[0]:
                print(1)
                ok1 = list(i.split('('))[1]
                ok = list(ok1.split(')'))[0]
                print(ok)
                counter += 1
            else:
                pass
            if 'IP' in a[0]:
                print(1)
                ip = a[1]
                print(ip)
            else:
                pass
            if 'Email' in a[0]:
                print(1)
                email = a[1]
                print(email)
            else:
                pass
            if 'Телефон' in a[0]:
                print(1)
                num = a[1]
                print(num)
            else:
                pass
            if 'Telegram' in a[0]:
                print(1)
                tg = a[1]
                print(tg)
            else:
                pass
            if 'ранспорт' in a[0]:
                print(1)
                car = a[1]
                print(car)
            else:
                pass
            if 'Instagram' in a[0]:
                print(1)
                inst1 = list(i.split('('))[1]
                inst = list(inst1.split(')'))[0]
                print(inst)
                counter += 1
            else:
                pass
            if 'Facebook' in a[0]:
                print(1)
                fb1 = list(i.split('('))[1]
                fb = list(fb1.split(')'))[0]
                print(fb)
                counter += 1
            else:
                pass
            if 'Whatsapp' in a[0]:
                print(1)
                whatsapp = a[1]
                print(whatsapp)
            else:
                pass
            if 'Viber' in a[0]:
                print(1)
                viber = a[1]
                print(viber)
            else:
                pass
            if 'Номер' in a[0]:
                print(1)
                mobile_number = a[1]
                print(mobile_number)
            else:
                pass
            if 'Страна' in a[0]:
                print(1)
                cantry1 = a[1]
                if 'Россия' in cantry1:
                    cantry = 'Российская Федерация'
                else:
                    cantry = cantry1
                print(cantry)
            else:
                pass
            if 'Оператор' in a[0]:
                print(1)
                operator = a[1]
                print(operator)
            else:
                pass
            if 'Регион' in a[0]:
                print(1)
                region1 = a[1]
                if 'область' in region1:
                    region2 = region1.split('область')[0]
                    if 'г.Москва и Московская' in region2:
                        region = 'Московская'
                        town = 'Москва'
                    else:
                        region = region2
                print(region, town)
            else:
                pass
            if imena != 0:
                book_name = ' '
                im1 = i.split(',')
                for im2 in im1:
                    book_name =  str(book_name) + str(im2) + '\n'
                    im1 = []
                    imena = 0
                    print(book_name)
            if 'Возможные имена' in i:
                print(1)
                imena += 1
            else:
                pass
            if adr != 0:
                adress = ' '
                adr1.append(i)
                if i == '\n':
                    for adr2 in adr1:
                        adress =  str(adress)+ str(adr2)
                    adr = 0
                    adr1 = []
                    print(adress)
            if 'Возможные адреса' in i:
                print(1)
                adr += 1
            else:
                pass
            
            if num_fam != 0:
                fio1.append(i)
                fam = ' '
                im = ' '
                oth = ' '
                if i == '\n':
                    for fio2 in fio1:
                        fam = str(fam) + str(fio2.split(' ')[1]) + '\n'
                        im = str(im) + str(fio2.split(' ')[2]) + '\n'
                        oth = str(oth) + str(fio2.split(' ')[3])
                    fio1 = []
                    num_fam = 0
                    print(fam)
                    print(im)
                    print(oth)
            if 'ФИО' in a[0]:
                print(1)
                fio = a[1]
                fam = fio.split(' ')[1]
                im = fio.split(' ')[2]
                oth = fio.split(' ')[3]
                print(fio)
            elif 'ФИО' in  i:
                num_fam += 1    
            else:
                pass
            if counter != 0:
                links = ' '
                link = [ok, vk, fb, inst]
                if ok == None:
                    link.remove(ok)
                if vk == None:
                    link.remove(vk)
                if fb == None:
                    link.remove(fb)
                if inst == None:
                    link.remove(inst)
                alfa = len(link)
                for i1 in link:
                    links = str(links) + str(i1) + '\n'
                print(links)
            else:
                pass
            
            if 'Если информация не найдена, закажите «Расширенный поиск»' in i:
                lists = (number, mobile_number, num, cantry, region, town, operator, book_name, fam, im, oth, adress, date_of_born, vk, ok, tg, fb, inst, links, email, whatsapp, viber, car, ip, snils, inn, pasport)
                ws.append(lists)
                number += 1
                num = None
                book_name = None
                fio = None
                region = None
                mobile_number = None
                adress = None
                cantry = None
                operator = None
                date_of_born = None
                vk = None
                ok = None
                tg = None
                fb = None
                inst = None
                email = None
                whatsapp = None
                viber = None
                car = None
                ip = None
                snils = None
                inn = None
                pasport = None
                fam = None
                im = None
                oth = None
                town = None
                links = None
        except Exception as e:
            print(e)
            
            pass
    wb.save('exel')

    sg.popup('поиск завершён')

while True:
    try:

        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break        

        exel = values['xlsx']

        if event == 'начать':
            working(exel)

    except Exception as a:
        sg.popup('error')
        print(a)